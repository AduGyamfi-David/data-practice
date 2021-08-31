import sys
import numpy as np
from pyicloud import PyiCloudService
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout, 
    QPushButton, 
    QVBoxLayout,
    QLabel,
    QWidget,
)
from utils import data
from utils import visualize

app = QApplication(sys.argv)
window = QWidget()

# template_label = QLabel()
# template_label.wordWrap()
# template_HBox = QHBoxLayout()
# template_HBox.addSpacing()
# template_HBox.addStretch()

def startup():
    window.setWindowTitle("Data Practice")

    window_objects = {
        "window_layout": QVBoxLayout(),

        "title_area": {
            "title_layout": QHBoxLayout(),
            "lblTitle": QLabel('<h1>Welcome to Data Practice</h1>')
        },

        "buttons_area": {
            "buttons_layout": QHBoxLayout(),
            "cmdLoadFromFile": QPushButton('Load data from file'),
            "cmdLoadFromiCloud": QPushButton('Load from iCloud')
        },
    }

    window.setStyleSheet(open(r"src\css\welcome.css").read())

    #_ get original size of window and label (with text) before data added
    original_window_dim = window.frameGeometry()
    original_label_size = window_objects["title_area"]["lblTitle"].sizeHint()

    #_ add label to container
    window_objects["title_area"]["title_layout"].addWidget(window_objects["title_area"]["lblTitle"])

    #_ add buttons to container
    window_objects["buttons_area"]["buttons_layout"].addWidget(window_objects["buttons_area"]["cmdLoadFromFile"])
    window_objects["buttons_area"]["buttons_layout"].addWidget(window_objects["buttons_area"]["cmdLoadFromiCloud"])

    #_ add label & buttons to window container, then set window container
    window_objects["window_layout"].addLayout(window_objects["title_area"]["title_layout"])
    window_objects["window_layout"].addLayout(window_objects["buttons_area"]["buttons_layout"])
    window.setLayout(window_objects["window_layout"])

    #_ restore orginial size of window & label
    window.setGeometry(original_window_dim)
    window_objects["title_area"]["lblTitle"].adjustSize()
    # window_objects["title_area"].addSpacing()
    window_objects["title_area"]["lblTitle"].setFixedSize(original_label_size)

def fetch_icloud():
    password_file = open((str(Path(__file__).parents[3]) + "\\password.txt"), "r")
    my_apple_id = password_file.readline()
    my_password = password_file.readline()

    print(my_apple_id + my_password)

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
# password_file = open((str(Path(__file__).parents[3]) + "\\password.txt"), "r")
# my_apple_id = password_file.readline()
# my_password = password_file.readline()
# print(my_apple_id + my_password)

# api = PyiCloudService(my_apple_id, password=my_password)
fetch_icloud()
# main()
# visualize.draw_graph(data.fetch_csv(), False)
# startup()
# window.show()
# sys.exit(app.exec_())