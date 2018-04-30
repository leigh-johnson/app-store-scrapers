from test_plus.test import TestCase
from ..celery import appium_scrape_trending_keywords


class TestAppiumScrapers(TestCase):

    def test_appium_scrape_trending_keywords(self):
        keywords = appium_scrape_trending_keywords()
        self.assertEqual(len(keyworkds), 5)