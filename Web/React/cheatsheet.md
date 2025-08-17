<div align="center">
    <h1> React Cheatsheet </h1>
</div>

## Rendering and Reconciliation

#### What and Why

A function component is just a JavaScript function. On every render, React calls it top-to-bottom to produce _a new tree_ of element objects (virtual nodes). React compares the new element tree with the previous element tree and performs the minimal DOM mutations required to make the real UI match your description. This separation lets React batch work, prioritize updates and avoid full reflows.

#### Type Identity Matters

In React, JSX like this,

```TSX
<div className="box"> Hello </div>
```

compiles into a React element object.

```JS
{
  type: "div",              // 👈 element type
  props: { className: "box", children: "Hello" },
  key: null,
  ref: null
}
```

So every React element has a `type` field. React preserves component state when the elements type and key are unchanged between renders. For host elements (`div`, `button`, ...), the type is a string literal that is naturally stable. For custom components, the type is the **function reference** itself. If that reference changes, React must remount it. This will lose local state and running mount effects again.

```TSX
// ❌ New component function reference each Parent render, leading to Child remounting.
function Parent() {
  function Child() { const [n] = useState(0); return <div>{n}</div>; }
  return <Child/>;
}

// ✅ Stable definition at module scope, leading to Child state preserved.
function Child() { const [n] = useState(0); return <div>{n}</div>; }
function Parent() { return <Child/>; }
```

#### Keys In Lists

When rendering arrays, React uses `key` to map old children to new ones. If keys are unstable (e.g. an array index), inserting/removing/reordering causes state to stick to the wrong rows or be thrown away. An index is considered stable only if the array is completely static. Always use a stable ID from your data. Changing a key intentionally forces a remount, which is useful for resetting a form.

```TSX
{items.map(item => <Row key={item.id} item={item}/>)}
```

#### Render vs Commit

The render phase is pure computation.

1. Run the component.
2. Read state/props.
3. Computer JSX.

The commit phase is where mutations happen.

- DOM updates.
- `ref` assignments.
- Layout effects `useLayoutEffect`.
- Then passive effects `useEffect`.

Code that depends on the DOM being updated belongs in layout effects. Whereas asynchronous subscriptions and network calls belong in passive effects.

## Re-rendering Triggers

React will re-render when any of the following triggers occur.

1. **State Updates** - This occurs when either `setState` or `useReducer` dispatch mark the component as stale, scheduling a re-render.
2. **Prop Changes** - This will cause children to re-render because the parent re-runs and produces new elements for its children. If a child is memoized and props are referentially equal, React may skip re-rendering it.
3. **Context Changes** - Re-render all consumers of that context value.

#### Cascading

When a parent renders, React _attempts_ to render its subtree. You can short-circuit this with `React.memo`, but if your pass new references every render (Inline object literals, freshly created callbacks), memoization won't help. Stabilize references with `useMemo` and `useCallback` only when necessary.

#### Batched Updates and Timing

React **batches** multiple state updates that occur in the same event loop turn. A batch means React queues the updates and performs **one render/commit** afterward, instead of re-rendering after each `setState`. In React 18, batching extends beyond sync events to many async boundaries (e.g. `Promise` microtasks, `setTimeout`, `fetch` callbacks), so updates scheduled close together are typically coalesced.

Batching exists to perform fewer re-renders and thus leading to a performance improvement. Consistent state transitions leading to all updates in a batch see a coherent 'previous state' model when using the functional updater pattern.

Within a batch, `setState` does not immediately update the state variable in the current render. If you compute the next value from the stale captured value, you can overwrite or drop updates.

```TSX
setCount(count + 1); // 'count' is the value from the current render
setCount(count + 1); // uses the same stale 'count' again, therefore not cumulative
```

Instead, the functional updater is used.

```TSX
setCount(c => c + 1); // uses the latest queued value within the batch
setCount(c => c + 1); // cumulative, it there applies after the previous updater
```

React executes updater functions sequentially against the most recent pending value in the batch.

- Start with `count = 0`.
- `c => c + 1` sets it to `1`.
- `c => c + 1` sets it to `2`.

