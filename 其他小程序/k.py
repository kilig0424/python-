# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    print(dmy)
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    print(date)
    ymd = date.strftime('%Y-%m-%d')
    print(ymd)
    return ymd


dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
        'aapl.csv',
        delimiter=',', usecols=(1, 3, 4, 5, 6),
        unpack=True, dtype='M8[D], f8, f8, f8, f8',
        converters={1: dmy2ymd})
mp.figure('Candlestick', facecolor='lightgray')
mp.title('Candlestick', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
ax = mp.gca()
# 设置水平坐标每个星期一为主刻度
ax.xaxis.set_major_locator(md.WeekdayLocator(
    byweekday=md.MO))
# 设置水平坐标每一天为次刻度
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置水平坐标主刻度标签格式
ax.xaxis.set_major_formatter(md.DateFormatter(
    '%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
# 阳线掩码
rise = closing_prices - opening_prices >= 0.01
# 阴线掩码
fall = opening_prices - closing_prices >= 0.01
# 填充色
fc = np.zeros(dates.size, dtype='3f4')
fc[rise], fc[fall] = (1, 1, 1), (0, 0.5, 0)
# 边缘色
ec = np.zeros(dates.size, dtype='3f4')
ec[rise], ec[fall] = (1, 0, 0), (0, 0.5, 0)
mp.bar(dates, highest_prices - lowest_prices, 0,
       lowest_prices, color=fc, edgecolor=ec)
mp.bar(dates, closing_prices - opening_prices, 0.8,
       opening_prices, color=fc, edgecolor=ec)
# 自动调整水平坐标轴的日期标签
mp.gcf().autofmt_xdate()
mp.show()
