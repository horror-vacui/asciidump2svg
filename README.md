This project is forked from [gds2ascii](https://github.com/leoheck/gds2ascii).

## Additions and improvements
- merged gds2svg and asciidump into one file
- no need to set the path anymore with `setup-env.sh` 
- If the file extension of the input file is `.gds`, the input file will be still treated as a gds. Otherwise ASCII dump format is assumed.
- the technology color files are now sourced from another file. No need to edit the source code for a different technology anymore.
- added argparse for command line help and usage
- created SVG groups for layers to make them easier to handle in an SVG editor (hide layout layerwise, re-order layers, select all object on a layer together)
- layer style is assigned to the layer groups, which results in a smaller svg file
- removed stroke (=edge highlight) from the objects; (it's my personal preference)

## Improvement ideas 
- read-in a more complex object style (fill, stroke, etc.) from a file. 
- option to merge overlapping objects. With non-uity opacity, the effective opacity increases due to the overlaps. (In `inkscape` it is equivalent to select layer group and Path --> Union command)
- layer order needs to be specified. Layer numbers does not match the physical structure of the manufacturaing layers.
- **Note**: groups named after layers have been added into the svg file. These allow faster manual workaround for the last two implementation idea

 ## Known issues with [gds2ascii](https://github.com/gurleyuk/gds2ascii/issues) 
- paths sometime results in meaninglessly big widths, and the text output is obscured. As a result asciidump2svg does not recognize an entry as a valid object and omits it from the SVG. Converting paths to polygons by strem-out seems to circumvent this error.
- merged polygons and paths might also results in oversized and non-physical asciidump output.

**Suggestion**: Always compare the number of objects streamed out with the number of object processed by `ascii2dump`. The number of polygons written into the SVG is returned to the `stdout`. If you are in doubt, whether everything is processed from the gds, you can open the gds with [klayout](https://github.com/KLayout/klayout).

## Usage examples

```bash
ascii2dump2svg my_circuit.gds
```
generates `my_circuit.svg` with the default technology file.

```bash
ascii2dump2svg my_circuit.gds -c cell_to_publish -t freePDK45.csv -o publication_layout.svg
```
generates `publication_layout.svg` file from the `cell_to_publish` cell in the `my_circuit.gds` stream with the layer style definition from `freePDK45.csv`.
