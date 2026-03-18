import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("mtcars.csv", delimiter=",", skiprows=1, usecols=(1,2,3,4,5,6))

mpg = data[:, 0]
cyl = data[:, 1]
hp = data[:, 3]
wt = data[:, 5]

plt.scatter(hp, mpg)
plt.xlabel("hp")
plt.ylabel("mpg")
plt.title("mpg vs hp")
plt.show()

plt.scatter(hp, mpg, s=wt*50)
plt.xlabel("hp")
plt.ylabel("mpg")
plt.title("mpg vs hp (veličina = wt)")
plt.show()

print("Min mpg:", np.min(mpg))
print("Max mpg:", np.max(mpg))
print("Srednji mpg:", np.mean(mpg))

mpg_6 = mpg[cyl == 6]

print("Min mpg (6 cyl):", np.min(mpg_6))
print("Max mpg (6 cyl):", np.max(mpg_6))
print("Srednji mpg (6 cyl):", np.mean(mpg_6))
