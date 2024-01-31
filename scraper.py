from bs4 import BeautifulSoup
import requests

def get_citations_needed_count(url):
    # Get request to webpage(wikipedia)
    response = requests.get(url)
    
    # Changes the formatting of the response for beautiful soup
    url_content = response.content

    # Makes the soup sandwich pretty, and parses it
    beaut_soup = BeautifulSoup(url_content, "html.parser")

    # Finds all anchor tags
    a_soup = beaut_soup.find_all('a')

    # index for number of citations
    number_citations = 0

    # loop through each anchor tag and find all that have "citation needed as text. Increment index"
    for index in a_soup:
        if index.text == "citation needed":
            number_citations += 1

    # Return number of "citation needed"
    return print(number_citations)

def get_citations_needed_report(url):
    
    response = requests.get(url)

    url_content = response.content

    beaut_soup = BeautifulSoup(url_content, "html.parser")

    a_soup = beaut_soup.find_all('a')

    formatted_string = ''

    for index in a_soup:
        if index.text == "citation needed":
            formatted_string += index.parent.parent.parent.text + "\n\n"
    
    return print(formatted_string)

get_citations_needed_count("https://en.wikipedia.org/wiki/Charles_E._Sexey")
get_citations_needed_report("https://en.wikipedia.org/wiki/Charles_E._Sexey")