from typing import Final
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

counted_locations = []
Final_case_dic = {}
Final_date = []
Final_total = []
Final_date_total = {}
listof_cases = []
Covid_info = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
for i in Covid_info["location"]:
    if i not in counted_locations:
        counted_locations.append(i)

for i in range(len(counted_locations)):
    Final_case_dic[i] = Covid_info[Covid_info["location"] == counted_locations[i]]


for i in Final_case_dic.values():
    Final_date.append(i["date"])
    Final_total.append(i["total_cases"])

for i in range(len(counted_locations)):
    Final_date_total[counted_locations[i]] = [Final_date[i],Final_total[i]]

print("Here are the available countries:\n")
for i in range(len(counted_locations)):
    print(counted_locations[i])
while True:
    ask_location = input("What country do you want to know about: ")
    if ask_location in counted_locations:
        break
print(Final_date_total[ask_location])
fig= plt.figure(figsize=(10,10))
if max(Final_date_total[ask_location][1]) < 70000:
    listof_cases = np.arange(0,max(Final_date_total[ask_location][1]),3000)
elif max(Final_date_total[ask_location][1]) < 300000:
    listof_cases = np.arange(0,max(Final_date_total[ask_location][1]),7500)
elif max(Final_date_total[ask_location][1]) < 3000000:
    listof_cases = np.arange(0,max(Final_date_total[ask_location][1]),75000)
elif max(Final_date_total[ask_location][1]) < 30000000:
    listof_cases = np.arange(0,max(Final_date_total[ask_location][1]),750000)
elif max(Final_date_total[ask_location][1]) < 50000000:
    listof_cases = np.arange(0,max(Final_date_total[ask_location][1]),7500000)

listof_dates = np.arange(0,len(Final_date_total[ask_location][0]),75)
plt.yticks(listof_cases)
plt.xticks(listof_dates, rotation = "vertical")
plt.plot(Final_date_total[ask_location][0], Final_date_total[ask_location][1])
plt.text(Final_date_total[ask_location][0].tail(1),max(Final_date_total[ask_location][1]), max(Final_date_total[ask_location][1]))
plt.text(Final_date_total[ask_location][0].head(1),min(Final_date_total[ask_location][1]), min(Final_date_total[ask_location][1]))
plt.title("Covid cases from 2020 to 2021")
plt.xlabel("Dates(Intervals of 75)")
plt.ylabel("Total Cases")
plt.show()

