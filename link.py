import setup_path
from twill.commands import *
import string as s
from datetime import datetime
from twill.utils import Link

def getZipLink(my_link):
    reset_browser()
    browser.clear_cookies()
    datetime.now()
    browser.go(my_link)
    fv("1", "RelayState", "https://services10.ieee.org/idp/SSO.saml2")
    browser.submit()
    fv("1", "pf.username", "yourUser@mail.com")
    fv("1", "pf.pass", "yourPass")
    browser.submit('Sign in')
    browser.submit('Resume')
    browser.reload()
    my_link=browser.find_link("Drone_RCS_Measurement_Dataset.zip") 
    str(my_link)
    no_otherinfo=[s.replace("Link(text)='Drone_RCS_Mesaurement_Dataset.zip', url=", "") for s in my_link]
    return no_otherinfo[1]   
