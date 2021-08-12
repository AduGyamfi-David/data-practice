import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from pyicloud import PyiCloudService
from pathlib import Path

from requests.models import Response

def fetch():
    password_file = open((str(Path(__file__).parents[2]) + "\\password.txt"), "r")
    # print(Path(__file__).parents[2])
    api = PyiCloudService(password_file.readline(), password=password_file.readline())

    if api.requires_2fa:
        two_fa_code = input("Enter the code you received of one of your approved devices: ")
        result = api.validate_2fa_code(two_fa_code)
        print("Validation result: " + str(result))

    # print(api.devices)

    # print(api.drive['Shortcuts'].dir())

    # print("\n")
    data_file = api.drive['Shortcuts']['data.txt']

    # print(data_file.open().content)

    icloud_file_data_str = str(data_file.open().content)

    # print(icloud_file_data)

    icloud_file_data_array = icloud_file_data_str.split("\\n")
    icloud_file_data_array[-1] = icloud_file_data_array[-1].split("'")[0]
    data = []

    # print(len(icloud_file_data))

    # with data_file.open() as icloud_file_response:
    #     with open(data_file.name, "rt") as icloud_file:
            

    for i in range(1, len(icloud_file_data_array)):
        print(icloud_file_data_array[i])
        data.append(float(icloud_file_data_array[i]))
    
    np_data = np.array(data)

    draw_graph(np_data, False)

    return 0

def main():

    data_file = open("data.csv")
    data = []
    for line in data_file:
        data = line.split(",")

    for i in range(0, len(data)):
        data[i] = float(data[i])

    np_data = np.array(data)

    today = date.today().strftime("%d-%m-%Y")
    # print(date.today().strftime("%d/%m/%Y"))

    # print(int((max(data) - min(data)) * 100))
    #? file_str = today + ".png" 
    #? print(file_str)

    draw_graph(np_data, False)

    # plt.hist(np_data, bins=int((max(data) - min(data)) * 100))
    # #* NUMBER OF BINS = RANGE OF FLOATS (then converted into integers), TO ENFORCE ONE VALUE PER BIN
    # #? plt.savefig(file_str, format="PNG")
    # plt.show()

    data_file.close()

def draw_graph(data, save_to_file):

    plt.hist(data, bins=int((max(data) - min(data)) * 100))

    if (save_to_file):
        plt.savefig(date.today().strftime("%d-%m-%Y") + ".png", format="PNG")

    plt.show()

fetch()
# main()