With direct values (`count + 1`), each call uses **the same** captured `count`, so multiple calls often set the same value.

```TSX
function Demo() {
  const [count, setCount] = useState(0);

  const onClick = () => {
    setCount(count + 1);     // ❌ uses stale 'count'
    setCount(count + 1);     // ❌ schedules same value again
    setCount(c => c + 1);    // ✅ cumulative
    setCount(c => c + 1);    // ✅ cumulative
  };

  return <button onClick={onClick}>Count: {count}</button>;
}
```

## Re-rendering vs Re-mounting

A **re-render** happens when props or state change but the element’s type and key stay the same. The component function runs again, React diffs and reuses existing DOM, **state and refs are preserved**, and `useEffect` only re-runs if its dependencies changed—so focus/scroll and inputs usually stay intact. Use re-render for in-place updates.

A **re-mount** happens when the element type or key changes. React unmounts the old instance (running effect cleanups), **discards the DOM**, and mounts a new instance. Therefore **state/refs reset**, inputs and focus are lost, and animations/timers start fresh. Change the key (or type) when you intentionally want a reset.

#### Props Change Only

```tsx
import React, { useEffect, useState } from "react";

function Box({ label }: { label: string }) {
  const [id] = React.useState(() => Math.random().toString(36).slice(2, 7));

  React.useEffect(() => {
    console.log(`[Box] MOUNT   id=${id}`);
    return () => console.log(`[Box] UNMOUNT id=${id}`);
  }, [id]); // Runs once on mount. Cleanup runs only on real unmount.

  return (
    <div style={{ border: "1px solid #999", padding: 8, margin: 6 }}>
      <div>
        <b>{label}</b>
      </div>
      <div>local state id = {id}</div>
    </div>
  );
}
```

Changing props only will cause a re-render, but state will be preserved. Clicking re-renders `Box` with a new `label` prop, but due to the `id` staying the same the state is preversed. For that reason `id` inside of `Box` will remain unchanged.

```tsx
function PropsChangeOnly() {
  const [n, setN] = useState(0);

  return (
    <>
      <button onClick={() => setN(n + 1)}>Increment prop ({n})</button>
      <Box label={`Child with prop=${n}`} />
    </>
  );
}
```

#### Key Changes

In the following example, every click changes `key`. This means the console shows `Box` being unmounted and mounted, i.e. `useEffect` is called again on each re-mount. Changing the `key` will force a fresh instance and reset the form state.

```tsx
function KeyChangeRemount() {
  const [keyVal, setKeyVal] = useState(0);

  return (
    <>
      <button onClick={() => setKeyVal((k) => k + 1)}>
        Change key ({keyVal})
      </button>
      {/* Changing 'key' changes identity */}
      <Box key={keyVal} label={`Key=${keyVal}`} />
    </>
  );
}
```

#### Component Type Changes

Toggling switches JSX type from `<A />` to `</B >` will cause the previous component to be unmounted and when switched back, it will be mounted again.

```tsx
function A() {
  return <Box label="Component A" />;
}
function B() {
  return <Box label="Component B" />;
}

function TypeChangeRemount() {
  const [showA, setShowA] = useState(true);

  return (
    <>
      <button onClick={() => setShowA((s) => !s)}>
        Toggle A/B (now {showA ? "A" : "B"})
      </button>
      {showA ? <A /> : <B />}
    </>
  );
}
```

#### Parent Stops Rendering

When hiding removes the child entirely, it will unmount it. Showing again mounts a new instance and then gives a new `id`.

```tsx
function ConditionalUnmount() {
  const [show, setShow] = useState(true);

  return (
    <>
      <button onClick={() => setShow((s) => !s)}>
        {show ? "Hide" : "Show"}
      </button>
      {show && <Box label="Conditional child" />}
    </>
  );
}
```

## Hooks

#### Rules of Hooks

Hooks rely on call order to associate internal state with your calls. If you conditionally call a hook, the order shifts and React reads the wrong slot. Always call hooks at the top level of the component or custom hook, never inside `if`, `for` or nested functions.

