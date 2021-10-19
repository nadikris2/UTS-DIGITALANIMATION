import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_excel('fileuts.xlsx')
x= df['daerah']
y= df['jumlah']

#plot 1 
#bar chart
plt.xlabel('daerah',fontsize=3)
plt.ylabel('jumlah',fontsize=3)
plt.subplot(1, 3, 1)
plt.bar(x,y)

#plot 2 
#line Graph
plt.xlabel('daerah',fontsize=18)
plt.ylabel('jumlah',fontsize=18)
plt.subplot(1, 3, 2)
plt.scatter(x,y)
plt.plot(x,y)

#plot 3 
#pie chart
plt.subplot(1, 3, 3)
explode = (0, 0.05, 0.03, 0, 0, 0.01)
plt.pie(y, labels=x, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)


plt.suptitle('Data Penjulan Alat Berat Dalam Unit di Bulan Oktober 2021')
plt.show()