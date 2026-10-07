import matplotlib.pyplot as plt
import numpy as np

# ตั้งค่าขนาดตัวอักษร
plt.rcParams.update({'font.size': 10})

# สร้าง Figure และ Subplots 3x3
fig, axs = plt.subplots(3, 3, figsize=(15, 10))

# Title หลัก
fig.suptitle("My First Chart", fontsize=24, fontweight='bold')

# ==========================
# 1. Scatter Plot
# ==========================
x = np.random.rand(100)
y = np.random.rand(100)

axs[0, 0].scatter(x, y, color='black', s=12)
axs[0, 0].set_title("Scatter Plot")
axs[0, 0].set_xlabel("X Axis")
axs[0, 0].set_ylabel("Y Axis")

# ==========================
# 2. Bubble Chart
# ==========================
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.randint(50, 500, 50)
colors = np.random.rand(50)

axs[0, 1].scatter(
    x,
    y,
    s=sizes,
    c=colors,
    alpha=0.6
)

axs[0, 1].set_title("Bubble Chart")
axs[0, 1].set_xlabel("X Axis")
axs[0, 1].set_ylabel("Y Axis")

# ==========================
# 3. Horizontal Bar Chart
# ==========================
categories = ['A', 'B', 'C']
values = [80, 50, 20]

axs[0, 2].barh(categories, values, color='tab:blue')
axs[0, 2].set_title("Horizontal Bar")
axs[0, 2].set_xlabel("Value")
axs[0, 2].set_ylabel("Category")

# ==========================
# 4. Line Graph
# ==========================
x = np.arange(10)
y = x

axs[1, 0].plot(x, y, color='green', linewidth=2)

axs[1, 0].axvline(4, color='gray')
axs[1, 0].axvline(6, color='gray')

axs[1, 0].set_title("Line Graph")
axs[1, 0].set_xlabel("X Axis")
axs[1, 0].set_ylabel("Y Axis")

# ==========================
# 5. Multi Line Graph
# ==========================
x = [1, 2, 3, 4, 5, 6]

y1 = [2, 4, 2, 5, 2, 6]
y2 = [4, 2, 5, 1, 4, 7]

axs[1, 1].plot(x, y1, label='Line 1')
axs[1, 1].plot(x, y2, label='Line 2')

axs[1, 1].set_title("Multi Line")
axs[1, 1].set_xlabel("X Axis")
axs[1, 1].set_ylabel("Y Axis")
axs[1, 1].legend()

# ==========================
# 6. Marker Line
# ==========================
x = [1, 2, 3, 4]
y = [2, 5, 1, 6]

axs[1, 2].plot(
    x,
    y,
    marker='o',
    markersize=8,
    linewidth=2
)

axs[1, 2].set_title("Marker Line")
axs[1, 2].set_xlabel("X Axis")
axs[1, 2].set_ylabel("Y Axis")

# ==========================
# 7. Histogram
# ==========================
data = np.random.normal(50, 10, 1000)

axs[2, 0].hist(
    data,
    bins=10,
    color='gray'
)

axs[2, 0].set_title("Histogram")
axs[2, 0].set_xlabel("Value")
axs[2, 0].set_ylabel("Frequency")

# ==========================
# 8. Pie Chart
# ==========================
sizes = [30, 25, 20, 25]
labels = ['A', 'B', 'C', 'D']

axs[2, 1].pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    textprops={'fontsize': 10}
)

axs[2, 1].set_title("Pie Chart")
axs[2, 1].set_xlabel("Category")
axs[2, 1].set_ylabel("Percent")

# ==========================
# 9. Pie Chart 2
# ==========================
sizes2 = [25, 35, 15, 25]
labels2 = ['Python', 'Java', 'C++', 'JS']

axs[2, 2].pie(
    sizes2,
    labels=labels2,
    autopct='%1.1f%%',
    textprops={'fontsize': 10}
)

axs[2, 2].set_title("Programming Languages")
axs[2, 2].set_xlabel("Language")
axs[2, 2].set_ylabel("Percent")

# ปรับระยะห่าง
plt.tight_layout(rect=[0, 0, 1, 0.95])

# แสดงผล
plt.show()