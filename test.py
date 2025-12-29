import numpy as np
from shapely.geometry import Polygon, MultiPolygon
from shapely.affinity import scale, translate
from shapely.ops import unary_union
from stl import mesh
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties

# -------------------------------
# 1. Heart shape
# -------------------------------
t = np.linspace(0, 2*np.pi, 400)
x = 16 * np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
heart_poly = Polygon(np.column_stack((x, y)))
heart_poly = scale(heart_poly, 3, 3)

# -------------------------------
# 2. Create text geometry
# -------------------------------
fp = FontProperties(family="DejaVu Sans", weight="bold")
tp = TextPath((0, 0), "RATRI", size=10, prop=fp)

polys = []
for path in tp.to_polygons():
    if len(path) > 2:
        polys.append(Polygon(path))

text_poly = unary_union(polys)

# Scale and center text on heart
text_poly = scale(text_poly, 1.5, 1.5)
minx, miny, maxx, maxy = text_poly.bounds
text_poly = translate(text_poly, xoff=-(minx+maxx)/2, yoff=-(miny+maxy)/2 + 10)

# -------------------------------
# 3. Extrusion helper
# -------------------------------
def extrude(geom, z0, h):
    verts, faces = [], []
    def one(poly, off):
        coords = list(poly.exterior.coords)
        n = len(coords)
        for x,y in coords: verts.append([x,y,z0])
        for x,y in coords: verts.append([x,y,z0+h])
        for i in range(n-1):
            faces.append([off+i, off+i+1, off+n+i])
            faces.append([off+i+1, off+n+i+1, off+n+i])
        for i in range(1,n-2):
            faces.append([off, off+i, off+i+1])
            faces.append([off+n, off+n+i, off+n+i+1])
        return 2*n

    offset = 0
    if isinstance(geom, Polygon):
        offset += one(geom, offset)
    elif isinstance(geom, MultiPolygon):
        for g in geom.geoms:
            offset += one(g, offset)

    return np.array(verts), np.array(faces)

# -------------------------------
# 4. Build mesh
# -------------------------------
hv, hf = extrude(heart_poly, 0, 4)
tv, tf = extrude(text_poly, 4, 2)
tf += len(hv)

verts = np.vstack([hv, tv])
faces = np.vstack([hf, tf])

# -------------------------------
# 5. Save STL
# -------------------------------
m = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
for i,f in enumerate(faces):
    for j in range(3):
        m.vectors[i][j] = verts[f[j]]

m.save("heart_ratri_raised.stl")
print("Saved heart_ratri_raised.stl")
