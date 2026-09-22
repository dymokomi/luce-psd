# luce-psd

A Photoshop document reader for Luce/Base. `parse(bytes)` reads a PSD (version 1,
8-bit RGB or grayscale, raw or PackBits channels) into a `Psd`: the document size
and its raster layers, bottom-most first, each with a name, visibility, opacity,
blend mode (by luce-image's numbering of Photoshop's 26 modes), clipping flag and
`width * height * 4` sRGB RGBA bytes at the document's size. Group markers are
passed over so their layers arrive flat. The package depends only on the
standard library; luce-image turns the buffers into pictures and luced-2d opens
`.psd` files through it.

Not read yet: PSB, 16/32-bit depth, CMYK/Lab, layer masks, adjustment layers,
text as text, and the composite image.

```
./test.sh    # builds luce-base's tests for the parser in native and C modes
```
