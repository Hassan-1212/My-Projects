import requests
import csv
header = ['Arabic' , 'English' , 'Math' , 'Science' , 'Social Studies', 'Total']
f = open(r'C:\Users\hassa\Desktop\Project\Data.csv', 'w') #enter your csv file path
writer = csv.writer(f)
writer.writerow(header)
for i in range(207412,207454):          #seat no. range
  x = requests.get('https://www.cairogovresults.com/api/results/Preparatory-Certificate?SeatNumber=' + str(i))
  json_x = x.json()
  if len(json_x['FinalResult']) != 0:
    if list(json_x['FinalResult'][1].values())[1] != 'غ':
      row = []
      for j in range(1,7):
        row.insert(j,list(json_x['FinalResult'][j].values())[1])
      print(row)
      writer.writerow(row)
#copyright Hassan Ayman
#in order to work properly download python 3.9.5 and requests library
