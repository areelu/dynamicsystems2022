import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# w índice de crecimiento
# T saltos de tiempo
# D índice de flexión
# G índice de gravitopismo

def growth_function(old_x_pos, old_y_pos, old_z_pos, x_dir, y_dir, z_dir, W, T, D, G):
    new_pos = np.array([[old_x_pos],
                     [old_y_pos],
                     [old_z_pos]]) + W * T * root_map(x_dir, y_dir, z_dir, D, G)
    new_dir = np.array([[x_dir], [y_dir], [z_dir]])
    return pd.Series({'pos': new_pos, 'dir': new_dir})

def root_map(x, y, z, D, G):
    if x == 0:
        x = 0.00001
    alpha = np.arccos(np.radians(z))
    beta = np.arctan(np.radians(y / x))
    R = np.random.random()
    while R == 0:
        R = np.random.random()
    phi = np.radians((200 * np.pi * np.exp(np.log(R / 2))) / D)
    theta = np.radians(100 * np.pi * np.exp(np.log(R)) / (G - 100))
    a1 = np.array([np.cos(alpha) * np.cos(beta), -y * np.sin(alpha) - z * np.cos(alpha) * np.sin(beta), x])
    a2 = np.array([np.cos(alpha) * np.sin(beta), x * np.sin(alpha) + z * np.cos(alpha) * np.cos(beta), y])
    a3 = np.array([-np.sin(alpha), x * np.cos(alpha) * np.sin(beta) - y * np.cos(alpha) * np.cos(beta), z])
    a = np.array([a1, a2, a3])
    b1 = np.sin(phi) * np.cos(theta)
    b2 = np.sin(phi) * np.sin(theta)
    b3 = np.cos(phi)
    b = np.array([[b1], [b2], [b3]])
    return np.dot(a, b)


points = np.empty(shape=(60, 3, 1))
directions = np.empty(shape=(60, 3, 1))
t_x, t_y, t_z = 0.001, 0, 2
x_dir, y_dir, z_dir = 0, 0, 0
W, T, D, G = 2, 4/60, 30, 65
directions[0] = np.array([[x_dir], [y_dir], [z_dir]])
points[0] = np.array([[t_x], [t_y], [t_z]])

for i in range(1, len(points)):
    result = growth_function(t_x, t_y, t_z, x_dir, y_dir, z_dir, W, T, D, G)
    t_x, t_y, t_z = result.pos
    t_x, t_y, t_z = t_x[0], t_y[0], t_z[0]
    x_dir, y_dir, z_dir = result.dir
    x_dir, y_dir, z_dir = x_dir[0], y_dir[0], z_dir[0]
    points[i] = np.array([[t_x], [t_y], [t_z]])
    directions[i] = np.array([[x_dir], [y_dir], [z_dir]])

x = points[:, 0, 0]
y = points[:, 1, 0]
z = points[:, 2, 0]

ax, fig = plt.subplots(1)
fig.plot(y, z)
fig.invert_yaxis()
plt.show()
