from bs4 import BeautifulSoup
import re

from extractor.extractor import COM_Extractor

com = COM_Extractor("./data/COM(2021)552final.html")
com.extract()
  