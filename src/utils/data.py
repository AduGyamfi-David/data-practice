import numpy as np
from pyicloud import PyiCloudService
from pathlib import Path
import numpy as np
from utils import visualize


def fetch_icloud():
    password_file = open((str(Path(__file__).parents[3]) + "\\password.txt"), "r")
    my_apple_id = password_file.readline()
    my_password = password_file.readline()

    my_apple_id = my_apple_id.split("\n")[0]

    # print("%r" % my_apple_id)
    # print("%r" % my_password)

    api = PyiCloudService(apple_id=my_apple_id, password=my_password)

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
    tdata = []
    ydata = []

    # print(len(icloud_file_data))

    # with data_file.open() as icloud_file_response: 
    #     with open(data_file.name, "rt") as icloud_file:
            

    for i in range(1, len(icloud_file_data_array)):
        item = icloud_file_data_array[i].split(";")
        if (item[1] == "t"):
            tdata.append(float(item[0]))
        else:
            ydata.append(float(item[0]))
        # print(icloud_file_data_array[i])
        # data.append(float(icloud_file_data_array[i]))
        
    
    np_tdata = np.array(tdata)

    visualize.draw_graph(np_tdata, False)

    np_ydata = np.array(ydata)

    visualize.draw_graph(np_ydata, False)
    # upload(np_data)
    return 0    

def fetch_csv():

	tdata_file = open(r"src/data/tdata.csv")
	ydata_file = open(r"src/data/ydata.csv")
	data = []

	t_data, y_data = split_data(tdata_file, ydata_file)

	np_tdata = np.array(t_data)
	np_ydata = np.array(y_data)
	np_data = np.append(np_tdata, np_ydata)

    #? file_str = today + ".png" 
    #? print(file_str)

    # plt.hist(np_data, bins=int((max(data) - min(data)) * 100))
    # #* NUMBER OF BINS = RANGE OF FLOATS (then converted into integers), TO ENFORCE ONE VALUE PER BIN
    # #? plt.savefig(file_str, format="PNG")
    # plt.show()

	tdata_file.close()
	ydata_file.close()

	return np_data

def split_data(tdf, ydf):

	for line in tdf:
		td = line.split(",")
	
	for i in range(0,len(td)):
		td[i] = float(td[i]) - 30

	for line in ydf:
		yd = line.split(",")
	
	for i in range(0, len(yd)):
		yd[i] = float(yd[i])

	return (td, yd)

def upload(tdata, ydata):

    tdata_file = open("src/data/tdata.csv", "a")
    ydata_file = open("src/data/ydata.csv", "a")
    out_str = ","

    for i in range(0, len(tdata)):
        out_str += (str(tdata[i]) + ",") if (i != len(tdata) - 1) else (str(tdata[i]))

    tdata_file.write(out_str)
	
    out_str = ","

    for i in range(0, len(ydata)):
        out_str += (str(ydata[i]) + ",") if (i != len(ydata) - 1) else (str(ydata[i]))

    ydata_file.write(out_str)

    tdata_file.close()
    ydata_file.close()