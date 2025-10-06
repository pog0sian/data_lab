import matplotlib.pyplot as plt
import numpy as np
import random

def midpoint(p1, p2, roughness):
    mid = (np.array(p1) + np.array(p2)) / 2
    displacement = random.uniform(-roughness, roughness)
    return (mid[0], mid[1] + displacement)

def draw_mountain(ax, p1, p2, p3, roughness, depth):
    if depth == 0:
        triangle = plt.Polygon([p1, p2, p3], closed=True, color='gray')
        ax.add_patch(triangle)
    else:
        m12 = midpoint(p1, p2, roughness)
        m23 = midpoint(p2, p3, roughness)
        m31 = midpoint(p3, p1, roughness)
        draw_mountain(ax, p1, m12, m31, roughness/2, depth-1)
        draw_mountain(ax, m12, p2, m23, roughness/2, depth-1)
        draw_mountain(ax, m31, m23, p3, roughness/2, depth-1)
        draw_mountain(ax, m12, m23, m31, roughness/2, depth-1)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

p1 = (0, 0)
p2 = (1, 0)
p3 = (0.5, 0.8)

draw_mountain(ax, p1, p2, p3, roughness=0.2, depth=5)
plt.show()
