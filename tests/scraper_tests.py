from unittest import TestCase

from core.web_scraper import scrape

from models.Site import Site


class ScraperTests(TestCase):
    def test_1_scrape_with_url(self):
        # Arrange
        url = "https://en.wikipedia.org/wiki/New_York"
        site = Site(url)
        title = "New York - Wikipedia"

        # Act
        page = scrape(site)

        # Assert
        self.assertEqual(title, page.title, "Title is not set correctly")
        self.assertEqual(url, page.url, "URL is not set correctly")
        self.assertNotEqual("", page.text, "No text returned")
        print(len(page.links_to))

    def test_2_scrape_with_html_doc(self):
        # Arrange
        url = "https://en.wikipedia.org/wiki/New_York_City"
        site = Site(url, "New York City - Wikipedia.html")
        title = "New York City - Wikipedia"

        # Act
        page = scrape(site)

        # Assert
        self.assertEqual(title, page.title, "Title is not set correctly")
        self.assertEqual(url, page.url, "URL is not set correctly")
        self.assertNotEqual("", page.text, "No text returned")
        print(len(page.links_to))
