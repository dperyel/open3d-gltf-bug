import open3d as o3d
import numpy as np

if "__main__" == __name__:

    mesh = o3d.io.read_triangle_mesh('./source.stl')
    mesh.remove_duplicated_vertices()
    mesh.compute_vertex_normals()

    o3d.io.write_triangle_mesh('./out.glb', mesh)

    print(np.asarray(mesh.vertices).shape)

