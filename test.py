import numpy as np
from stl import mesh

n_lat = 50
n_lon = 50
radius = 1
lat = np.linspace(0, np.pi, n_lat)
lon = np.linspace(0, 2 * np.pi, n_lon)
lat_grid, lon_grid = np.meshgrid(lat, lon)
x = radius * np.sin(lat_grid) * np.cos(lon_grid)
y = radius * np.sin(lat_grid) * np.sin(lon_grid)
z = radius * np.cos(lat_grid)
vertices = np.column_stack((x.ravel(), y.ravel(), z.ravel()))
faces = []
for i in range(n_lon - 1):
    for j in range(n_lat - 1):
        v1 = i * n_lat + j
        v2 = (i + 1) * n_lat + j
        v3 = (i + 1) * n_lat + j + 1
        v4 = i * n_lat + j + 1
        faces.append([v1, v2, v3])
        faces.append([v1, v3, v4])
faces = np.array(faces)
sphere = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        sphere.vectors[i][j] = vertices[f[j]]
sphere.save('sphere.stl')