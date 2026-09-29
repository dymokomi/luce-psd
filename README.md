# luce-psd

Photoshop file readers for Luce/Base: documents, brush files and action
descriptors.

## Documents

The `psd` module reads documents. `parse(bytes)` reads a PSD (version 1,
8-bit RGB or grayscale, raw or PackBits channels) into a `Psd`: the document size
and its raster layers, bottom-most first, each with a name, visibility, opacity,
blend mode (by luce-image's numbering of Photoshop's 26 modes), clipping flag and
`width * height * 4` sRGB RGBA bytes at the document's size. Group markers are
passed over so their layers arrive flat. The package depends only on the
standard library; luce-image turns the buffers into pictures and luced-2d opens
`.psd` files through it.

Not read yet: PSB, 16/32-bit depth, CMYK/Lab, layer masks, adjustment layers,
text as text, and the composite image.

## Brush files

The `abr` module opens Photoshop 7-and-later brush files (`.abr` versions 6 to
10) for Luce and Base callers: `Abr.open(path)` or `Abr.parse(bytes)`, then per
preset `count()`, `text(i, "Nm")`, `number(i, "Brsh.Dmtr", fallback)`,
`has`, and `unit_key` (a number's unit such as `#Pxl`, or an enum's type).
Settings are read by dotted descriptor path; a key's padding spaces never need
spelling and a list item is its index. `tip(i, "Brsh")` decodes the sampled tip
a brush descriptor names (coverage, 255 paints) and `pattern(i, "Txtr")` the
texture pattern (gray; RGB as luma, indexed through its palette), each sized by
`tip_width`/`tip_height` and `pattern_width`/`pattern_height`. What the
settings mean is the caller's to map; luced-2d maps them onto its brushes.
Version 1 and 2 files (tips only) are refused.

## Action descriptors

The `descriptor` module parses one action descriptor into a flat node list
walked by dotted path. Brush presets use it, and PSD layer effects can too.

```
./test.sh    # builds luce-base's tests for the parser in native and C modes
```
