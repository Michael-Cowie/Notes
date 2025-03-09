<div align="center">
  <h1> Understanding Layouts </h1>
</div>

<div align="center">
  <h2> Default Layout </h2>
</div>

Each HTML element has an inherent display behavior that determines how it interacts with other elements. This behavior is primarily categorized into **block-level elements, inline elements, and inline-block elements.**

#### Block-Level Elements

Block-level elements **take up the full width available in their parent container and start on a new line by default.** These elements naturally expand to fill the entire width of their container unless a specific width is assigned.

Some common block-level elements include,

- `<div>` - A generic container used for structuring content
- `<p>` - Represents paragraphs and takes up the full width of the container.
- `<h1>` to `<h6>` - Headings that automatically break onto a new line.
- `<ul>` and `<ol>` - Lists that structure items vertically.

```HTML
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```

Even though the text content ie short, the second `<p>` element will appear on a new line because paragraphs are block-level elements.

Block elements can be modified using `width`, `margin`, `padding` and `display` properties.

```CSS
p {
  width: 50%;
  margin: 10px auto;
  background-color: lightgray;
}
```

#### Inline Elements

Unlike block elements, **inline elements only take up as much space as necessary and do not start on a new line.** They are typically used for styling portions of text within a block.

Some common inline elements include,

- `<span>` -  A generic inline container used for styling text.
- `<a>` - Links that stay within then flow of text.
- `<strong>` and `<em>` - Used for bold and italicized text.

```HTML
<p>This is an <span style="color: red;">inline span</span> inside a paragraph.</p>
```

The `span` element does not force a line break and takes up the space for its content, making it suitable for text styling.

Since inline elements do not allow modifications to width and height directly, developers often use `inline-block` to achieve more control.

```CSS
span {
  display: inline-block;
  width: 100px;
  height: 50px;
  background-color: lightblue;
}
```

This change allows the `<span>` element to behave like a block element while remaining inline with surrounding text.

#### Inline-Block Elements

Inline-block elements combine properties of both inline and block elements. They remain inline with other elements but allow modifications to `width`, `height`, `padding` and `margin` properties.

Some common inline-block elements are,

- `<img>` - Images are inline-block by default.
- `<button>` - Buttons also behave like inline-block elements.

```HTML
<img src="image.jpg" alt="Sample Image">
<button> Click Me </button>
```
These elements align next to each other but can still have the `width` and `height` properties modified.

#### The `disply` Property

Although elements have default behaviours, CSS allows us to modify them using the `display` property.

- `block` - Makes an element behave like a block.
- `inline` - Makes an elememt behave like inline text.
- `inline-block` - Combines both behaviours.
- `none` - Hides the element from the document.

```CSS
div {
  display: inline;
}
```

This would make a `<div>` behave like an inline element instead of a block element.

<div align="center">
  <h2> Float </h2>
</div>

Introduced in early versions of CSS, `float` was originally designed to allow text to wrap around images, similar to how text flows around pictures in newspapers. Over time, developers started using it for creating multi-column layouts before newer layout methods like Flexbox and CSS Grid became popular. 

Today, while `float` still has valid use cases, **it is largely considered outdated for page layout**.

#### How Float Works

When an element is floated, **it is removed from the normal document flow** and shifted to the left or right of its container. Importantly, other content will flow around the floated element, creating a magazine-like layout effect. The property can take three primary values,

- `left` - Shifts the element to the left side of its container.

- `right` - Shifts the element to the right side of its container.

- `none` - Restores the element to its default position.

```HTML
<div class="container">
  
    <p> Hello World </p>
  
    <img src="https://placehold.co/500x100" class="float-left">
  
    <p> This text will wrap around the image, demonstrating how float allows content to flow dynamically around elements. </p>
  
    <br>
  
    <p> This text will wrap around the image, demonstrating how float allows content to flow dynamically around elements. </p>
</div>
```

```CSS
.float-left {
    float: left;
    margin-right: 15px;
}
```

<div align="center">
    <img src="./images/37.png">
</div>

