import numpy as np
import matplotlib.pyplot as plt

# Balanced at 4,500 points for a medium graphic print
n_points = 4500
golden_angle = np.pi * (3 - np.sqrt(5))

n = np.arange(n_points)
r = np.sqrt(n)
theta = n * golden_angle

x = r * np.cos(theta)
y = r * np.sin(theta)

# Compact 8x8 canvas layout
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_facecolor('black')

# Reduced dot size scaling (r * 0.2 + 2.0) to keep the overall footprint compact
scatter = ax.scatter(x, y, c=r, cmap='hsv', s=(r * 0.2 + 2.0), alpha=0.9, edgecolors='none')

ax.set_aspect('equal')
ax.axis('off')

# 300 DPI retains  vector-like edges 
plt.tight_layout()
plt.savefig(
    'phyllotaxis_medium_shirt.png', 
    dpi=300, 
    bbox_inches='tight', 
    pad_inches=0, 
    facecolor=fig.get_facecolor()
)
print("Saved as 'phyllotaxis_medium_shirt.png' at 300 DPI!")
plt.show()
