import csv, matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

file = 'hukuo_day_20210910163112.csv'
with open(file, encoding='utf-8-sig') as f:
	csvfile = csv.reader(f)
	header = next(csvfile)
#print(header)
	dates, highs, lows = [], [], []  #設置日期,高溫,低溫串列
	for row in csvfile:
		
		try:                         #例外處理
			current_date = datetime.strptime(row[1], '%Y-%m-%d').date()
			high = float(row[3])
			low = float(row[4])
		except Exception:
			print(f"缺少{current_date}的資料")
		else:
			highs.append(high)
			lows.append(low)
			dates.append(current_date)

#繪製圖表
plt.style.use('seaborn')
fig, ax = plt.subplots()
x = np.arange(len(dates))
width = 0.3
ax.bar(x, highs, width, color='red', label='high')
ax.bar(x + width, lows, width, color='blue', label='lows')
plt.xticks(x+width/2 , dates)
fig.autofmt_xdate()
plt.ylabel("溫度 (C)", fontsize=16, fontproperties="Taipei Sans TC Beta")
plt.title("湖口鄉2021年8月每日氣溫圖", fontsize=24,
	fontproperties="Taipei Sans TC Beta")
plt.legend(bbox_to_anchor=(1,1), loc='upper left')
plt.show()