Despite its initial popularity, `float` has significant drawbacks.

1. **Layout Complexity** - Floated elements can cause unexpected layout behaviours.

2. **Clearing Issues** - Floats can "escape" their parent containers, leading to layout breaks.

3. **Non-Intuitive Behaviour** - Complex layouts become difficult to manage.

#### Modern Alternatives

With the evolution of CSS, several modern layout techniques have largely replaced `float`.

**Flexbox**

- It has more predictable and powerful layout system
- Easier alignment and distribution of space
- Better handling of responsive designs

**CSS Grid**

- Two-dimensional layout system
- Precise control over rows and columns
- Native support for complex, responsive layouts.

While modern techniques are preferred, `float` still has valid use cases.

- Simple text wrapping around images.
- Legacy browser support
- Basic side-by-side element positioning. 

<div align="center">
  <h2> Document Flow </h2>
</div>

It's important to understand what the meaning of "document flow" when positioning elements. **Document flow** refers to the natural way elements are arranged on a webpage. When an element **is within document flow**, it takes up space and affects the positioning of other elements. If an element is removed from document flow, it no longer affects or interacts with the surrounding elements. It no longer takes up space **as if it wasn't there**, other elements do not adjust for it. The two positioning types that remove it from document flow is `absolute` and `fixed`.

```HTML
<div class="box1"> Box 1 </div>
<div class="box2"> Box 2 </div>
<div class="box3"> Box 3 </div>
```

```CSS
.box1 {
  width: 100px;
  height: 100px;
  background-color: red;
}

.box2 {
  width: 100px;
  height: 100px;
  background-color: blue;
}

.box3 {
  width: 100px;
  height: 100px;
  background-color: green;
}
```

In this code, we have three coloured boxes. By default, they'll stack vertically in order they appear in HTML because they're block elements. This vertical stacking happens because these elements are "in document flow". **Each element takes up space, and the next element flows naturally after it**.

<div align="center">
    <img src="./images/42.png">
</div>

Elements can be taken "out of document flow" using CSS positioning properties such as `absolute` and `fixed`. If we were to apply this property on `.box2`,

```CSS
.box2 {
  width: 100px;
  height: 100px;
  background-color: blue;
  position: absolute;  /* Removes it from document flow */
  left: 0px;           /* Moves it to the right */
  top: 0px;            /* Moves it down */
}
```

Now,

- The red box is placed at the top normally.
- The blue box is **removed from document flow**. Meaning, it no longer influences the green box.
- The green box ignores the bluebox and moves up, appearing right below the red box.

<div align="center">
    <img src="./images/43.png">
</div>

<div align="center">
  <h2> Positioning Layout </h2>
</div>

CSS provides several positioning methods that determine how elements are arranged relative to each other and their surroundings. These methods include `static`, `relative`, `absolute`, `fixed`, and `sticky` positioning. 

#### Static Positioning

```CSS
.element {
    position: static;
}
```

- The default positioning for all elements is `static`.
- Not positioned in any special way and it is always positioned according to the normal flow of the page.
- `top`, `right`, `bottom` and `left` properties have no effect.

#### Relative Positioning

`relative` was designed to let elements be shifted **slightly without affecting the layout**, which was essential for fine-tuning.

```CSS
.relative-element {
    position: relative;
    top: 10px;     /* Moves 10px down from its original position */
    left: 20px;    /* Moves 20px right from its original position */
}
```

- Element is positioned **relative to its normal position.**
- Does not affect the layout of surrounding elements when moved using `top`, `right`, `bottom` and `left`.
- The element will remain in document flow. Meaning it still takes up space **where it was originally placed.**

```HTML
<div class="container">
    <div class="box"> This is a relatively positioned box. </div>
</div>
```

```CSS
.container {
  background-color: red;
  width: 100px;
  height: 100px;
}

.box {
  position: relative;
  top: 100px;
  left: 100px;
  width: 100px;
  height: 100px;
  background-color: green;
}
```

In this particular example, we have created two boxes of equal size and displace the relatively positioned box of `top` and `left` to the same size of the `width` and `height` which results in it moving from its normal overlapping position to the corner of the red box.

