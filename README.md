# Results-Analyzer-of-university

This web scraper will fetch the results of students of all departements and creates a bar graph representing the passed,promoted and detained persnetage of students of all departments . This scraper will work on any result page uploaded on Osmania University's official site. - "https://www.osmania.ac.in"


## Getting Started

Clone the repository to your local machine  
Extract all the files into a directory  
Run the **Results Analyzer.py**  


### Prerequisites

Dependencies:
1. BeautifulSoup
2. pandas
3. matplotlib

```
from bs4 import BeautifulSoup
import pandas as pd
import requests
from matplotlib import pyplot as plt
```

### Installing

Installing our dependencies :

BeautifulSoup

```
$ apt-get install python-bs4 (for Python 2)
$ apt-get install python3-bs4 (for Python 3)
$ easy_install beautifulsoup4
$ pip install beautifulsoup4
(these may be named pip3 and easy_install3 respectively if you’re using Python 3)

If you don’t have easy_install or pip installed, you can download the Beautiful Soup 4 source tarball and install it with setup.py.
$ python setup.py install
```

Pandas

```
$ pip install pandas
$ pip3 install pandas (For python3, use pip for windows here as well)
```

Matplotlib

```
$ pip install matplotlib

If you are on Linux, you might prefer to use your package manager. Matplotlib is packaged for almost every major Linux distribution.

    Debian / Ubuntu: sudo apt-get install python3-matplotlib
    Fedora: sudo dnf install python3-matplotlib
    Red Hat: sudo yum install python3-matplotlib
    Arch: sudo pacman -S python-matplotlib

```
Example Graph Created : 
https://github.com/syedibrahimhussain/Results-Analyzer-of-university/blob/master/Figure_1.png

## Deployment

Run the  	**result_Analyzer.py**


## Built With

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Used for pulling data from HTML page
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/) - Dataframes used
* [Matplotlib](https://matplotlib.org/) - Used for data visualization


## Authors

**SYED IBRAHIM HUSSAIN** - 

## Acknowledgments

* StackOverflow
* https://github.com/AbdulAhadSiddiqui11/Web-Scraper-OU-Results
 
#Reference

* * https://github.com/AbdulAhadSiddiqui11/Web-Scraper-OU-Results
