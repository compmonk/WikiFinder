import json

from core.text_churner import get_keywords
from core.web_scraper import scrape
from models.Index import Index
from models.OccurrenceList import OccurrenceList
from models.PatriciaTrie import Trie
from models.Site import Site
from settings import DATA_DIR


class WikiFinder:
    web = OccurrenceList()
    keywords = Trie

    def __init__(self, urls=None,
                 html_docs=DATA_DIR.child("urls.json"),
                 url_list=DATA_DIR.child("urls.lst"),
                 save_keywords=True):
        """
        The WikiFinder class handles the web and the
        inverted index file
        :param urls: List of urls or url as the database
        :param html_docs: File containing location of
        html docs of the sites to use as the database
        :param url_list: File containing the list of urls
        to use as the database
        :param save_keywords: boolean flag whether to
        save the inverted index file or not,
        default is True and saves the inverted index in
        data/keywords.json
        """
        if urls:
            self.urls = list(map(lambda x: Site(x), urls))
        elif html_docs.exists:
            self.urls = []
            sites = json.loads(open(html_docs).read())['sites']
            for site in sites:
                self.urls.append(Site(site['url'], site['html']))
        elif url_list.exists:
            self.urls = list(map(lambda x: Site(x), open(url_list).read().rstrip().split('\n')))
        else:
            self.urls = []

        self.populate_web()

        if save_keywords:
            with open(DATA_DIR.child("keywords.json"), "w") as keywords_file:
                keywords_file.write(self.keywords.to_json())

    def populate_web(self):
        """
        Populates the web and the inverted index keyword
        dictionary with the urls provided
        """
        for url in self.urls:
            page = scrape(url)
            keywords = get_keywords(page.text)
            index = len(self.web)
            self.web.append(Index(index, page.title, page.url, page.links_to))

            for word in keywords:
                value = OccurrenceList()
                value.append(index)
                self.keywords.add(word.lower(), value)

    def search(self, query):
        """
        Search results for a multi-word query
        :param query: The string query to search for
        :return: Ranked pages relevant to the query
        """
        query = get_keywords(query)
        pages = OccurrenceList()
        first = True
        for word in query:
            node = self.keywords.search(word.lower())
            if node and node.value:
                this_page_results = OccurrenceList()
                for page_index in node.value:
                    this_page_results = this_page_results.union(OccurrenceList([self.web[page_index]]))

                if first:
                    pages = this_page_results
                    first = False
                else:
                    pages = pages.intersect(this_page_results)

        return self.rank_page(pages)

    def rank_page(self, pages):
        """
        Rank the pages using the page rank algorithm
        :param pages: The pages to rank using the
        page ranking algorithm
        :return: List of pages ranked in order
        by the algorithm
        """
        return pages
