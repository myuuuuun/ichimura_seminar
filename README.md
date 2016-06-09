# 市村ゼミ 2016年度

## 稲垣数理統計

### 11章
* [Notebook](http://nbviewer.jupyter.org/github/myuuuuun/ichimura_seminar/blob/master/inagaki/inagaki_ch11.ipynb)
* Data csv
    * [11_1.csv](/inagaki/inagaki_ch11_1.csv)
    * [11_5.csv](/inagaki/inagaki_ch11_5.csv)
    * [11_8_south.csv](/inagaki/inagaki_ch11_8_south.csv), [11_8_north.csv](/inagaki/inagaki_ch11_8_north.csv)

### How to import csv

Pythonの場合:

```python
import numpy as np
import csv

data = np.loadtxt("inagaki_ch11_1.csv", delimiter=",", skiprows=1)
print(data)
```