import numpy as np
import matplotlib.pyplot as plt


# calculates the y value of a function given its lagrange expansion
def lagrange_i(x_i, x_list, y_list):
    y_i = 0
    for j in range(len(x_list)):
        l = 1
        for m in range(len(x_list)):
            if m != j:
              l *= (x_i - x_list[m])/(x_list[j]-x_list[m])
        y_i = y_i + y_list[j]*l
    return y_i


#  calculates the Lagrange Extrapolation of a discrete function given a list of x coordinates,
#  corresponding y coordinates, and the number of point wanted to make the extrapolation
def lagr_interpol(x_list, y_list, num_points):
    x_pts = np.linspace(x_list[0], x_list[len(x_list)-1], num_points)
    y_pts = np.zeros(shape=(num_points, 1))
    for i in range(num_points):
        y_i = lagrange_i(x_pts[i], x_list, y_list)
        y_pts[i] = y_i
    return x_pts, y_pts


if __name__ == '__main__':
    # list of H and B values provided in the assignment
    B = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
    H = [0, 14.7, 36.5, 71.7, 121.4, 197.4, 256.2, 348.7, 540.6, 1062.8, 2318.0, 4781.9, 8687.4, 13924.3, 22650.2]

    B_1 = B[0:6]  # subdomain of B for Q1a)
    H_1 = H[0:6]  # subdomain of H for Q1a)
    ans = lagr_interpol(B_1, H_1, 100)
    x1, y1 = ans

    B_2 = [0, 1.3, 1.4, 1.7, 1.8, 1.9]  # subdomain of B for Q1b)
    H_2 = [0, 540.6, 1062.8, 8687.4, 13924.3, 22650.2]  # subdomain of H for Q1b)

    ans2 = lagr_interpol(B_2, H_2, 100)
    x2, y2 = ans2

# comment these out to test for the question 1 a), or 1b)
    plt.title("Question 1a")
    plt.xlabel("B (T)")
    plt.ylabel("H (A/m)")
    plt.plot(x1, y1, color="black", label="Lagrange Interpolation")
    plt.plot(B_1, H_1, label='Original Values')
    plt.legend(loc="upper left")
    plt.show()

# uncomment to see 1b) answer
#     plt.title("Question 1b")
#     plt.xlabel("B (T)")
#     plt.ylabel("H (A/m)")
#     plt.plot(x2, y2, color="black", label="Lagrange Interpolation")
#     plt.plot(B_2, H_2, label='Original Values')
#     plt.legend(loc="upper left")
#     plt.show()