<div align="center">
    <img src="./images/38.png">
</div>

#### Absolute Positioning

`absolute` was created to give developers the ability to **remove an element from the normal flow** and position it freely. This behavior was needed for complex UI elements like modals, dropdowns, or fixed overlays.

```CSS
.container {
    position: relative;  /* Important for absolute child positioning */
}

.absolute-element {
    position: absolute;
    top: 50px;
    right: 100px;
}
```

- **Removed element from document flow**. Other elements behave as if the absolute element doesn't exist.
- Positioned relative **to the nearest positioned ancestor**. If no positioned ancestor exists, it positions relative to the initial containing block, usually the viewport.
- A "positioned" element is one whose position is anything except `static`.
- **You need to specify the coordinates in order for it to work**. That is, `top`, `right`, `bottom` and `left`.

```CSS
.container {
    position: relative;  /* Important for absolute child positioning */
    background-color: purple;
}

.pushed {
  background-color: red;
  width: 300px;
  height: 100px;
  margin-left: 200px;
}

.absolute-element {
    position: absolute;
    top: 30px;
    left: 10px;
    background-color: green;
}
```

```HTML
<div class="container">
  <div class="pushed">
    <div> Hello World </div>
    <div class="absolute-element"> This is a relatively positioned box. </div>
  </div>
</div>
```

In the example above we have a container with multiple child elements. The crucial component to understand here is that the `pushed` class has no positioning applied to it, i.e. it has `position: static`. Because of this the element with the `absolute-element` class will be positioned relative to the nearest position element, which is the element with the `container` class applied to it. For this reason, it will appear outside of the red rectangle because it's not position relatively relatively to its parent.

<div align="center">
    <img src="./images/39.png">
</div>

#### Fixed Positioning

- Positioned **relative to the browser viewport.**
- Stays in the same place even when the page is scrolled.
- Useful for navigations, floating buttons.
- **Completely removed from document flow.**
- `top`, `right`, `bottom` and `left` will position it relative to the viewport.

```CSS
.fixed-box {
  position: fixed;
  top: 0px;
  right: 0px;
  width: 100px;
  height: 25px;
  background-color: red;
  color: white;
  text-align: center;
}
```

```HTML
<div class="fixed-box">Fixed Box</div>
```

The following will place a rectangle on the upper right corner of the viewport.

<div align="center">
    <img src="./images/40.png">
</div>

#### Position Sticky

- Hybrid between `relative` and `fixed` positioning. The element behaves like `relative` positioning until the user scrolls to a specified point. Once it reaches a certain position, it becomes `fixed` in place. This means the `sticky` element is within document flow until it is "stuck" and then removed from document flow.
- Requires `top`, `bottom`, `left` or `right` for it to work.


<div align="center">
    <img src="./images/41.png">
</div>

<div align="center">
  <h2> How Display and Position Work Together </h2>
</div>

CSS provides various tools to control the layout of elements on a webpage. Two fundamental properties that dictate how elements behave within a document are `display` and `position`. While each property serves a distinct purpose, their interaction can sometimes appear contradictory or confusing.

Every HTML element in a document is represented as a rectangular box. This CSS Box Model consists of content, padding, border and margin. How these boxes behave in relation to one another is determined largely by the `display` and `position` properties.

Recall that the `display` property serves two critical functions,

- **Outer Display Type** - Determines how the element participates in flow layout (`block` or `inline`).
- **Inner Display Type** - Defines how the elements children are laid out.

As a recap, `display: block` creates a block-level box that spans the full width of its container and creates a line breaks, while `display: inline` creates an inline box that flows with text. Beyond these basic types, we have more complex values like `flex` and `grid` that establish specialized formatting contexts for children.

When both `display` and `position` are applied to the same element, `position` **takes precedence in determining flow participation**, while `display` continues to **influence the internal formatting behaviour**. This hierarchy is key to understanding their seemingly contradictory interaction.

Let's example a more complex example that demonstrates how these properties affect not just the targeted elements but also their children.

