wt = data[:, 5]

plt.scatter(hp, mpg, s=wt*50)  
plt.xlabel("hp")
plt.ylabel("mpg")
plt.title("mpg vs hp (veličina = wt)")

plt.show()
