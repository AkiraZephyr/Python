import matplotlib.pyplot as plt
x = ['A', 'B', 'C']
y = [10, 5, 8]
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4)
plt.title("Histogram")
plt.show()

labels = ['Apples', 'Bananas', 'Cherries']
sizes = [30, 45, 25]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()