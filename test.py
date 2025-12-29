import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ------------------------------------------------------------------------------
# Step 1: Define parametric equations for 3D rose petals
# ------------------------------------------------------------------------------
def generate_rose_petals(num_petals=20, petal_resolution=50, height_resolution=30):
    """
    Generate 3D points and triangular faces for rose petals
    Based on polar rose curve (r = a*sin(nθ)) extended to 3D with curvature
    """
    # Parameters for petal shape (tune these for different rose styles)
    a = 1.5  # Base radius of petals
    n = 5    # Petal "lobes" (higher = more detailed)
    height = 4.0  # Total height of the rose bloom
    curvature = 0.8  # Petal curvature factor

    # Generate parametric coordinates
    theta = np.linspace(0, 2 * np.pi, num_petals * petal_resolution)
    phi = np.linspace(0, np.pi/2, height_resolution)
    theta, phi = np.meshgrid(theta, phi)

    # 3D polar rose equation (convert to Cartesian coordinates)
    r = a * np.sin(n * theta) * np.cos(phi) * curvature
    x = r * np.cos(theta) * np.sin(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = phi * height  # Height increases with phi

    # Add slight randomness for natural petal shape
    x += np.random.normal(0, 0.02, x.shape)
    y += np.random.normal(0, 0.02, y.shape)
    z += np.random.normal(0, 0.01, z.shape)

    # Generate triangular faces for the petals
    faces = []
    vertices = []
    vertex_idx = 0

    # Flatten vertices and create triangular mesh
    for i in range(height_resolution - 1):
        for j in range(num_petals * petal_resolution - 1):
            # Collect 4 vertices of a quad (split into 2 triangles)
            v1 = (x[i,j], y[i,j], z[i,j])
            v2 = (x[i+1,j], y[i+1,j], z[i+1,j])
            v3 = (x[i+1,j+1], y[i+1,j+1], z[i+1,j+1])
            v4 = (x[i,j+1], y[i,j+1], z[i,j+1])
            
            vertices.extend([v1, v2, v3, v4])
            
            # Add two triangles per quad
            faces.append([vertex_idx, vertex_idx+1, vertex_idx+2])
            faces.append([vertex_idx, vertex_idx+2, vertex_idx+3])
            vertex_idx += 4

    return np.array(vertices), np.array(faces)

# ------------------------------------------------------------------------------
# Step 2: Generate cylindrical stem
# ------------------------------------------------------------------------------
def generate_stem(stem_height=8, stem_radius=0.3, resolution=20):
    """Generate 3D points/faces for a cylindrical stem"""
    theta = np.linspace(0, 2 * np.pi, resolution)
    z = np.linspace(-stem_height, 0, resolution)
    theta, z = np.meshgrid(theta, z)

    # Cylinder coordinates
    x = stem_radius * np.cos(theta)
    y = stem_radius * np.sin(theta)

    # Generate faces
    faces = []
    vertices = []
    vertex_idx = 0

    for i in range(resolution - 1):
        for j in range(resolution - 1):
            v1 = (x[i,j], y[i,j], z[i,j])
            v2 = (x[i+1,j], y[i+1,j], z[i+1,j])
            v3 = (x[i+1,j+1], y[i+1,j+1], z[i+1,j+1])
            v4 = (x[i,j+1], y[i,j+1], z[i,j+1])
            
            vertices.extend([v1, v2, v3, v4])
            
            faces.append([vertex_idx, vertex_idx+1, vertex_idx+2])
            faces.append([vertex_idx, vertex_idx+2, vertex_idx+3])
            vertex_idx += 4

    # Add stem bottom cap (closed cylinder)
    cap_center = (0, 0, -stem_height)
    vertices.append(cap_center)
    cap_idx = vertex_idx
    vertex_idx += 1

    # Append all edge vertices for the cap first
    edge_start_idx = vertex_idx
    for j in range(resolution - 1):
        v_edge = (x[0, j], y[0, j], z[0, j])
        vertices.append(v_edge)
        vertex_idx += 1

    # Create triangular fan faces from center to edge vertices
    num_edges = resolution - 1
    for j in range(num_edges):
        v_curr = edge_start_idx + j
        v_next = edge_start_idx + ((j + 1) % num_edges)
        faces.append([cap_idx, v_curr, v_next])

    return np.array(vertices), np.array(faces)

# ------------------------------------------------------------------------------
# Step 3: Combine all parts and generate STL
# ------------------------------------------------------------------------------
def create_rose_stl(output_filename="3d_rose.stl"):
    # Generate individual parts
    petal_vertices, petal_faces = generate_rose_petals()
    stem_vertices, stem_faces = generate_stem()

    # Adjust stem face indices (offset by petal vertex count)
    stem_faces += len(petal_vertices)

    # Combine vertices and faces
    all_vertices = np.vstack([petal_vertices, stem_vertices])
    all_faces = np.vstack([petal_faces, stem_faces])

    # Create STL mesh object
    rose_mesh = mesh.Mesh(np.zeros(all_faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, face in enumerate(all_faces):
        for j in range(3):
            rose_mesh.vectors[i][j] = all_vertices[face[j], :]

    # Save STL file
    rose_mesh.save(output_filename)
    print(f"STL file saved as: {output_filename}")

    return all_vertices, all_faces

# ------------------------------------------------------------------------------
# Step 4: Visualize 3D rose (matplotlib preview)
# ------------------------------------------------------------------------------
def visualize_rose(vertices):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot vertices (points)
    ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], 
               c=vertices[:,2], cmap="RdYlGn", s=1, alpha=0.8)

    # Set axis labels and title
    ax.set_xlabel('X (cm)')
    ax.set_ylabel('Y (cm)')
    ax.set_zlabel('Z (cm)')
    ax.set_title('3D Rose Model Preview')

    # Equal aspect ratio for realistic view
    ax.set_aspect('equal')
    plt.show()

# ------------------------------------------------------------------------------
# Main execution
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # Generate STL file
    vertices, faces = create_rose_stl()
    
    # Preview the 3D model
    visualize_rose(vertices)