import numpy as np
import matplotlib.pyplot as plt

# To use LaTeX in the plots
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})
# for Palatino and other serif fonts use:
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})
plt.rcParams.update({
  "text.usetex": True,
  "font.family": "Helvetica"
})

# constants used in the problem
E = 0.220  # in volts
R = 500  # in Ohms
Vt = 0.025  # in volts
Isa = 0.6e-6  # in Amps
Isb = 1.2e-6  # in Amps


# Calculates the vector F which solves the equation F = 0
def F(v):  # v is a 2 x 1 vector which contains the voltage values of the circuit
    f1 = (E - v[0]) / R - Isa * (np.exp((v[0] - v[1]) / Vt) - 1)
    f2 = Isa*(np.exp((v[0]-v[1]) / Vt)-1)-Isb * (np.exp((v[1] / Vt)) - 1)
    F = np.array([f1, f2])
    return F


# compute the Jacobian
def Jacobian(v):
    J = np.zeros(shape=(2, 2))
    J[0][0] = -1/R - (Isa / Vt) * np.exp((v[0] - v[1]) / Vt)
    J[0][1] = (Isa / Vt) * np.exp((v[0] - v[1]) / Vt)
    J[1][0] = (Isa / Vt) * np.exp((v[0] - v[1]) / Vt)
    J[1][1] = -(Isb / Vt) * np.exp(v[1] / Vt) - (Isa/Vt)*np.exp((v[0]-v[1])/Vt)
    return J


# uses the above two functions to calculate the voltage solution to the circuit
def newton_raphson(maxerr):
    i = 0
    Vnew = np.zeros(shape=(2, 1))
    dV_vec = []
    val_vec = []
    conv = False
    while not conv:
        i += 1
        F_p = Jacobian(Vnew)  # calculate the Jacobian given teh current voltage values
        eff = F(Vnew)  # calculate the value of the F vector for the current voltage values
        dV = np.multiply(np.dot(np.linalg.inv(F_p), eff), -1)  # compute dV
        crit_val = np.linalg.norm(dV, 2)  # compute the 2-norm of dV for convergence criteria
        Vnew = np.add(Vnew, dV)  # compute new voltage value for next step

        dV_vec.append(crit_val)
        val_vec.append(Vnew)
        print("------------------------------------")
        print("iteration = "+str(i))
        print("Jacobian = "+str(F_p))
        print("F-vector = "+str(eff))
        print("\u0394 V = "+str(dV))
        if crit_val < maxerr:
            break
    return Vnew, dV_vec, i, val_vec


if __name__ == "__main__":
    error = 10e-15  # the maximum allowable error
    val = newton_raphson(error)
    # plot error in the log scale
    dV_norm_err = val[1]
    iter_no = val[2]
    ans = val[3]
    print("------------------------------------")
    print(ans[7])

    # Plot the 10log_10 of dV
    x_val = np.linspace(1, iter_no, iter_no)
    dV = 10*np.log10(dV_norm_err)
    plt.plot(x_val, dV)
    plt.xlabel("Number of Iterations")
    plt.ylabel("log(2-norm dV)")
    plt.show()