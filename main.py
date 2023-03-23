import math

import numpy as np
import PIL.Image as im


def gen_cplx_grid(xmin, xmax, nx, ymin, ymax, ny):
    xstep = np.linspace(xmin, xmax, nx)
    ystep = np.linspace(ymin, ymax, ny)

    return xstep[:, None] + 1j*ystep


def f_cubic(x):
    return x**3 - 1


def fprime_cubic(x):
    return 3*x**2 + 2**x


def newton_iter(x, f=f_cubic, fprime=fprime_cubic):
    return x - f(x)/fprime(x)


def newton (x, max_iter=50):
    for _ in range(max_iter):
        new_x = newton_iter(x)
        if np.isclose(x, new_x):
            return new_x
        x = new_x
    return new_x


def classify(p, c):
    z0 = 1
    z1 = -0.5 + np.sqrt(3) * 1j / 2
    z2 = -0.5 - np.sqrt(3) * 1j / 2


    if np.isclose(p,z0):
        return (255,0,int(c/4))
    elif np.isclose(p, z1):
        return (int(c/4),255,0)
    elif np.isclose(p, z2):
        return (0,int(c/4),255)
    else:
        return (0,0,0)


def main():
    size_x = 1020
    size_y = 1020

    grid = gen_cplx_grid(-2, 2, size_x, -2, 2, size_y)

    image = im.new('RGB', (size_x, size_y))
    px = image.load()

    for i in range(size_x):
        for j in range(size_y):
            #print(*newton(grid[awwa\]=i, j]))
            px [i, j] = classify(newton(grid[i, j]), j)

    image.save("image.png")


if __name__ == '__main__':
    main()

"""
def newtonsmethod(f, x, times, eps = 0.001):
    if times <= 0:
        return x
    var1 = f(x + eps) - f(x - eps)
    nextx = eps * var1/2*eps
    print(var1)
    print(x - nextx)
    return newtonsmethod(f, nextx, times - 1)
"""