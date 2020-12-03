import requests
from bs4 import BeautifulSoup

URL ='https://en.wikipedia.org/wiki/Haus_Steineck'

def get_citations_needed_count(URL):
    response = requests.get(URL)
    information = response.content
    bs = BeautifulSoup(information, 'html.parser')
    find_int = bs.find_all('a', href='/wiki/Wikipedia:Citation_needed')
    # print(bs)
    print(len(find_int))

def get_citations_needed_report(URL):
    response = get_citations_needed_count(URL)
    citations = []
    for citation in citations:
        citation = citation.parent.text.strip()
        citations.append(citation)
    string = ""
    for n in citations:
        string += n + "\n"
    print(string)
    return(string)





get_citations_needed_count(URL)
get_citations_needed_report(URL)