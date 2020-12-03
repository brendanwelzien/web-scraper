from scraper import get_citations_needed_count, get_citations_needed_report

def test_citation_count():
    URL ='https://en.wikipedia.org/wiki/Haus_Steineck'
    actual = get_citations_needed_count(URL)
    expected = 1
    assert actual == expected