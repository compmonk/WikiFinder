from urllib.request import urlopen

from bs4 import BeautifulSoup, Comment

from models.Page import Page
from models.OccurrenceList import OccurrenceList
from settings import HTML_DIR


def scrape(site, prefix="https://en.wikipedia.org"):
    """
    Scrape a webpage by url or html
    :param site: Site object which specifies the url
    or the html document of the website
    :param prefix: prefix url to prefix to links
    found in the webpage, default is "https://en.wikipedia.org"
    :return: A Page object containing title, url, text and
    links_to from the web page scraped
    """
    if site.html_doc:
        with open(HTML_DIR.child(site.html_doc)) as html:
            page = BeautifulSoup(html, 'html.parser')
    else:
        page = BeautifulSoup(urlopen(site.url), 'html.parser')

    links_to = OccurrenceList()
    for link in page.find_all('a'):
        if link.get('href'):
            url_link = link.get('href')
            if not url_link.startswith("http"):
                url_link = prefix + url_link
            links_to = links_to.union(OccurrenceList([url_link]))

    """
    Remove script tags
    """
    for script in page("script"):
        page.script.extract()

    """
    Remove style tags
    """
    for style in page("style"):
        page.style.extract()

    """
    Remove comments
    """
    comments = page.findAll(text=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    return Page(page.title.string, site.url, page.text, links_to)
