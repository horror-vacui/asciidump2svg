This project is forked from [gds2ascii](https://github.com/leoheck/gds2ascii).

Additions:
- the technology color files are now sourced with another file. No need to edit the source code for a different technology.
- added argparse for command line help and usage
- created SVG groups for layers to make them easier to handle in an SVG editor (hide layout layerwise)
- removed stroke (=edge highlight) from the objects

Improvement ideas:
- read-in object style (fill, stroke, etc.) from a file. 
- opton to merge overlapping objects. With non-uity opacity, the effective opacity increases due to the overlaps. (In `inkscape` it is equivalent to select layer group and Path --> Union command)

Known issues with [gds2ascii](https://github.com/gurleyuk/gds2ascii/issues):
- paths sometime results in meaninglessly big widths, and the text output is obscured. As a result asciidump2svg does not recognize an entry as a valid object and omits it from the SVG. Converting paths to polygons by strem-out seems to circumvent this error.
- merged polygons and paths might also results in oversized and non-physical asciidump output.


