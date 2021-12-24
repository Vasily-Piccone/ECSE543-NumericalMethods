import numpy as np
import copy
# formula for capacitance: epsilon*4*w(energy)/V^2


def S_matrices(x1, x2, x3, x4, y1, y2, y3, y4):
    S1 = np.zeros(shape=(3, 3))
    S2 = np.zeros(shape=(3, 3))
    A = 1 / 2 * (x3 - x1) * (y1 - y2)
    # print(A)  # non-zero, which is good
    x5 = x1
    x6 = x3
    y5 = y1
    y6 = y3

    # the matrix responsible for the first triangle
    S1[0][0] = 1 / (4 * A) * ((y2 - y3) * (y2 - y3) + (x3 - x2) * (x3 - x2)) # used to be (y2 - y3) - (x3 - x2)
    S1[0][1] = 1 / (4 * A) * ((y2 - y3) * (y3 - y1) + (x3 - x2) * (x1 - x3))
    S1[0][2] = 1 / (4 * A) * ((y2 - y3) * (y1 - y2) + (x3 - x2) * (x1 - x2))

    S1[1][0] = copy.deepcopy(S1[0][1])
    S1[1][1] = 1 / (4 * A) * ((y3 - y1) * (y3 - y1) + (x1 - x3) * (x1 - x3)) # used to be  (y3 - y2)
    S1[1][2] = 1 / (4 * A) * ((y3 - y1) * (y3 - y1) + (x1 - x3) * (x1 - x2))

    S1[2][0] = copy.deepcopy(S1[0][2])
    S1[2][1] = copy.deepcopy(S1[1][2])
    S1[2][2] = 1 / (4 * A) * ((y1 - y2) * (y1 - y2) + (x1 - x2) * (x1 - x2))
    # print(S1)
    # The matrix responsible for the second triangle
    S2[0][0] = 1 / (4 * A) * ((y5 - y6) * (y5 - y6) + (x6 - x5) * (x6 - x5)) # used to be (y5 - y6) - (x6 - x5)
    S2[0][1] = 1 / (4 * A) * ((y5 - y6) * (y6 - y4) + (x6 - x5) * (x4 - x6))
    S2[0][2] = 1 / (4 * A) * ((y5 - y6) * (y4 - y5) + (x6 - x5) * (x4 - x5))

    S2[1][0] = copy.deepcopy(S2[0][1])
    S2[1][1] = 1 / (4 * A) * ((y6 - y4) * (y6 - y5) + (x4 - x6) * (x4 - x6))
    S2[1][2] = 1 / (4 * A) * ((y6 - y4) * (y6 - y4) + (x4 - x6) * (x4 - x5))

    S2[2][0] = copy.deepcopy(S2[0][2])
    S2[2][1] = copy.deepcopy(S2[1][2])
    S2[2][2] = 1 / (4 * A) * ((y4 - y5) * (y4 - y5) + (x4 - x5) * (x4 - x5))

    Sdis = np.zeros(shape=(6, 6))
    # concatenate these two matrices
    Sdis[0][0] = copy.deepcopy(S1[0][0])
    Sdis[0][1] = copy.deepcopy(S1[0][1])
    Sdis[0][2] = copy.deepcopy(S1[0][2])

    Sdis[1][0] = copy.deepcopy(S1[1][0])
    Sdis[1][1] = copy.deepcopy(S1[1][1])
    Sdis[1][2] = copy.deepcopy(S1[1][2])

    Sdis[2][0] = copy.deepcopy(S1[2][0])
    Sdis[2][1] = copy.deepcopy(S1[2][1])
    Sdis[2][2] = copy.deepcopy(S1[2][2])

    Sdis[3][3] = copy.deepcopy(S2[0][0])
    Sdis[3][4] = copy.deepcopy(S2[0][1])
    Sdis[3][5] = copy.deepcopy(S2[0][2])

    Sdis[4][3] = copy.deepcopy(S2[1][0])
    Sdis[4][4] = copy.deepcopy(S2[1][1])
    Sdis[4][5] = copy.deepcopy(S2[1][2])

    Sdis[5][3] = copy.deepcopy(S2[2][0])
    Sdis[5][4] = copy.deepcopy(S2[2][1])
    Sdis[5][5] = copy.deepcopy(S2[2][2])

    C = np.zeros(shape=(6, 4))
    C[0][0] = 1
    C[1][1] = 1
    C[2][2] = 1
    C[3][3] = 1
    C[4][0] = 1
    C[5][2] = 1
    # print(C)
    Sg = np.matmul(np.transpose(C), np.matmul(Sdis, C))

    return [Sg, S1, S2]


if __name__ == "__main__":
    x1, y1 = (0, 0.02)
    x2, y2 = (0, 0)
    x3, y3 = (0.02, 0)
    x4, y4 = (0.02, 0.02)

    mat = S_matrices(x1, x2, x3, x4, y1, y2, y3, y4)
    print(mat)