from datetime import datetime
from getpass import getpass
from time import sleep

import matplotlib.pyplot as plt
from matplotlib import colors

from get_data import get_data
from parse_data import get_squares

print("Please enter your login details to Safteynet/MWS - this will not be stored!")
username = input("Enter username:")
password = getpass("Enter password:")

while True:
    get_data(username=username, password=password)

    plt.close("all")
    fig, ax = plt.subplots()
    # create discrete colormap
    cmap = colors.ListedColormap(["red", "green"])
    bounds = [0, 0.5, 1]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    ax.text(0, 0, "Hood 1", ha="center", va="center", color="white")
    ax.text(1, 0, "Hood 2", ha="center", va="center", color="white")
    ax.text(2, 0, "Hood 3", ha="center", va="center", color="white")
    ax.text(0, 1, "Hood 4", ha="center", va="center", color="white")
    ax.text(1, 1, "Hood 5", ha="center", va="center", color="white")
    ax.text(2, 1, "Hood 6", ha="center", va="center", color="white")

    ax.set_xticks([])
    ax.set_yticks([])

    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)

    squares = get_squares()
    ax.imshow(squares.reshape((2, 3)), cmap=cmap, norm=norm)
    ax.set_title("Hood Availability as of " + str(datetime.now())[:-7])

    plt.savefig("hood_availability.png")

    sleep(10)
