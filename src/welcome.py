import sys
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

# fetch()
# main()
# visualize.draw_graph(data.fetch_csv(), False)
startup()
window.show()
sys.exit(app.exec_())