import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk(50000)
rw.fill_walk()
# 设置绘图窗口尺寸
plt.figure(dpi=128, figsize=(10, 6))

point_numbers = list(range(rw.num_points))

plt.scatter(
    rw.x_values,
    rw.y_values,
    c=point_numbers,
    cmap=plt.cm.Blues,
    edgecolors='none',
    s=15,
)

# 突出起点和终点
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1],
            rw.y_values[-1],
            c='red',
            edgecolors='none',
            s=100)

# 隐藏坐标轴
ax = plt.gca()
# 隐藏坐标轴的边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
# 隐藏刻度轴
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

plt.show()
