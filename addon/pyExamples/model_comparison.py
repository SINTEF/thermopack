#!/usr/bin/python

import sys
sys.path.append('../pycThermopack/')

import matplotlib.pyplot as plt
import numpy as np

from pyctp import extended_csp, pcsaft, tcPR


tc_pr = tcPR.tcPR()
tc_pr.init("CO2,N2")
csp = extended_csp.ext_csp()
csp.init("CO2,N2", "SRK", "Classic", "vdW", "NIST_MEOS", "C3")
pcs = pcsaft.pcsaft()
pcs.init("CO2,N2")

eoss = [tc_pr, csp, pcs]
colors = ["r", "g", "b"]

# Plot phase envelope
z = np.array([0.9, 0.1])
for i, eos in enumerate(eoss):
    label = eos.get_model_id()
    T, P, v = eos.get_envelope_twophase(1.0e4,
                                        z,
                                        maximum_pressure=1.5e7,
                                        calc_v=True)
    Tc, vc, Pc = eos.critical(z)
    plt.plot(T, P*1.0e-6, color=colors[i], label=label)
    plt.plot([Tc], [Pc*1.0e-6], color=colors[i], marker="o")
plt.ylabel(r"$P$ (MPa)")
plt.xlabel(r"$T$ (K)")
leg = plt.legend(loc="best", numpoints=1)
leg.get_frame().set_linewidth(0.0)
plt.title("CO$_2$-N$_2$ phase diagram")
plt.show()
plt.clf()
