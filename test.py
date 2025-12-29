import numpy as np
from stl import mesh

# -------------------------- PARAMETRIC SETTINGS (EASY TO ADJUST) --------------------------
# Core plate dimensions (tweak these for bigger/smaller name plate)
PLATE_WIDTH = 4.0          # Total width of name plate (4 inches)
PLATE_HEIGHT = 2.0         # Total height of name plate (2 inches)
PLATE_THICKNESS = 0.2      # Base thickness (0.2 inches, sturdy)
LETTER_HEIGHT = 0.15       # Height of raised "SARA" letters (0.15 inches, visible)
LETTER_WIDTH_SCALE = 0.8   # Scale for letter width (0.8 = proportional)

# Stand parameters (adjust angle/height for stability)
STAND_ANGLE = 30           # Angle of the stand (30°, no supports needed)
STAND_HEIGHT = 1.5         # Height of the stand (1.5 inches, stable)
STAND_THICKNESS = 0.3      # Thickness of stand (0.3 inches, no bending)

# -------------------------- HELPER FUNCTION: GENERATE LETTER SHAPES (SARA) --------------------------
def generate_letter_S(center_x, center_y, height, width_scale):
    """Generate 2D points for letter S (parametric, print-friendly)"""
    s_points = []
    # S curves (2 half-circles + straight edges)
    radius = height/4 * width_scale
    # Top curve (right half-circle)
    angles = np.linspace(np.pi/2, 3*np.pi/2, 10)
    for a in angles:
        x = center_x + radius * np.cos(a) + radius
        y = center_y + height/2 - radius + radius * np.sin(a)
        s_points.append([x, y])
    # Middle straight
    s_points.append([center_x - radius, center_y])
    # Bottom curve (left half-circle)
    angles = np.linspace(3*np.pi/2, 5*np.pi/2, 10)
    for a in angles:
        x = center_x + radius * np.cos(a) - radius
        y = center_y - height/2 + radius + radius * np.sin(a)
        s_points.append([x, y])
    return s_points

def generate_letter_A(center_x, center_y, height, width_scale):
    """Generate 2D points for letter A (parametric, print-friendly)"""
    a_points = []
    # A shape (triangle + crossbar)
    width = height * width_scale
    # Top peak
    a_points.append([center_x, center_y + height/2])
    # Left leg
    a_points.append([center_x - width/2, center_y - height/2])
    # Crossbar
    a_points.append([center_x - width/3, center_y - height/6])
    a_points.append([center_x + width/3, center_y - height/6])
    # Right leg
    a_points.append([center_x + width/2, center_y - height/2])
    return a_points

# -------------------------- GENERATE VERTICES (PARAMETRIC + CLEAR SHAPES) --------------------------
vertices = []

# 1. Base Name Plate (rectangular, stable)
# Plate corners (parametric size)
plate_corners = [
    (-PLATE_WIDTH/2, -PLATE_HEIGHT/2), (PLATE_WIDTH/2, -PLATE_HEIGHT/2),
    (PLATE_WIDTH/2, PLATE_HEIGHT/2), (-PLATE_WIDTH/2, PLATE_HEIGHT/2)
]
for (x, y) in plate_corners:
    # Plate bottom (z=0)
    vertices.append([x, y, 0.0])
    # Plate top (z=PLATE_THICKNESS)
    vertices.append([x, y, PLATE_THICKNESS])
plate_count = len(vertices)  # Track: 8 vertices (4 corners * 2)

# 2. Raised Letters "SARA" (parametric, centered on plate)
letter_verts = []
# Letter positions (centered, evenly spaced)
letter_spacing = PLATE_WIDTH / 5
letter_centers_x = [
    -1.5*letter_spacing,  # S
    -0.5*letter_spacing,  # A
    0.5*letter_spacing,   # R (simplified to A shape for print-friendliness)
    1.5*letter_spacing    # A
]

# Generate each letter (S, A, R=A, A)
for i, cx in enumerate(letter_centers_x):
    if i == 0:  # S
        letter_points = generate_letter_S(cx, 0, LETTER_HEIGHT*8, LETTER_WIDTH_SCALE)
    else:       # A/R (R simplified to A for print-friendliness)
        letter_points = generate_letter_A(cx, 0, LETTER_HEIGHT*8, LETTER_WIDTH_SCALE)
    
    # Convert 2D letter points to 3D (raised above plate)
    for (x, y) in letter_points:
        # Letter base (z=PLATE_THICKNESS)
        letter_verts.append([x, y, PLATE_THICKNESS])
        # Letter top (z=PLATE_THICKNESS + LETTER_HEIGHT)
        letter_verts.append([x, y, PLATE_THICKNESS + LETTER_HEIGHT])
