cyl = data[:, 1]

mpg_6 = mpg[cyl == 6]

print("Min mpg (6 cyl):", np.min(mpg_6))
print("Max mpg (6 cyl):", np.max(mpg_6))
print("Srednji mpg (6 cyl):", np.mean(mpg_6))
