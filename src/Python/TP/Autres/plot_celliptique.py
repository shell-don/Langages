import numpy as np
import matplotlib.pyplot as plt

def plot_elliptic_curve(a, b):
    '''
    Affiche la courbe éliptique associé de forme : y**2 = x**3 + a*x**2 + b.

    '''
    x_min = -2 * max(1, abs(a), abs(b))  
    x_max = 2 * max(1, abs(a), abs(b))
    x = np.linspace(x_min, x_max, 10000)

    y_max = np.sqrt(np.max(pow(x,3) + a*x + b)) if np.max(pow(x,3) + a*x + b) > 0 else 1
    y_min = -y_max
    y = np.linspace(y_min, y_max, 10000)

    X, Y = np.meshgrid(x, y)

    Z = pow(Y,2) - (pow(X,3) + a*pow(X,2) + b)

    plt.figure(figsize=(10, 8), dpi=300)
    plt.contour(X, Y, Z, levels=[0], colors='r')

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title(f"Courbe Elliptique pour a={a}, b={b}")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


#
plot_elliptic_curve(3, -1)

