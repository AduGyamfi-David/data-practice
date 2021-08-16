import numpy as np
from pyicloud import PyiCloudService
from pathlib import Path
import numpy as np
from utils import visualize


def fetch_icloud():
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
        # print(icloud_file_data_array[i])
        data.append(float(icloud_file_data_array[i]))
    
    np_data = np.array(data)

    visualize.draw_graph(np_data, False)
    # upload(np_data)

    return 0

def fetch_csv():

	data_file = open(r"src/data/data.csv")
	data = []


	for line in data_file:
		data = line.split(",")

	for i in range(0, len(data)):
		data[i] = float(data[i])
		
	np_data = np.array(data)

    # print(date.today().strftime("%d/%m/%Y"))

    # print(int((max(data) - min(data)) * 100))
    #? file_str = today + ".png" 
    #? print(file_str)

    # plt.hist(np_data, bins=int((max(data) - min(data)) * 100))
    # #* NUMBER OF BINS = RANGE OF FLOATS (then converted into integers), TO ENFORCE ONE VALUE PER BIN
    # #? plt.savefig(file_str, format="PNG")
    # plt.show()

	data_file.close()

	return np_data

def upload(data):

    data_file = open("data.csv", "a")
    out_str = ","

    for i in range(0, len(data)):
        out_str += (str(data[i]) + ",") if (i != len(data) - 1) else (str(data[i]))

    # print(out_str)
    data_file.write(out_str)
    data_file.close()