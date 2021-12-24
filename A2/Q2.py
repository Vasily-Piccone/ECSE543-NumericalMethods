import numpy as np


def mu(B_i, B, H):  # B and H are lists of values
    # condition to check where B falls relative to the B list
    B_cond = B_i
    # correct the B is it falls out of the range
    if B_cond > 1.9:
        B_cond = 1.9
    elif B_cond < 0:
        B_cond = 0
    # set the value of mu if B_cond = 0
    if B_cond == 0:
        mu_val = 0.0163
    else:
        for i in range(len(B)):
            if B_cond > B[i]:
                # do nothing
                pass
            else:
                index = i
                break
        H_B = H[index - 1] * (B_cond - B[index]) / (B[index - 1] - B[index]) + H[index] * (B_cond - B[index - 1]) / (B[index] - B[index - 1])
        mu_val = B_cond / H_B
    return mu_val


def f_mu_p(B_cur, B, H):
    # re-normalize B_cond
    if B_cur > 1.9:
        B_cur = 1.9
    elif B_cur < 0:
        B_cur = 0
    # set the value of mu' if B = 0
    if B_cur == 0:
        mu_p = 60.173
    else:
        for i in range(len(B)):
            if B_cur > B[i]:  # set to equal
                # do nothing
                pass
            else:
                index = i
                break
        mu_p = (H[index] - H[index - 1]) / (B[index] - B[index - 1])
    return mu_p


def f(B_i, B, H):  # psi is a guess, B_val is current
    # fill in value for mu
    func = (la / mu0 + lc/mu(B_i, B, H)) * B_i - N * I
    return func


# the previous file did not have a value here
def f_p(B_i, B, H):
    f_prime = (la / mu0 + lc / mu(B_i, B, H)) + lc*B_i*f_mu_p(B_i, B, H)  # changed to B_i
    return f_prime


def B_ext(B_i, B, H):
    B = (N*I)/(la/mu0+lc/mu(B_i, B, H))
    return B


def successive_sub(B_i, B, H):
    c = 6e-5
    f_0 = f(B_i, B, H)
    B_val = B_i
    i = 0
    cond = 1
    while abs(cond) > maxerr:
        f_cur = f(B_val, B, H)
        B_val = B_val - c*f_cur
        i += 1
        cond = f_cur / f_0
        print("------------------------------")
        print("iteration = "+str(i))
        print("B field value = "+str(B_val))
        print("Error = "+str(cond))
    return B_val


if __name__ == "__main__":
    # constants specific to the problem
    I = 8  # Current in A
    la = 0.005  # length of air gap in metres
    lc = 0.3  # length of core in metres
    A = 1e-4  # Cross-sectional area in metres^2
    mu0 = 4 * np.pi * 1e-7  # permeability of free space (H/m)
    N = 1000  # number of turns
    maxerr = 1e-6  # maximum error

    B = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
    H = [0, 14.7, 36.5, 71.7, 121.4, 197.4, 256.2, 348.7, 540.6, 1062.8, 2318.0, 4781.9, 8687.4, 13924.3, 22650.2]

    B_guess = 1
    r = successive_sub(B_guess, B, H)