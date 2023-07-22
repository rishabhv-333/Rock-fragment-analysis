import matplotlib.pyplot as plt
import csv
x = []
with open("data.txt",'r') as csvfile:
    plots = csv.reader(csvfile, delimiter = "\n")
    for row in plots:
        x.append(float (row[0]))
plt.scatter(range(len(x)), x)
plt.xlabel("Fragment Size")
plt.title("Rock Fragment Distribution")
plt.show()