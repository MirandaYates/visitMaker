from django.test import TestCase
from selenium import webdriver
import unittest


# Create your tests here.
class VisitMakerTestCase(TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  # tests homepage
  def test_home_page_url(self):
    self.browser.get('http://127.0.0.1:8000/home/')
    self.assertIn('home', self.browser.current_url)

  # clicks "Reservations" link
  def test_reservations_link(self):
    self.browser.get('http://127.0.0.1:8000/home/')
    self.browser.find_element_by_link_text('Reservations').click()
    self.assertIn('reservHome', self.browser.current_url)

  def test_home_link(self):
    self.browser.get('http://127.0.0.1:8000/reservHome/addReserv')
    self.browser.find_element_by_link_text('Home').click()
    self.assertIn('home', self.browser.current_url)

  # fills out and submits reservation form
  def test_submit_add_reservation_form(self):
    self.browser.get('http://127.0.0.1:8000/reservHome/addReserv')
    self.browser.find_element_by_id('id_name').send_keys('John Johnson')
    self.browser.find_element_by_id('id_email').send_keys('jaspertomanyih@gmail.com')
    self.browser.find_element_by_id('id_people_number').send_keys('21')
    self.browser.find_element_by_id('id_tour_time').send_keys('12')
    self.browser.find_element_by_id('id_tour_date').send_keys('6/22/1997')
    self.browser.find_element_by_id('id_Special_Accomidations').send_keys('I\'m allergic to art.')
    self.browser.find_element_by_name('submit').click()
    self.assertIn('confirmReserv', self.browser.current_url)

if __name__ == '__main__':
  unittest.main(warnings = 'ignore')