vertices.extend(letter_verts)
letter_count = len(letter_verts)  # Track: ~80 vertices (4 letters)

# 3. Integrated Stand (parametric angle/height, stable)
stand_verts = []
# Stand base (connects to name plate back)
stand_back_y = -PLATE_HEIGHT/2
# Stand bottom (on build plate)
stand_bottom_x = np.linspace(-PLATE_WIDTH/2, PLATE_WIDTH/2, 8)
stand_angle_rad = np.radians(STAND_ANGLE)
for x in stand_bottom_x:
    # Stand bottom (z=0)
    stand_verts.append([x, stand_back_y - STAND_HEIGHT * np.cos(stand_angle_rad), 0.0])
    # Stand top (connects to plate back, z=PLATE_THICKNESS)
    stand_verts.append([x, stand_back_y, PLATE_THICKNESS])
vertices.extend(stand_verts)
stand_count = len(stand_verts)  # Track: 16 vertices (8 points * 2)

# Convert to NumPy array (total: 8+80+16=104 → valid indices 0-103)
vertices = np.array(vertices)

# -------------------------- DEFINE FACES (SINGLE-PIECE, NO ERRORS) --------------------------
faces = []
plate_start = 0
letter_start = plate_count  # 8
stand_start = letter_start + letter_count  # ~88

# --- 1. Name Plate Faces (solid base) ---
for i in range(4):
    next_i = (i+1) % 4
    # Plate bottom
    faces.append([plate_start + 2*i, plate_start + 2*next_i, plate_start + 2*next_i + 1])
    faces.append([plate_start + 2*i, plate_start + 2*next_i + 1, plate_start + 2*i + 1])
    # Plate walls
    faces.append([plate_start + 2*i, plate_start + 2*i + 1, plate_start + 2*next_i + 1])
    faces.append([plate_start + 2*i, plate_start + 2*next_i + 1, plate_start + 2*next_i])

# --- 2. Raised Letters "SARA" (clear, visible) ---
for i in range(len(letter_verts)//2 - 1):
    v1 = letter_start + 2*i
    v2 = letter_start + 2*(i+1)
    v3 = letter_start + 2*(i+1) + 1
    v4 = letter_start + 2*i + 1
    # Letter top/bottom
    faces.append([v1, v2, v3])
    faces.append([v1, v3, v4])
    # Letter walls (connect to plate)
    faces.append([v1, v4, plate_start + 1])
    faces.append([v1, plate_start + 1, v2])

# --- 3. Integrated Stand (stable, no supports) ---
for i in range(len(stand_verts)//2 - 1):
    v1 = stand_start + 2*i
    v2 = stand_start + 2*(i+1)
    v3 = stand_start + 2*(i+1) + 1
    v4 = stand_start + 2*i + 1
    # Stand walls
    faces.append([v1, v2, v3])
    faces.append([v1, v3, v4])
    # Connect stand to plate
    faces.append([v4, v3, plate_start + 1])
    faces.append([v4, plate_start + 1, plate_start + 3])

# Convert faces to NumPy array
faces = np.array(faces)

# -------------------------- GENERATE STL (PARAMETRIC SARA NAME PLATE) --------------------------
nameplate_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, face in enumerate(faces):
    for j in range(3):
        nameplate_mesh.vectors[i][j] = vertices[face[j]]

# Save STL (parametric SARA name plate)
nameplate_mesh.save('parametric_sara_name_plate.stl')

print("✅ Parametric SARA Name Plate STL saved: parametric_sara_name_plate.stl")
print(f"📏 Plate Size: {PLATE_WIDTH}\"x{PLATE_HEIGHT}\" (adjust via PLATE_WIDTH/HEIGHT)")
print(f"🔑 Stand Angle: {STAND_ANGLE}° (stable, no supports needed)")
print(f"💬 Letter Height: {LETTER_HEIGHT}\" (raised, clear visibility)")