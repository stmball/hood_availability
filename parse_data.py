import json
import re
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors


def get_squares():
    with open("./output.json") as f:
        data = json.load(f)

    squares = np.array([True for _ in range(6)])

    for booking in data:
        start = datetime.strptime(booking["start"], "%Y-%m-%dT%H:%M:%SZ")
        end = datetime.strptime(booking["end"], "%Y-%m-%dT%H:%M:%SZ")
        if start < datetime.now() < end:
            hood = re.findall(r"Hood \d", booking["title"])
            if hood:
                hood_index = int(hood[0][-1]) - 1
                squares[hood_index] = False

    return squares
