import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('../kaggle_source_dataset/India_Menu.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=';')
    for row in lines:
        x.append(row[1])
        y.append(int(row[3]))
        
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Total Calory Per Menu")
  
plt.xticks(rotation = 25)
plt.xlabel('Menu')
plt.ylabel('Energy (Cal)')
plt.title('Report Calory Per Menu', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
