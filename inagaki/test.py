#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import csv


if __name__ == "__main__":
    data = np.loadtxt("inagaki_ch11_8_north.csv", delimiter=",", skiprows=1)
    print(data)
