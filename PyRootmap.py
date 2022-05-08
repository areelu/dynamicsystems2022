import numpy as np
import matplotlib.pyplot as plt


# w índice de crecimiento
# T saltos de tiempo
# D índice de flexión
# G índice de gravitopismo

def growth_function(y, x, z, w, T, D, G):
    return np.array([[x], [y], [z]]) + w * T * root_map(x, y, z, D, G)


def root_map(x, y, z, D, G):
    alpha = np.arccos(np.radians(z))
    betha = np.arctan(np.radians(y / x))
    R = np.random.random()
    while R == 0:
        R = np.random.random()
    phi = np.radians((200 * np.pi * np.exp(np.log(R / 2))) / D)
    theta = np.radians(100 * np.pi * np.exp(np.log(R)) / G - 100)
    a1 = np.array([np.cos(alpha) * np.cos(betha), -y + np.sin(alpha) - z * np.cos(alpha) * np.sin(betha), x])
    a2 = np.array([np.cos(alpha) * np.sin(betha), x + np.sin(alpha) + z * np.cos(alpha) * np.cos(betha), y])
    a3 = np.array([-np.sin(alpha), x * np.cos(alpha) * np.sin(betha) - y * np.cos(alpha) * np.cos(betha), z])
    a = np.array([a1, a2, a3])
    b1 = np.sin(phi) * np.cos(theta)
    b2 = np.sin(phi) * np.sin(theta)
    b3 = np.cos(phi)
    b = np.array([[b1], [b2], [b3]])
    return b


points = np.empty(shape=(60, 3, 1))
t_x, t_y, t_z = 0.001, 0, 2
W, T, D, G = 2, 4/60, 30, 65

points[0] = np.array([[t_x], [t_y], [t_z]])

for i in range(1, len(points)):
    t_x, t_y, t_z = growth_function(t_x, t_y, t_z, W, T, D, G)
    t_x, t_y, t_z = t_x[0], t_y[0], t_z[0]
    points[i] = np.array([[t_x], [t_y], [t_z]])

x = points[:, 0, 0]
y = points[:, 1, 0]
z = points[:, 2, 0]

ax, fig = plt.subplots(1)
fig.plot(x, z)
fig.invert_yaxis()
plt.show()
