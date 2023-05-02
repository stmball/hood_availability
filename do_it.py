import json
import re
import typing as tp
from dataclasses import dataclass
from datetime import datetime, timedelta
from getpass import getpass

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
import twill.commands as t
from matplotlib import colors
from matplotlib.animation import FuncAnimation
from twill import browser


@dataclass
class Booking:
    user: str
    item: str
    start_time: datetime
    end_time: datetime
    available: bool = True


class Hood_Availability:
    def __init__(self):
        self.username = input("Enter username:")
        self.password = getpass("Enter password:")
        self.raw_data = self.get_data()
        self.data = self.parse_data()
        self.squares, self.bookers = self.get_squares()
        self.labels = []
        self.fig, self.ax = plt.subplots()

        cmap = colors.ListedColormap(["red", "green"])
        bounds = [0, 0.5, 1]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        for i in range(8):
            t = self.ax.text(
                i % 4, i // 4, f"Hood {i + 1}", ha="center", va="center", color="white"
            )
            self.labels.append(t)

        self.ax.set_xticks([])
        self.ax.set_yticks([])

        [
            self.ax.spines[a].set_visible(False)
            for a in ["top", "bottom", "left", "right"]
        ]

        self.im = self.ax.imshow(self.squares.reshape((2, 4)), cmap=cmap, norm=norm)

    def get_data(self) -> str:
        login = "https://safetynet.liverpool.ac.uk/login/"

        t.go(login)
        t.form_clear("1")
        t.formvalue("1", "username", self.username)
        t.formvalue("1", "password", self.password)
        t.submit("1")

        start_date = datetime.now().strftime("%Y-%m-%d")
        end_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

        t.go(
            f"https://safetynet.liverpool.ac.uk/equipment/booking/api/list/?limit_to=&start={start_date}&end={end_date}"
        )

        a = browser.html
        return a

    def parse_data(self) -> tp.List[Booking]:
        data = json.loads(self.raw_data)

        data = [
            Booking(
                user=re.findall(r"(?<=\d{2}:\d{2}: )[\w ]+", booking["title"])[0][:-1],
                item=re.findall(r"\(.*\)$", booking["title"])[0][1:-1],
                start_time=datetime.strptime(booking["start"], "%Y-%m-%dT%H:%M:%SZ"),
                end_time=datetime.strptime(booking["end"], "%Y-%m-%dT%H:%M:%SZ"),
            )
            for booking in data
        ]

        for booking in data:
            if booking.start_time < datetime.now() < booking.end_time:
                booking.available = False

        return data

    def update(self, frame: int) -> None:
        if datetime.now().minute % 5 == 0 and datetime.now().second == 0:
            print("Getting data")
            self.raw_data = self.get_data()

        self.data = self.parse_data()

        squares, bookers = self.get_squares()

        self.im.set_data(squares.reshape((2, 4)))
        self.ax.set_title("Hood Availability as of " + str(datetime.now())[:-7])

        for idx, booker in enumerate(bookers):
            if booker:
                start_time = booker.start_time.strftime("%H:%M")
                end_time = booker.end_time.strftime("%H:%M")
                self.labels[idx].set_text(
                    f"Hood {idx+1}\n{booker.user}\n{start_time}-{end_time}",
                )

    def get_squares(self) -> tp.Tuple[npt.NDArray[np.bool_], tp.List[Booking]]:
        squares = [True for _ in range(8)]
        bookers = [None for _ in range(8)]
        for booking in self.data:
            if not booking.available:
                # Find the hood number
                hood_no = re.findall(r"(?<=Hood )\d", booking.item)
                if hood_no:
                    index = int(hood_no[0]) - 1
                    squares[index] = False
                    bookers[index] = booking

        return np.array(squares), bookers

    def start_plot(self):
        animation = FuncAnimation(self.fig, self.update, interval=1000)

        plt.tight_layout()
        plt.show()
        plt.pause(0.01)


if __name__ == "__main__":
    hood = Hood_Availability()
    hood.start_plot()
