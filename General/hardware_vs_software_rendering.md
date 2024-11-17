Hardware rendering and Software rendering is related to 2D drawing and are two different ways to produce graphics in computer graphics.

<div align="center">
  <h1> Hardware Rendering </h1>
</div>

When you're using Hardware rendering:

- The drawing operations (lines, circles, transformations, ...) performed on the canvas object will be executed by the **GPU** of the device.

- A GPU is designed to handle the complex math operations needed for graphics rendering without being broken up into so many pieces, breaking it up into fewer pieces means that it can accomplish the same math in fewer steps and graphics are rendered more quickly as a result.

- The GPU is designed specifically to perform complex calculations required for rendering graphics. It is optimized for parallel processing, which allows it to perform multiple calculations simultaneously, making it much faster than software rendering.

<div align="center">
  <h1> Software Rendering </h1>
</div>

When you're using Hardware rendering:

- Drawing operations are executed by the **CPU**, which is much slower.

-  CPU's will break up complex math operations into several smaller pieces. Each piece takes a fixed amount of times for the CPU to calculate, so the more pieces, the longer the operation takes. Sometimes this can be very inefficient.


The CPU is the main general-purpose processor in our computer, whereas the GPU is a specialized microchip that some computers have that is optimized for doing 3D math and other calculations very quickly.