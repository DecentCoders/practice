import numpy as np
from stl import mesh

# --------------------------
# PARAMETERS (EASY TO ADJUST)
# --------------------------
plate_width = 80    # mm
plate_height = 40   # mm
plate_thickness = 5 # mm
stand_height = 20   # mm
stand_thickness = 5 # mm
letter_height = 15  # mm
letter_width = 8    # mm
letter_depth = 3    # mm (protrusion from plate)
gap_between_letters = 3 # mm

# --------------------------
# HELPER FUNCTION: CREATE A CUBE
# --------------------------
def create_cube(x0, y0, z0, dx, dy, dz):
    """
    Create a 3D cube mesh with:
    - Origin at (x0, y0, z0)
    - Dimensions (dx=width, dy=height, dz=depth)
    """
    # Define the 8 vertices of the cube
    vertices = np.array([
        [x0, y0, z0],          # 0
        [x0+dx, y0, z0],       # 1
        [x0+dx, y0+dy, z0],    # 2
        [x0, y0+dy, z0],       # 3
        [x0, y0, z0+dz],       # 4
        [x0+dx, y0, z0+dz],    # 5
        [x0+dx, y0+dy, z0+dz], # 6
        [x0, y0+dy, z0+dz]     # 7
    ])

    # Define the 12 triangles (each face has 2 triangles)
    faces = np.array([
        [0,3,1], [1,3,2], # Bottom face
        [0,4,7], [0,7,3], # Left face
        [1,2,6], [1,6,5], # Right face
        [3,7,6], [3,6,2], # Top face
        [0,1,5], [0,5,4], # Front face
        [4,5,6], [4,6,7]  # Back face
    ])

    # Create the mesh object
    cube_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, face in enumerate(faces):
        for j in range(3):
            cube_mesh.vectors[i][j] = vertices[face[j]]
    return cube_mesh

# --------------------------
# STEP 1: CREATE THE NAME PLATE BASE
# --------------------------
# Plate is centered at (0,0,0) for easy alignment
plate = create_cube(
    x0 = -plate_width/2,
    y0 = 0,
    z0 = 0,
    dx = plate_width,
    dy = plate_height,
    dz = plate_thickness
)

# --------------------------
# STEP 2: CREATE THE STAND
# --------------------------
# Stand is a tilted cube at the back of the plate (for stability)
stand = create_cube(
    x0 = -plate_width/2,
    y0 = plate_height - stand_thickness,
    z0 = 0,
    dx = plate_width,
    dy = stand_thickness,
    dz = stand_height
)

# Tilt the stand (rotate around X-axis for angled support)
theta = np.radians(45)  # 45-degree tilt
rotation_matrix = np.array([
    [1, 0, 0],
    [0, np.cos(theta), -np.sin(theta)],
    [0, np.sin(theta), np.cos(theta)]
])

# Apply rotation to stand vertices
for i in range(len(stand.vectors)):
    for j in range(3):
        stand.vectors[i][j] = np.dot(rotation_matrix, stand.vectors[i][j])

# --------------------------
# STEP 3: CREATE LETTERS "SARA"
# --------------------------
# Calculate starting X position to center the name on the plate
total_letter_width = 4*letter_width + 3*gap_between_letters
start_x = -total_letter_width/2

# Y position (center vertically on the plate)
start_y = plate_height/2 - letter_height/2

# Z position (protrude from the plate)
start_z = plate_thickness

# Helper: Create letter S (built from 3 cubes)
def create_S(x, y, z):
    s_parts = []
    # Top horizontal part of S
    s_parts.append(create_cube(x, y+letter_height*2/3, z, letter_width, letter_height/3, letter_depth))
    # Middle vertical part of S
    s_parts.append(create_cube(x+letter_width*2/3, y+letter_height/3, z, letter_width/3, letter_height/3, letter_depth))
    # Bottom horizontal part of S
    s_parts.append(create_cube(x, y, z, letter_width, letter_height/3, letter_depth))
    return np.concatenate([part.data for part in s_parts])

# Helper: Create letter A (built from 3 cubes)
def create_A(x, y, z):
    a_parts = []
    # Left side of A
    a_parts.append(create_cube(x, y, z, letter_width/3, letter_height, letter_depth))
    # Right side of A
    a_parts.append(create_cube(x+letter_width*2/3, y, z, letter_width/3, letter_height, letter_depth))
    # Crossbar of A
    a_parts.append(create_cube(x+letter_width/6, y+letter_height/2, z, letter_width*2/3, letter_height/6, letter_depth))
    return np.concatenate([part.data for part in a_parts])

# Helper: Create letter R (built from 3 cubes)
def create_R(x, y, z):
    r_parts = []
    # Vertical part of R
    r_parts.append(create_cube(x, y, z, letter_width/3, letter_height, letter_depth))
    # Top horizontal part of R
    r_parts.append(create_cube(x+letter_width/3, y+letter_height*2/3, z, letter_width*2/3, letter_height/3, letter_depth))
    # Diagonal part of R
    r_parts.append(create_cube(x+letter_width/3, y+letter_height/3, z, letter_width*2/3, letter_height/3, letter_depth))
    return np.concatenate([part.data for part in r_parts])

# Build each letter and position them
letters = []

# Letter S
s_mesh = mesh.Mesh(create_S(start_x, start_y, start_z))
letters.append(s_mesh)

# Letter A (next to S)
a1_mesh = mesh.Mesh(create_A(start_x + letter_width + gap_between_letters, start_y, start_z))
letters.append(a1_mesh)

# Letter R (next to A)
r_mesh = mesh.Mesh(create_R(start_x + 2*letter_width + 2*gap_between_letters, start_y, start_z))
letters.append(r_mesh)

# Letter A (next to R)
a2_mesh = mesh.Mesh(create_A(start_x + 3*letter_width + 3*gap_between_letters, start_y, start_z))
letters.append(a2_mesh)

# --------------------------
# STEP 4: MERGE ALL PARTS
# --------------------------
# Combine plate, stand, and letters into one mesh
all_parts = [plate, stand] + letters
combined_data = np.concatenate([part.data for part in all_parts])
final_mesh = mesh.Mesh(combined_data)

# --------------------------
# STEP 5: SAVE STL FILE
# --------------------------
final_mesh.save('Sara_Name_Plate.stl')
print("STL file 'Sara_Name_Plate.stl' generated successfully!")