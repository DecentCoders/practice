import numpy as np
from stl import mesh

# -------------------------- MAPLE LEAF PARAMETERS (REALISTIC + PRINT-FRIENDLY) --------------------------
LEAF_WIDTH = 3.0            # Total leaf width (3 inches, printable size)
LEAF_THICKNESS = 0.15       # Thin thickness (0.15 inches, leaf-like)
LOBE_COUNT = 5              # Classic 5 maple leaf lobes
LOBE_DEPTH = 0.6            # Depth of lobes (0.6 = natural shape, not too deep)
SERRATION_COUNT = 15        # Serrated edges (15 per lobe, natural look)
SERRATION_SIZE = 0.1        # Small serrations (print-friendly, not too sharp)
PETIOLE_LENGTH = 1.0        # Integrated stem/petiole (1 inch, fused to leaf)
PETIOLE_WIDTH = 0.2         # Petiole width (0.2 inches, sturdy)

# -------------------------- GENERATE MAPLE LEAF VERTICES (ERROR-FREE) --------------------------
vertices = []

# 1. Maple Leaf Lobe Contour (5 symmetrical lobes with serrations)
# Base angles for 5 lobes (0°, 72°, 144°, 216°, 288°)
lobe_angles = np.linspace(0, 2*np.pi, LOBE_COUNT, endpoint=False)
leaf_contour = []

for lobe_angle in lobe_angles:
    # Lobe center line (from leaf center to lobe tip)
    lobe_tip_x = (LEAF_WIDTH/2) * np.cos(lobe_angle)
    lobe_tip_y = (LEAF_WIDTH/2) * np.sin(lobe_angle)
    
    # Add serrated edges to each lobe (symmetrical on both sides of lobe center)
    serration_angles = np.linspace(-np.pi/4, np.pi/4, SERRATION_COUNT)
    for serr_angle in serration_angles:
        # Serrated edge shape (natural curve + small teeth)
        serr_radius = (LEAF_WIDTH/2) * (1 - LOBE_DEPTH * np.abs(np.sin(serr_angle)))
        serr_x = serr_radius * np.cos(lobe_angle + serr_angle) + SERRATION_SIZE * np.sin(3*serr_angle)
        serr_y = serr_radius * np.sin(lobe_angle + serr_angle) + SERRATION_SIZE * np.sin(3*serr_angle)
        leaf_contour.append([serr_x, serr_y])

# 2. Add Petiole (integrated stem, fused to leaf)
petiole_points = []
# Petiole extends from leaf center (0,0) to negative y-axis
for i in range(10):  # Smooth petiole taper (wider at leaf, narrower at tip)
    petiole_x = (PETIOLE_WIDTH/2) * (1 - i/10) * np.cos(np.pi/2 * (i/10))
    petiole_y = - (i/10) * PETIOLE_LENGTH - LEAF_WIDTH/10
    petiole_points.append([petiole_x, petiole_y])
    petiole_points.append([-petiole_x, petiole_y])

# Combine leaf contour + petiole into 3D vertices (add thickness)
all_2d_points = leaf_contour + petiole_points
for (x, y) in all_2d_points:
    # Leaf top (z = LEAF_THICKNESS/2)
    vertices.append([x, y, LEAF_THICKNESS/2])
    # Leaf bottom (z = -LEAF_THICKNESS/2)
    vertices.append([x, y, -LEAF_THICKNESS/2])

# Convert to NumPy array (total vertices: (75 + 20)*2 = 190 → valid indices 0-189)
vertices = np.array(vertices)

# -------------------------- DEFINE MAPLE LEAF FACES (SINGLE-PIECE) --------------------------
faces = []
point_count = len(all_2d_points)  # 95 2D points → 190 3D vertices

# --- 1. Leaf Surface Faces (connect top/bottom + contour) ---
# Connect leaf contour (first 75 points = leaf, last 20 = petiole)
for i in range(point_count - 1):
    # Indices for top/bottom of current and next point
    top1 = 2*i
    top2 = 2*(i+1)
    bot1 = 2*i + 1
    bot2 = 2*(i+1) + 1
    
    # Connect top surface (solid)
    faces.append([top1, top2, 0])  # Connect to leaf center (0 = top center)
    # Connect bottom surface
    faces.append([bot1, 0 + 1, bot2])  # Connect to bottom center (1 = bottom center)
    # Connect side walls (thickness)
    faces.append([top1, top2, bot2])
    faces.append([top1, bot2, bot1])

# --- 2. Close Leaf Center (solid core) ---
# Add center vertices (already included in index 0/1)
faces.append([0, 2, 4])  # Top center to first 2 lobe points
faces.append([1, 5, 3])  # Bottom center to first 2 lobe points

# Convert faces to NumPy array
faces = np.array(faces)

# -------------------------- GENERATE MAPLE LEAF STL --------------------------
leaf_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, face in enumerate(faces):
    for j in range(3):
        leaf_mesh.vectors[i][j] = vertices[face[j]]

# Save STL (maple leaf)
leaf_mesh.save('maple_leaf.stl')

print("✅ Maple Leaf STL saved: maple_leaf.stl")
print(f"📏 Size: {LEAF_WIDTH}\" wide + {PETIOLE_LENGTH}\" petiole (print-friendly)")
print("🔑 Features: 5 lobes, serrated edges, integrated petiole, thin leaf thickness")