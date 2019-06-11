#coding: utf-8 
from __future__ import unicode_literals
from behave import *
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *
import logging
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
#from environment import *
from selenium.webdriver.common.action_chains import ActionChains
import random
import string
import getpass

def before_all(context):
    selenium_logger = logging.getLogger(
        'selenium.webdriver.remote.remote_connection')
    selenium_logger.setLevel(logging.WARN)
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(3)
    context.driver.native_events_enabled = True 
    

def after_all(context):
    context.driver.quit()
    
def find(context, meth, val):
    sleep(1)
    WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located(
            ( meth, val)
            ))
    return context.driver.find_element(meth, val)

# def enter_insta(context):
    
landing_url="https://lushli.com/theinkeylist/"

    
    
    
    