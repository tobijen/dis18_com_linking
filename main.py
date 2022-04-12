from bs4 import BeautifulSoup
import re

# TODO: Extract clean COM Numbers
# TODO: Implement logic (method) to get the search results for the COM Numbers
# TODO: Extract the right (most fitting) search result
# TODO: Extract link from the search result 

from extractor.extractor import COM_Extractor

com = COM_Extractor("./data/COM(2021)552final.html")
com.extract()
  