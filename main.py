import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
import uncertainties as unc
from scipy.optimize import curve_fit


#Lock-In-Verstärker
amplitude1 = np.genfromtxt('Daten3.txt', unpack = True)
x = np.linspace(30, 360, 12)
phase = np.radians(x)

def f(phase,a,b,c,d):
    return 2/np.pi*a*np.cos(b*phase+c)+d

params, covariance_matrix = curve_fit(f, phase, amplitude1)
uncertainties = np.sqrt(np.diag(covariance_matrix))

phase_plot = np.linspace(phase[0], phase[-1], 1000)

print(*uncertainties)
print(*params)


plt.plot(phase, amplitude1, '.', label = 'Messwerte')
plt.plot(phase_plot, f(phase_plot, *params), label = 'Regressionkurve')

plt.xlabel(r'$\varphi/rad$')
plt.ylabel(r'$A/V$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('Graph_3.pdf')








