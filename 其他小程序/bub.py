
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
n_bubbles = 100  # 100个气泡
# 气泡数组
bubbles = np.zeros(n_bubbles, dtype=[
    ('position', float, 2),  # 位置(水平和垂直坐标)
    ('size', float, 1),      # 大小
    ('growth', float, 1),    # 生长速度
    ('color', float, 4)])    # 颜色(红、绿、蓝和透明度)
bubbles['position'] = np.random.uniform(
    0, 1, (n_bubbles, 2))
bubbles['size'] = np.random.uniform(
    50, 750, n_bubbles)
bubbles['growth'] = np.random.uniform(
    30, 150, n_bubbles)
bubbles['color'] = np.random.uniform(
    0, 1, (n_bubbles, 4))
mp.figure('Bubbles', facecolor='lightgray')
mp.title('Bubbles', fontsize=20)
mp.xticks(())
mp.yticks(())
sc = mp.scatter(
    bubbles['position'][:, 0],
    bubbles['position'][:, 1], s=bubbles['size'],
    c=bubbles['color'])


# 更新回调函数
def update(number):
    # 更新气泡的大小
    bubbles['size'] += bubbles['growth']
    # 确定哪个气泡破裂
    burst = number % n_bubbles
    # 更新破裂气泡的位置
    bubbles['position'][burst] = np.random.uniform(
        0, 1, 2)
    # 更新破裂气泡的大小
    bubbles['size'][burst] = 0
    # 更新破裂气泡的生长速度
    bubbles['growth'][burst] = np.random.uniform(
        30, 150)
    # 更新破裂气泡的颜色
    bubbles['color'][burst] = np.random.uniform(
        0, 1, 4)
    # 设置气泡的位置
    sc.set_offsets(bubbles['position'])
    # 设置气泡的大小
    sc.set_sizes(bubbles['size'])
    # 设置气泡的颜色
    sc.set_facecolors(bubbles['color'])


# 启动动画
anim = ma.FuncAnimation(
    mp.gcf(), update, interval=10)
mp.show()
