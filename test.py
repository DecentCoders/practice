import numpy as np
from stl import mesh
from shapely.geometry import Polygon
from shapely.ops import triangulate
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path

# ================= SETTINGS =================
TEXT = "SARA"

FONT_SIZE = 90
LETTER_HEIGHT = 10
BASE_HEIGHT = 5
MARGIN = 12

CURVE_STEPS = 8   # 🔴 INCREASE THIS FOR SMOOTHER CURVES (6–12 good)

# ==========================================

faces = []

# ---------- HIGH-RES TEXT PATH ----------
font = FontProperties(family="DejaVu Sans", weight="bold")
tp = TextPath((0, 0), TEXT, size=FONT_SIZE, prop=font)

# 🔑 Interpolate curves (THIS IS THE MAGIC)
hires_path = tp.interpolated(CURVE_STEPS)

# Convert to polygons (holes preserved)
polygons = []
for poly in hires_path.to_polygons():
    p = Polygon(poly)
    if p.is_valid and p.area > 1:
        polygons.append(p)

# Merge text
text_shape = polygons[0]
for p in polygons[1:]:
    text_shape = text_shape.union(p)

minx, miny, maxx, maxy = text_shape.bounds
W = (maxx - minx) + 2 * MARGIN
D = (maxy - miny) + 2 * MARGIN

OX = MARGIN - minx
OY = MARGIN - miny

# ---------- BASE ----------
def add_box(x, y, z):
    v = np.array([
        [0,0,0],[x,0,0],[x,y,0],[0,y,0],
        [0,0,z],[x,0,z],[x,y,z],[0,y,z]
    ])
    f = [
        [0,1,2],[0,2,3],
        [4,6,5],[4,7,6],
        [0,4,5],[0,5,1],
        [1,5,6],[1,6,2],
        [2,6,7],[2,7,3],
        [3,7,4],[3,4,0]
    ]
    for a,b,c in f:
        faces.append([v[a],v[b],v[c]])

add_box(W, D, BASE_HEIGHT)

# ---------- EXTRUDE WITH HOLES ----------
def extrude(poly):
    for tri in triangulate(poly):
        pts = np.array(tri.exterior.coords)[:3]

        # bottom
        faces.append([
            [pts[0][0]+OX, pts[0][1]+OY, BASE_HEIGHT],
            [pts[1][0]+OX, pts[1][1]+OY, BASE_HEIGHT],
            [pts[2][0]+OX, pts[2][1]+OY, BASE_HEIGHT]
        ])

        # top
        faces.append([
            [pts[0][0]+OX, pts[0][1]+OY, BASE_HEIGHT+LETTER_HEIGHT],
            [pts[2][0]+OX, pts[2][1]+OY, BASE_HEIGHT+LETTER_HEIGHT],
            [pts[1][0]+OX, pts[1][1]+OY, BASE_HEIGHT+LETTER_HEIGHT]
        ])

    def wall(coords, reverse=False):
        if reverse:
            coords = coords[::-1]
        for i in range(len(coords)-1):
            x1,y1 = coords[i]
            x2,y2 = coords[i+1]
            faces.append([
                [x1+OX,y1+OY,BASE_HEIGHT],
                [x2+OX,y2+OY,BASE_HEIGHT],
                [x2+OX,y2+OY,BASE_HEIGHT+LETTER_HEIGHT]
            ])
            faces.append([
                [x1+OX,y1+OY,BASE_HEIGHT],
                [x2+OX,y2+OY,BASE_HEIGHT+LETTER_HEIGHT],
                [x1+OX,y1+OY,BASE_HEIGHT+LETTER_HEIGHT]
            ])

    wall(list(poly.exterior.coords))
    for hole in poly.interiors:
        wall(list(hole.coords), reverse=True)

# Handle multi-polygons
if text_shape.geom_type == "Polygon":
    extrude(text_shape)
else:
    for g in text_shape.geoms:
        extrude(g)

# ---------- EXPORT ----------
data = np.zeros(len(faces), dtype=mesh.Mesh.dtype)
for i, f in enumerate(faces):
    data["vectors"][i] = f

mesh.Mesh(data).save("SARA_nameplate_high_quality.stl")
print("✅ High-quality realistic nameplate created")
