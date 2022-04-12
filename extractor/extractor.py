from bs4 import BeautifulSoup
import re
import urllib
from requests_html import HTML
from requests_html import HTMLSession
import requests


# Extract clean COM Numbers  
# TODO: Implement logic (method) to get the search results for the COM Numbers
# TODO: Extract the right (most fitting) search result
# TODO: Extract link from the search result 

class COM_Extractor:

    def __init__(self, file):
        self.file = file

    def extract(self):

        """
            This method aims to extract all com numbers with the corresponding footnote,
            wich are not already implemented as a hyperlink
        """
        # Filter out COM numbers wich are already displayed as hyperlink

        html= open(self.file, "r")
        content = html.read()

        soup = BeautifulSoup(content, 'html.parser')
        footer = soup.find_all("dd")# extract the footer

        extracted_com= []
        for f in footer:

            if f.find_all("a", {"class": "externalRef"}):  # if a tag with class="externalRef" is already present, ignore it
                continue

            inner_text = f.getText() # get the content (text) from the footer
            com_findings = re.findall("(COM\s?\([0-9][0-9][0-9][0-9]\)\s?[0-9]*\s(?:final))|(COM\s?\([0-9][0-9][0-9][0-9]\)[0-9]*)", inner_text) #regex for extracting com numbers 

            for results in com_findings:
                for com in results:
                    if com != '':
                        if com in inner_text:   # check if com number is in the current innertext to extract the corresponding com number
                            footnote_att = f.attrs
                            com_dict = {footnote_att["id"]: com}
                            extracted_com.append(com_dict)

        print(extracted_com)

    def get_source(self, url):
        """Return the source code for the provided URL. 

        Args: 
            url (string): URL of the page to scrape.

        Returns:
            response (object): HTTP response object from requests_html. 
        """

        try:
            session = HTMLSession()
            response = session.get(url)
            return response

        except requests.exceptions.RequestException as e:
            print(e)


    def scrape_google(self, query):

        query = urllib.parse.quote_plus(query)
        response = self.get_source("https://www.google.co.uk/search?q=" + query)

        links = list(response.html.absolute_links)
        google_domains = ('https://www.google.', 
                        'https://google.', 
                        'https://webcache.googleusercontent.', 
                        'http://webcache.googleusercontent.', 
                        'https://policies.google.',
                        'https://support.google.',
                        'https://maps.google.')

        for url in links[:]:
            if url.startswith(google_domains):
                links.remove(url)

        eur_lex_url = "https://eur-lex.europa.eu/legal-content/"

        extracted_link = ""
        for url in links:
            if eur_lex_url in url:
                print(url)
                extracted_link = url

        print(extracted_link)