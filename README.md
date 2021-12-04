This repoisitory is made temoporary and made only to reporoduce the bug.

`export.py` will read from `source.stl` and writes to `out.glt`.
However the byteOffset for vertex positions is wrong. As a result, when UInt8 buffer is transformed to Float32Array in some libraries (like BabylonJS) the wrong position vectors will be calculated.
The errors might be seen in the GLB report in `out_report.json` file.
