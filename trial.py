import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('data.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(float(row[4]))
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Stock Data")
  
plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Closing Value')
plt.title('Stock', fontsize = 20)
plt.grid()
plt.legend()
plt.show()