```TSX
// Don't do this!
if (props.enabled) {
  useEffect(() => {}, []); // order may change across renders
}
```

#### `useState`

The `useState` hook returns an array of two items. The first is the value whereas the other is a setter for the value. We use array destructing to assign variable names. in the syntax of,

```tsx
const [name, setName] = useState(0);
```

This stores local, reactive state scoped to the component instance. Updates are asynchronous and batched. Reading `state` immediately after `setState` call may show the old value. Use functional updates for correctness under batching.

```TSX
const [items, setItems] = useState<Item[]>([]);

const add = (x: Item) => setItems(prev => [...prev, x]); // immutable update
```

Calling `setItems` will cause the component to re-render if the previous value does not equal the new value.

#### `useMemo` and `useCallback`

These hooks cache a computed value or a function reference so they don't change identity every render and cause a re-render. The goal is to avoid recomputing expensive results and avoid invalidating memoized children/effects due to new identities.

```TSX
const onSelect = useCallback((id: string) => select(id), [select]); // stabilizes function identity
const options = useMemo(() => ({ theme, density }), [theme, density]); // stabilizes object identity
```

#### `useRef`

This hook is a mutable `.current` container that survives renders but doesn't trigger re-renders when changed. It's ideal for DOM nodes, instance variables or storing the latest value to avoid stale closures in long-lived callbacks.

```TSX
const latest = useRef(value);

useEffect(() => { latest.current = value; }, [value]);

useEffect(() => {
  const id = setInterval(() => console.log(latest.current), 1000);
  return () => clearInterval(id);
}, []);
```

#### `useEffect`

Synchronize your component with external systems (network, subscriptions, timers). The dependency array must list **all reactive values used inside**, otherwise the effect will see stale values. If listing a callback or object causes constant re-runs, stabilize it first with `useCallback` or `useMemo` rather than omitting it from the dependency array. If any value in the dependency array changes, the function passed to `useEffect` will rerun.

```TSX
const onResize = useCallback(() => setSize({ w: innerWidth, h: innerHeight }), []);

useEffect(() => {
  addEventListener('resize', onResize);
  return () => removeEventListener('resize', onResize); // cleanup on unmount/dep change
}, [onResize]);
```

The return value of `useEffect` is an optional cleanup function. React calls it to undo the side effect. The clean up runs,

1. Before the effect re-runs because any dependency changed.
2. On unmount of the component.
3. (Dev, Strict Mode) follows a slightly different rendering process to help catch leaks. It will instead `mount -> run effect -> cleanup immediately -> run effect again`.

It is primarily required to prevent memory leaks and stale subscriptions/timers by disconnecting from whatever you connected to in the effect. Always return a cleanup function for timers, subscriptions, and event listeners. Leaks and duplicate handlers are notoriously hard to debug because they accumulate quietly across renders.

#### `useLayoutEffect`

Runs after DOM mutations but before paint. Use it for reading layout or applying measurements/sync DOM reads/writes. Avoid heavy work here as it can block painting.

## Data Fetching

#### Baseline

Initialization of a component to perform a query for data population can be done be passing an empty array to the `useEffect` hook. This means it will be ran once the component is mounted. This will update the data using the `useState` hook and cause the data to rerender.

```TSX
useEffect(() => {
    const res = await fetch(...).then(...);
    ...
}, [])
```

#### React Query or TanStack Query

Although not a built-in React feature, `useQuery` can be used to help solve caching, request deduplication, retries, stale-while-revalidate, focus/refetch, background updates and pagination. This drastically reduces custom code and common bugs.

```TSX
const { data, error, isLoading } = useQuery({
  queryKey: ['user', id],
  queryFn: () => fetchJson<User>(`/api/user/${id}`),
  staleTime: 60_000,
  refetchOnWindowFocus: true
});
```

#### Parallel/Concurrent

Create all the promises first, then `await Promise.all` to avoid sequential latency, especially when you're fetching per-day resources.

```TS
const days = Array.from({ length: 7 }, (_, i) => start.add(i, 'day'));
const results = await Promise.all(days.map(d => fetchDay(d)));
```

