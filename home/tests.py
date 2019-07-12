from django.test import TestCase
from selenium import webdriver

import unittest


# Create your tests here.
class VisitMakerTestCase(TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_url_contains_home(self):
    self.browser.get('http://127.0.0.1:8000/home/')
    self.assertIn('home', self.browser.current_url)

if __name__ == '__main__':
  unittest.main(warnings = 'ignore')