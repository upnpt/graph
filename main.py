import matplotlib.pyplot as plt
import numpy as np

# สร้าง figure 3x3
fig, axs = plt.subplots(3, 3, figsize=(12, 9))

# Main Title
fig.suptitle("My First Chart", fontsize=20)

# ------------------
# 1. Scatter Plot
# ------------------
x = np.random.rand(100)
y = np.random.rand(100)

axs[0, 0].scatter(x, y, color='black', s=10)
axs[0, 0].set_title("Scatter Plot")
axs[0, 0].set_xlabel("X")
axs[0, 0].set_ylabel("Y")

# ------------------
# 2. Bubble Chart
# ------------------
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.randint(50, 500, 50)
colors = np.random.rand(50)

axs[0, 1].scatter(x, y, s=sizes, c=colors, alpha=0.6)
axs[0, 1].set_title("Bubble Chart")
axs[0, 1].set_xlabel("X")
axs[0, 1].set_ylabel("Y")

# ------------------
# 3. Horizontal Bar
# ------------------
courses = ["A", "B", "C"]
values = [80, 50, 20]

axs[0, 2].barh(courses, values)
axs[0, 2].set_title("Horizontal Bar")
axs[0, 2].set_xlabel("Value")
axs[0, 2].set_ylabel("Category")

# ------------------
# 4. Line + Vertical Lines
# ------------------
x = np.arange(0, 10)
y = x

axs[1, 0].plot(x, y, color='green')
axs[1, 0].axvline(4, color='gray')
axs[1, 0].axvline(6, color='gray')
axs[1, 0].set_title("Line Graph")
axs[1, 0].set_xlabel("X")
axs[1, 0].set_ylabel("Y")

# ------------------
# 5. Multi Line
# ------------------
x = np.arange(1, 7)

axs[1, 1].plot(x, [2,4,2,5,2,6])
axs[1, 1].plot(x, [4,2,5,1,4,7])

axs[1, 1].set_title("Multi Line")
axs[1, 1].set_xlabel("X")
axs[1, 1].set_ylabel("Y")

# ------------------
# 6. Line With Marker
# ------------------
x = [1, 2, 3, 4]
y = [2, 5, 1, 6]

axs[1, 2].plot(x, y, marker='o')
axs[1, 2].set_title("Marker Line")
axs[1, 2].set_xlabel("X")
axs[1, 2].set_ylabel("Y")

# ------------------
# 7. Histogram
# ------------------
data = np.random.normal(50, 10, 1000)

axs[2, 0].hist(data, bins=10, color='gray')
axs[2, 0].set_title("Histogram")
axs[2, 0].set_xlabel("Value")
axs[2, 0].set_ylabel("Frequency")

# ------------------
# 8. Pie Chart
# ------------------
sizes = [30, 25, 20, 25]
labels = ['A', 'B', 'C', 'D']

axs[2, 1].pie(sizes, labels=labels, autopct='%1.1f%%')
axs[2, 1].set_title("Pie Chart")

# ------------------
# 9. Pie Chart 2
# ------------------
sizes = [25, 35, 15, 25]
labels = ['Python', 'Java', 'C++', 'JS']

axs[2, 2].pie(sizes, labels=labels, autopct='%1.1f%%')
axs[2, 2].set_title("Programming Languages")

plt.tight_layout()
plt.show()