import numpy as np
import matplotlib.pyplot as plt

LR = 0.1

def f1(x, y):
    return #Need Some Code

def d_f1_dx(x, y):
    return #Need Some Code

def d_f1_dy(x, y):
    return #Need Some Code

def f2(x):
    return #Need Some Code

def d_f2_dx(x):
    return #Need Some Code

def getData_f1() :
    return #Need Some Code

def getData_f2():
    return #Need Some Code


def loss_visualisation_f1(min_x, min_y, min_z):
    """Visualisation de la fonction f1"""
    x, y = getData_f1()
    X, Y = np.meshgrid(x, y)
    Z = f1(X, Y)
    ax = plt.subplot(121, projection='3d')
    ax.contour(X, Y, Z, 100)
    ax.set_xlabel('input x')
    ax.set_ylabel('input y')
    ax.set_zlabel('prediction (error)')
    ax.view_init(30, 30)
    ax.set_title('f1')
    ax.plot(min_x, min_y, min_z, markersize=10,
            marker='x', markeredgecolor='r')


def loss_visualisation_f2(min_x, min_y):
    """Visualisation de la fonction f2"""
    x = getData_f2()
    y = f2(x)
    ax = plt.subplot(122)
    ax.plot(x, y)
    ax.set_xlabel('input')
    ax.set_ylabel('prediction (error)')
    ax.set_title('f2')
    ax.plot(min_x, min_y, markersize=10, marker='x')


if __name__ == '__main__':
    #-- minimisation de la fonction f2 --#
    print("Minimisation de la fonction f2")
    # Need Some Code
    loss_visualisation_f2(1, 1)
    #-- minimisation de la fonction f1 --#
    # Need Some Code
    loss_visualisation_f1(1, 1, 1)
    plt.show()