## Lists, Keys and Identity-preserving Updates

Keys let React map old children to new children across renders. If keys change, React can't match nodes. It will remount them, losing local state, focus and scroll positions. Index keys are especially problematic with insertions/removal because index to item mapping changes.

It is best practices to use `key={item.id}`. If the backend or source data doesn’t give you a unique id field, then you should generate one yourself as soon as you load/receive the data, rather than waiting until render.

```TSX
// This is considered bad practice.
items.map((item, index) => <Row key={index} {...item} />)


// It is considered good practice to generates IDs once when ingesting the data.
const itemsWithId = rawItems.map((item) => ({
  ...item,
  id: crypto.randomUUID(), // or a hash of the content
}));
```

## React Context

Context eliminates prop-drilling by making a value available to all descendants. Any consumer re-renders when the providers value changes. If you put a rapidly changing object in context without stabilizing it, you'll cause all consumers to re-render at high frequency.

It is considered best practices to provide stable values by wrapping in `useMemo` and split contexts by change frequency (e.g. `AuthUserContext`, `PermissionsContext`, ...) rather than one monolithic context that always update.

```TSX
const AuthContext = createContext<Auth | null>(null);

function AuthProvider({ children }: PropsWithChildren) {
  const [user, setUser] = useState<User | null>(null);
  const login = useCallback(/*...*/, []);
  const logout = useCallback(/*...*/, []);
  const value = useMemo(() => ({ user, login, logout }), [user, login, logout]); // stable
  return <AuthContext.Provider value={value}> {children} </AuthContext.Provider>;
}
```

## Forms

#### Controlled Inputs

The input values are driven by React states. This gives full control for validation and formatting, but every keystroke re-renders.

```TSX
import React, { useState } from "react";

export default function ControlledForm() {
  // Step 1: React state drives the input value
  const [name, setName] = useState("ExampleName");

  // Step 2: Save function that consumes React state
  const save = (value: string) => {
    console.log("Saving value:", value);
    alert(`Saved: ${value}`);
  };

  // Step 3: handle submit by reading from state (not the DOM directly)
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault(); // prevent page reload

    save(name); // value comes from React state
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:{" "}
        <input
          value={name} // React controls value
          onChange={(e) => setName(e.target.value)} // update state on keystroke
        />
      </label>
      <button type="submit">Save</button>
    </form>
  );
}

```

#### Uncontrolled Inputs

The DOM holds the value. You read it via `ref` on submit. This reduces renders and is simpler for large forms where validation happens on submit or blue.

```tsx
import React, { useRef } from "react";

export default function UncontrolledForm() {
  // Step 1: create a ref that will eventually point to the <input>
  const nameRef = useRef<HTMLInputElement>(null);

  // Step 2: define a save function that reads the DOM value directly
  const save = (value: string) => {
    console.log("Saving value:", value);
    // pretend to send to server, etc.
    alert(`Saved: ${value}`);
  };

  // Step 3: handle form submit by grabbing the current input value
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault(); // prevent page reload

    if (nameRef.current) {
      save(nameRef.current.value); // read value directly from DOM
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:{" "}
        <input
          defaultValue="ExampleName" // starting value
          ref={nameRef} // wire up ref to DOM
        />
      </label>
      <button type="submit">Save</button>
    </form>
  );
}
```

The `ref={ref}` is telling React to attach this input DOM element to the `ref` object created using `useRef`. So after React renders, `ref.current` will point to the actual `<input>` DOM node.

#### Consistency

Don't switch a field from uncontrolled to controlled (or visa versa) mid-life React will warn. Provide `value` from the start if you plan to control it.

## Refs

**Refs** persist across renders **without causing re-renders**. They're ideal for focus management, measuring DOM nodes and caching mutable values that shouldn't trigger updates. Due to `useRef` not causing a re-render the following code will always display `log count 0`, but will log to the console the correct increased integer value.

```tsx
export default function Demo() {
  const clicks = useRef(0);

  return (
    <button
      onClick={() => console.log(++clicks.current)}
    >{`log count ${clicks.current}`}</button>
  );
}
```
