import numpy as np
import matplotlib.pyplot as plt
import time

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]

pd = int(input("pixel density: "))
ni = int(input("number of iterations:"))
msc = input("color: ")

then = time.time()

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=pd)
members = get_members(c, num_iterations=ni)
plt.scatter(members.real, members.imag, color=msc, marker=",", s=1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()

now = time.time()
print("seconds: " + str(now - then))

plt.show()
