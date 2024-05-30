# PPI

Pixels per inch (ppi) and pixels per centimetre (ppcm or pixels/cm) are measurements of the pixel density of an electronic image device, such as a computer monitor or television display. Horizontal and vertical density are usually the same, as most devices have square pixels, but differ on devices that have non-square pixels. Note that **pixel density** is not the same as resolution - where the former describes the amount of detail on a physical surface or device, the latter describes the amount of pixel information regardless of its scale. Considered in another way, a pixel has no inherent size or unit (a pixel is actually a sample), but when it is printed, displayed or scanned, then the pixel has both a physical size (dimension) and a pixel density (ppi).

## Basic principles

Since most digital hardware devices use dots *or* pixels, the size of the media (in inches) and the number of pixels (or dots) are directly related by the 'pixels per inch'. The following formula gives the number of pixels, horizontally or vertically, given the physical size of a format and the **pixels per inch** of the output:

$NumberOfPixels = SizeInInches * PPI$

Pixels per inch describes the **detail** of an image file when the print size is known. For example, a 100 x 100 pixel image printed in a 2 inch square has a resolution of 50 PPI. Used this way, the measurement is meaningful when printing an image. In many applications such as Adobe Photoshop, the program is designed so that one creates new images by specifying the output device and PPI. Thus the output target is often defined upon creating the image.

## Examples 

A raster image is normally composed of a grid of *pixels*, which are the smallest *el*ement of a *pict*ure ("pix"-"el") that shows some colour, and will compose the final image in its entirety. 

The "size" of a raster image is always measured in the length of those pixels for each dimension. But that's not a physical size (like meters or inches), it's an absolute unit of quantity.

For example, a standard (real) HD screen has a physical resolution of 1920 x 1080 pixels. It means that screen has a **physical** grid of leds (or whatever) that are exactly put in 1920 columns and 1080 rows. You can actually have screens with that same resolution that 2 meters wide or even 20 centimeters (and less).

If you create an image that has the above resolution and draw a text that uses a font that is set for a *pixel* size of 1080, then you'll see the text filling the whole image vertically, but that text would be 1 meter tall in the first screen or 10cm in the second.

When you specify the *setDotsPerMeter*, you're setting the density of pixels in a physical reference.

If you draw the text setting the font size in *points*, the result will change depending on the setting of the *dots per meter*

Now, here where things gets confusing and imagine a virtual situation. I am an artist and I want to create a project that shows a black square using grids. I have two groups *a* and *b* of 4 square canvasses.

1. A 1 meter wide canvas, with grids 10cm (100 total "pixels"), meaning each grid is 10 by 10 pixels.
2. A 10 centimeter wide canvas with grids 1cm wide (again, 100 total "pixels")
3. A 1 meter wide canvas, with grids 1cm wide (10000 "pixels")
4. A 10cm wide canvas, with grids 1mm wide (10000 "pixels")

Then, I start with the first group, and I will paint in black just 1 "cell/grid" of that grid, as they were "pixels", which is the same as using `font.setPixelSize(1)`: A 1-pixel square. I will get squares that, for each canvas, will be wide:

1. 10cm
2. 1cm
3. 1cm
4. 1mm

Now, the second group. The aim is to $always$ get a 10 x 10cm square, just like using `font.setPointSize(1)` (and "point" is the reference). This means that I'll need to paint in black:

1. Just one cell in the grid
2. All cells in the grid
3. 100 Cells (10 x 10)
4. All 10000 cells in the grid

This is because each one has its `dotsPerMeter` based on the grid size and each "dot" is the expected result of a 10 x 10cm square.

1. 10
2. 100
3. 100
4. 10000

