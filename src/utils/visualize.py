import matplotlib.pyplot as plt
from datetime import date


def draw_graph(data, save_to_file):

    plt.hist(data, bins=int((max(data) - min(data)) * 100))

    if (save_to_file):
        plt.savefig(date.today().strftime("%d-%m-%Y") + ".png", format="PNG")

    plt.show()
