import numpy as np
import matplotlib.pyplot as plt
from datetime import date

data_file = open("data.csv")
data = []
for line in data_file:
    data = line.split(",")

for i in range(0, len(data)):
    data[i] = float(data[i])

today = date.today().strftime("%d-%m-%Y")
# print(date.today().strftime("%d/%m/%Y"))

# print(int((max(data) - min(data)) * 100))
#? file_str = today + ".png" 
#? print(file_str)

plt.hist(data, bins=int((max(data) - min(data)) * 100))
#* NUMBER OF BINS = RANGE OF FLOATS, TO ENFORCE ONE VALUE PER BIN
#? plt.savefig(file_str, format="PNG")
plt.show()

data_file.close()