```CSS
.container {
  position: relative;
  width: 600px;
  height: 400px;
  border: 3px solid black;
  margin: 20px;
  background-color: #f8f8f8;
}

.normal-block {
  display: block;
  width: 80%;
  background-color: lightblue;
  border: 2px solid blue;
}

.absolute-block {
  display: block;
  position: absolute;
  top: 125px;
  left: 100px;
  width: 200px;
  background-color: lightgreen;
  border: 2px solid green;
  padding: 15px;
}

.flex-container {
  display: flex;
  justify-content: space-between;
  margin-top: 350px;
  background-color: #eaeaea;
  padding: 15px;
  border: 2px dashed gray;
}

.flex-item {
  width: 120px;
  height: 80px;
  background-color: lightcoral;
  border: 2px solid red;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.absolute-flex-item {
  position: absolute;
  top: 280px;
  left: 250px;
  background-color: lightgoldenrodyellow;
  border-color: goldenrod;
}

.child {
  background-color: rgba(255, 255, 255, 0.7);
  border: 1px dotted #333;
  padding: 5px;
  margin: 5px 0;
  display: block;
}

.nested-block {
  margin-top: 10px;
  padding: 8px;
  background-color: rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(0, 0, 0, 0.3);
}
```

```HTML
<div class="container">
  <div class="normal-block">
    Block in normal flow
    <span class="child">Child in block</span>
  </div>
  
  <div class="absolute-block">
    Absolute block
    <span class="child">Child in absolute block</span>
    <div class="nested-block">Nested block</div>
  </div>
  
  <div class="flex-container">
    Flex container
    <div class="flex-item">Flex item 1</div>
    <div class="flex-item absolute-flex-item">
      Absolute flex item
      <span class="child">Child in absolute flex item</span>
    </div>
    <div class="flex-item">Flex item 3</div>
  </div>
</div>
```

<div align="center">
    <img src="./images/46.png">
</div>

Here we can observe many of the previously discussed interactions,

#### Normal Block and Its Child

Here, the `.normal-block` follows normal document flow as a block element. This means it will,

- Take up `80%` of the width of the container.
- It's child (The `<span>`) becomes a block due to `display: block` applied to it.
- The child remains within the normal flow of its parent

#### Absolute Block and Its Children

- The `.absolute-block` **is removed from normal flow**.
- It's positioned at `125px` from the top and `100px` from the left of the container.
- Despite being removed from document flow, **it maintains block formatting context internally.**
- Its children (The `<span>` and `<div>`) follow normal flow **within** the absolutely positioned parent.

#### Flex Container and Its Items

- The `.flex-container` establishes a flex formatting context.
- **Its child elements** are arranged according to flex layout rules.
- The normal flex items follow flex layout positioning.
- The `.absolute-flex-item` is removed from the flex layout flow due to `position: absolute`. Despite being removed from flex flow, the absolute flex items **maintains flex display characteristics internally.** Its child follow normal flow within the absolute flex item.

#### Containment Hierarchy Persists

Even when an element is removed from document flow with `position: absolute`, **it still acts as a containing block for its children**. The children follow normal flow **within** the positioned parent, not within the overall document.

An absolutely positioned element that is a flex container still maintains its flex formatting context **for its children**, even though it no longer participates in the parents normal flow. In summary, elements with `position: absolute` or `fixed` exhibit a dual nauture.

- **Externally**, they're removed from flow and positioned according to their offset properties.
- **Internally**, they maintain their display-based formatting context for their children.

Understanding these interactions has several practical applications in CSS layout.

- **Modal Dialogs and Tooltips** - Absolute positioning removes an element from flow, but that element can still contain a complex internal layout with flexbox or grid.

- **Dropdown Menus** - A dropdown can be absolutely positioned relative to its trigger, while its menu items follow normal flow within the dropdown.

- **Complex UI Components** - Components like carousels, tabbed interfaces and custom form controls often rely on this interplay between position and display.

<div align="center">
  <h1> Flexbox </h1>
</div>