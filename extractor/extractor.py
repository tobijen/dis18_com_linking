from bs4 import BeautifulSoup
import re

class COM_Extractor:

    def __init__(self, file):
        self.file = file

    def extract(self):
        html= open(self.file, "r")
        content = html.read()

        soup = BeautifulSoup(content, 'html.parser')
        footer = soup.find_all("dd")# extract the footer

        raw_footer_text = []

        for f in footer:
            inner_text = f.getText() # get the content (text) from the footer

            x = re.findall("(COM\([0-9][0-9][0-9][0-9]\)[0-9]*\s(?:final))|(COM\([0-9][0-9][0-9][0-9]\)[0-9]*)", inner_text) #regex for extracting com numbers 

            #x = re.match(regex, inner_text)

            print(x)
