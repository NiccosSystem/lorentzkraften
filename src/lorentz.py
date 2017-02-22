import numpy as np
from matplotlib import pyplot as plt

b = np.linspace(0.5, 15, 200)
u1 = 20
u2 = 40
u3 = 60

em = 1.6 * 10**(-19) / (9.11 * 10**(-31))

r1 = (b*10**(-4))**(-1) * (2*u1/em)**(1/2)
r2 = (b*10**(-4))**(-1) * (2*u2/em)**(1/2)
r3 = (b*10**(-4))**(-1) * (2*u3/em)**(1/2)

plt.plot(b, r1)
plt.plot(b, r2)
plt.plot(b, r3)
plt.show()