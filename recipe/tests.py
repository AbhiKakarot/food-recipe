from django.test import TestCase

# Create your tests here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'/gecko')
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AccountTestCase(LiveServerTestCase):
  def test_login(self):
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:8000/user/login/')