import numpy as np
from stl import mesh

# -------------------------- Customize these parameters --------------------------
HEART_SCALE = 0.4    # Controls the overall size of the heart
THICKNESS = 2.0      # Thickness (3D depth) of the heart
NUM_POINTS = 100     # Smoothness (more points = smoother outline)

# -------------------------- Generate 2D heart contour (parametric equation) --------------------------
t = np.linspace(0, 2 * np.pi, NUM_POINTS, endpoint=False)
# Classic heart curve equations
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
# Scale and center the heart
x = (x * HEART_SCALE)
y = (y * HEART_SCALE)

# -------------------------- Create 3D vertices (top/bottom surfaces + centers) --------------------------
vertices = []
# Top surface vertices (z = +THICKNESS/2)
for i in range(NUM_POINTS):
    vertices.append([x[i], y[i], THICKNESS / 2])
# Bottom surface vertices (z = -THICKNESS/2)
for i in range(NUM_POINTS):
    vertices.append([x[i], y[i], -THICKNESS / 2])
# Top center vertex (for closing the top surface)
vertices.append([0, 0, THICKNESS / 2])  # Index: 2*NUM_POINTS
# Bottom center vertex (for closing the bottom surface)
vertices.append([0, 0, -THICKNESS / 2]) # Index: 2*NUM_POINTS + 1

vertices = np.array(vertices)

# -------------------------- Define triangular faces --------------------------
faces = []

# 1. Side faces (connect top/bottom surfaces)
for i in range(NUM_POINTS):
    next_i = (i + 1) % NUM_POINTS
    # Split each quadrilateral side into 2 triangles
    faces.append([i, next_i, NUM_POINTS + next_i])
    faces.append([i, NUM_POINTS + next_i, NUM_POINTS + i])

# 2. Top surface (triangle fan from top center)
top_center_idx = 2 * NUM_POINTS
for i in range(NUM_POINTS):
    next_i = (i + 1) % NUM_POINTS
    faces.append([top_center_idx, i, next_i])

# 3. Bottom surface (triangle fan from bottom center)
bottom_center_idx = 2 * NUM_POINTS + 1
for i in range(NUM_POINTS):
    next_i = (i + 1) % NUM_POINTS
    faces.append([bottom_center_idx, NUM_POINTS + next_i, NUM_POINTS + i])

faces = np.array(faces)

# -------------------------- Generate and save STL --------------------------
heart_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, face in enumerate(faces):
    for j in range(3):
        heart_mesh.vectors[i][j] = vertices[face[j]]

heart_mesh.save('3d_heart.stl')
print("✅ 3D heart STL saved as '3d_heart.stl' (current folder)")