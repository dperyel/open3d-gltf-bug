This repoisitory is temoporary and made only to reporoduce the bug.

`export.py` will read from `source.stl` and writes to `out.glt`.
However the byteOffset for vertex positions is wrong. As a result, when UInt8 buffer is transformed to Float32Array with a wrong byteOffset, the wrong data is calculated. For example, reading this file in BabylonJS will lead to the wrong position vectors.
The errors might be seen in the GLB report in `out_report.json` file.
