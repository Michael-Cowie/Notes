<div align="center">
    <h1> Rendering in React </h1>
</div>

React programming model is declarative. Developers describe what the UI should look like given the current state and React handles how to reconcile that description with the DOM. Under the hood, Reacts rendering model has strict rules and misunderstanding them can lead to bugs like components losing state or unnecessary re-renders.

At its core, a React function component is simply a JavaScript function.

```TypeScript
function MyComponent(props) {
    return <div> {props.value} </div>;
}
```

When React needs to render `MyComponent`, it calls the function. There is nothing magical here. The function runs from top to bottom, returning React elements which are plain objects describing the UI.

## Re-rendering

Whenever a components props or state change, React schedules a re-render.

1. The function is called again.
2. All variables and expressions inside it are re-executed.
3. A new tree of React element objects is created.
4. React compares this new tree to the previous one (The reconsiliation step).
5. It updates the real DOM efficiently to match the new description.
6. If differences are found, React applies updates to the DOM in a batch.

This means **everything in the body of a component is executed on every render**. Local variables, inline JSX and function definitions are all re-created.

A component re-renders when React schedules an update. This can be triggered by,

1. **State Updates** - This can occur by calling `setState` function returned by a `useState`. Re-render will not occur if it is set to the same value.
2. **Prop Changes** - If a parent re-renders and passes new props (different by reference or value) to a child.
3. **Context Changes** - Any component that consumes a context `useContext` re-renders when the context providers value changes.

Common mistakes for unwanted renders include,

1. **Defining Components Inside Others** - This will cause a new function reference each render and will cause React the remount instead of rerendering which resets the state.

2. **Unstable Props** - Passing inline objects or functions without memoization. Even if the values are the same, the reference is different so `Child` re-renders.

```TSX
<Child config={{ a: 1 }} /> // new object every render
```

## The Reconciliation Process

React doesn't blindly throw away the old UI. Instead, it runs a diff algorithm.

- For **host elements** (`<div>`, `<span>`, `<input>`), React compares tags and attributes. If the tag `div` matches, it reuses the existing DOM node and updates the props.
- For **custom components** (`<MyButton>`), React compares the **component type reference**. If it's the same **function object** as before, React preserves the component and its state. If it's a new reference, React treats it as a different component, unmounting the old one and mounting a new one.

For this reason a **common mistake is defining components inline**.

```TSX
function Parent() {
  function Child() {
    const [count, setCount] = useState(0);
    return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
  }

  return <Child />;
}
```

At first glance, this seems fine. However, every time `Parent` re-renders.

1. The body of `Parent` runs again.
2. A new `Child` function objected is created.
3. React sees that the `<Child />` in this render points **to a different function reference** than the one from the previous render.
4. React unmounts the old `Child` and mounts a new one.
5. All of `Child`s state is lost.

The result is that the counter resets to 0 whenever `Parent` re-renders. However, when we instead write,

```TSX
return <div>Hello</div>;
```

We are creating a new element object each render, but their type `div` is a string constant that never changes. React sees this is still a `<div>` and reuses the node. That's why `<div>` doesn't unmount/re-mount like `Child` did. The correct usage for this example is to define the component outside.

```TSX
function Child() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}

function Parent() {
  return <Child />;
}
```

Here, `Child` is **defined once** at module scope. Each render of `Parent` creates new React elements `<Child />`, but they all reference the same function `Child`. Thus, React preserves state across renders correctly.

When defined **outside** the React component, the function is **created once** when the module is loaded. On each render, React creates new element objects like `<Child />`, but those elements **reference the same `Child` function**. Because the type reference is stable, React reconciles it is "the same component" and preserves its state.

When defined **inside** the React component, every re-render re-executes the parent function so the `Child` function **creates a brand new function object each time**. Now, `Child` points **to a different function reference** than last render. React treats that as a different component type and thus, will unmount the old child and mount a new one and the state will reset.
