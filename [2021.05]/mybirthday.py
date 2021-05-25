import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r',encoding='cp949')
data = csv.reader(f, delimiter=',')
next(data)

high=[]
low=[]

for row in data:
    if row[-1]!='' and row[-2] != '':
        if int(row[0].split('-')[0]) >= 1980:
            if row[0].split('-')[1] == '03' and row[0].split('-')[2] == '25':
                high.append(float(row[-1]))
                low.append(float(row[-2]))
                
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title("생일의 기온 변화 그래프")

plt.plot(high, 'r', label="high")
plt.plot(low, 'b', label="low")
plt.legend()

plt.show()

f.close()
