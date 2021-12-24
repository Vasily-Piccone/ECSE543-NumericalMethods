import numpy as np
import matplotlib.pyplot as plt


# this calculates the derivatives
def b_j(x_list, y_list, i):
    if i == 0:
        b1 = (y_list[i+1] - y_list[i])/(x_list[i+1] - x_list[i])
        b2 = (y_list[i+2] - y_list[i])/(x_list[i+2] - x_list[i])
    elif i == len(x_list) - 1:
        b1 = (y_list[i] - y_list[i-1])/(x_list[i] - x_list[i-1])
        b2 = (y_list[i + 1] - y_list[i]) / (x_list[i + 1] - x_list[i])
    else:
        b1 = (y_list[i+1] - y_list[i-1]) / (x_list[i+1] - x_list[i-1])
        b2 = (y_list[i+2] - y_list[i]) / (x_list[i+2] - x_list[i])
    return b1, b2


# calculating the v_i terms
def v(x_i, x0, x1):
    v1 = (x_i-x0)*((x1-x_i)/(x1-x0))**2
    v2 = (x_i-x1)*((x0-x_i)/(x0-x1))**2
    return v1, v2


# calculating the u_i terms
def u(x_i, x0, x1):
    u1 = (1-2*(x_i-x0)/(x0-x1))*((x_i-x1)/(x0-x1))**2  # changed (x0-x1) to (x1-x0)
    u2 = (1-2*(x1-x_i)/(x1-x0))*((x0-x_i)/(x0-x1))**2  # original
    return u1, u2


def cubic_hermite(x_i, x, y):  # x_i is a point, x is a list of points, y is a list of points
    # we are doing the interpolation for 6 points, therefore there are 5 sub-domains
    # make an array of the different coefficients
    a_arr = []
    b_arr = []

    for i in range(6):
        # add y values
        a_arr.append(y[i])
        # add b values
        if i == 0:
            b_arr.append((y[i+1] - y[i])/(x[i+1] - x[i]))
        elif i == len(x) - 1:  # big guy did smthg different
            b_arr.append((y[i] - y[i - 1]) / (x[i] - x[i - 1]))
        else:
            b_arr.append((y[i+1] - y[i-1]) / (x[i+1] - x[i-1]))
    k = 0
    # calculate where the value lies w.r.t the other arrays
    while x_i > x[k]:
        k += 1

    # Now, calculate the value of the function at that point
    u1 = (1 - 2 * (x_i - x[k-1]) / (x[k-1] - x[k])) * ((x_i - x[k]) / (x[k-1] - x[k])) ** 2
    u2 = (1 - 2 * (x_i - x[k]) / (x[k] - x[k-1])) * ((x_i - x[k-1]) / (x[k] - x[k-1])) ** 2

    v1 = (x_i - x[k-1]) * ((x_i - x[k]) / (x[k-1] - x[k])) ** 2
    v2 = (x_i - x[k]) * ((x[k-1] - x_i) / (x[k] - x[k-1])) ** 2

    val = (a_arr[k-1] * u1 + b_arr[k-1]*v1 + a_arr[k]*u2 + b_arr[k] * v2)
    return val


if __name__ == "__main__":
    B = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
    H = [0, 14.7, 36.5, 71.7, 121.4, 197.4, 256.2, 348.7, 540.6, 1062.8, 2318.0, 4781.9, 8687.4, 13924.3, 22650.2]

    B_2 = [0, 1.3, 1.4, 1.7, 1.8, 1.9]
    H_2 = [0, 540.6, 1062.8, 8687.4, 13924.3, 22650.2]

    x = np.arange(0, 1.9, 0.1)
    y_extrap = []

    for l in range(len(x)):
        y_extrap.append(cubic_hermite(x[l], B_2, H_2))

    # plot the extrapolation for Q1c)
    plt.plot(x, y_extrap, label='Cubic Hermite')
    plt.plot(B, H, label='H(B) curve')
    plt.xlabel("B field (T)")
    plt.ylabel("H field (A/M)")
    plt.legend(loc="upper left")
    plt.show()
