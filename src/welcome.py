import sys
from typing import MutableMapping
import numpy as np
from numpy.lib import twodim_base
from pyicloud import PyiCloudService
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout, 
    QPushButton, 
    QVBoxLayout,
    QLabel,
    QWidget,
)
from utils import data
from utils import visualize

app = QApplication(sys.argv)
welcome_window = QWidget()
icloud_window = QWidget()
csv_window = QWidget()

def main():
    startup()

    welcome_window.show()

    sys.exit(app.exec_())

def startup():
    welcome_window.setWindowTitle("Data Practice")

    window_objects = {
        "window_layout": QVBoxLayout(),

        "title_area": {
            "label_frame": QFrame(welcome_window),
            "title_layout": QHBoxLayout(),
            "lblTitle": QLabel('<h1>Welcome to Data Practice</h1>')
        },

        "buttons_area": {
            "buttons_layout": QHBoxLayout(),
            "cmdLoadFromFile": QPushButton('Load data from file'),
            "cmdLoadFromiCloud": QPushButton('Load from iCloud')
        },
    }
    
    welcome_window.setStyleSheet(open(r"src\css\welcome.css").read())

    #_ get original size of window before objects added
    original_window_dim = welcome_window.frameGeometry()

    #_ add label to container
    window_objects["title_area"]["title_layout"].addWidget(window_objects["title_area"]["lblTitle"])
    window_objects["title_area"]["label_frame"].setLayout(window_objects["title_area"]["title_layout"])
    window_objects["title_area"]["label_frame"].adjustSize()

    #_ add buttons to container
    window_objects["buttons_area"]["buttons_layout"].addWidget(window_objects["buttons_area"]["cmdLoadFromFile"])
    window_objects["buttons_area"]["buttons_layout"].addWidget(window_objects["buttons_area"]["cmdLoadFromiCloud"])

    #_ add label & buttons to window container, then set window container
    window_objects["window_layout"].addLayout(window_objects["title_area"]["title_layout"])
    window_objects["window_layout"].addLayout(window_objects["buttons_area"]["buttons_layout"])
    welcome_window.setLayout(window_objects["window_layout"])

    #_ restore orginial size of window & label
    welcome_window.setGeometry(original_window_dim)

    #_ add events to buttons
    window_objects["buttons_area"]["cmdLoadFromiCloud"].clicked.connect(loadiCloudWindow)

def loadiCloudWindow():
    welcome_window.close()

    icloud_window.setWindowTitle("Fetch from iCloud")

    window_objects = {
        "window_layout": QVBoxLayout(),

        "heading": {   
            "container": QFrame(icloud_window),
            "layout": QHBoxLayout(),
            "label": QLabel('<h1>Loading From iCloud...</h1>')
        },

        "icloud_data": {
            "container": QFrame(icloud_window),
            "layout": QHBoxLayout(),

            "header_container": QFrame(),
            "header_layout": QVBoxLayout(),

            "info_container": QFrame(),
            "info_layout": QVBoxLayout(),

            "headers": [
                QLabel('<h3>Total number of data items: </h3>'), 
                QLabel('<h4>From Dataset 1: </h4>'), 
                QLabel('<h4>From Dataset 2: </h4>')
            ],

            "info": [
                QLabel(),
                QLabel(),
                QLabel()
            ]
        },

        "data_actions": {
            "container": QFrame(icloud_window),
            "layout": QHBoxLayout(),
            "cmdAddToCSVs": QPushButton("Add iCloud data to CSV files"),
            "cmdVisualise": QPushButton("Visualise Data from iCloud")
        }
    }

    
    #_ call stylesheet for window
    icloud_window.setStyleSheet(open(r"src\css\icloud.css").read())

    #_ edit window
    original_window_dim = icloud_window.frameGeometry()

    #_ edit loading header
    window_objects["heading"]["layout"].addWidget(window_objects["heading"]["label"])
    window_objects["heading"]["container"].setLayout(window_objects["heading"]["layout"])
    window_objects["heading"]["container"].adjustSize()
    
    #_ edit headers for loaded data
    for label in window_objects["icloud_data"]["headers"]:
        window_objects["icloud_data"]["header_layout"].addWidget(label)
    window_objects["icloud_data"]["header_container"].setLayout(window_objects["icloud_data"]["header_layout"])
    window_objects["icloud_data"]["header_container"].adjustSize()

    #_ edit info from loaded data
    for label in window_objects["icloud_data"]["info"]:
        label.setText('<h5>TEMP</h5>')
        window_objects["icloud_data"]["info_layout"].addWidget(label)
    window_objects["icloud_data"]["info_container"].setLayout(window_objects["icloud_data"]["info_layout"])
    window_objects["icloud_data"]["info_container"].adjustSize()

    #_ edit frame for all data from iCloud
    window_objects["icloud_data"]["layout"].addWidget(window_objects["icloud_data"]["header_container"])
    window_objects["icloud_data"]["layout"].addWidget(window_objects["icloud_data"]["info_container"])
    window_objects["icloud_data"]["container"].setLayout(window_objects["icloud_data"]["layout"])
    window_objects["icloud_data"]["container"].adjustSize()

    #_ edit action controls for data
    window_objects["data_actions"]["layout"].addWidget(window_objects["data_actions"]["cmdAddToCSVs"])
    window_objects["data_actions"]["layout"].addWidget(window_objects["data_actions"]["cmdVisualise"])
    window_objects["data_actions"]["container"].setLayout(window_objects["data_actions"]["layout"])
    window_objects["data_actions"]["container"].adjustSize()

    #_ add all to window
    window_objects["window_layout"].addWidget(window_objects["heading"]["container"])
    window_objects["window_layout"].addWidget(window_objects["icloud_data"]["container"])
    window_objects["window_layout"].addWidget(window_objects["data_actions"]["container"])
    icloud_window.setLayout(window_objects["window_layout"])
    icloud_window.setGeometry(original_window_dim)

    icloud_window.show()
    return 0

def loadCSVWindow():

    return 0

main()