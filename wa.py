import sys, random, time, os, platform, datetime, json
from selenium import webdriver
from random import randint
import datetime as d

systeminforma = sys.platform

print("\n\n\n\n\n\n\n\n\n\n\n")
print("  ===========================================================================\n")
print("                                  weighted average")
print("  ===========================================================================")
print("\n\n\n\n\n\n\n\n\n\n\n")

try: gmail = sys.argv[1]
except IndexError:
                print(" [!] Your account file is written improperly! (Check your email)")
                print("  Format: (program name) email password [protocol://proxy:port]\n")
                print("  Example: wa.py pocketrocket123@dikbut.co.nz foobar 192.168.0.0:80")
                time.sleep(2)
                sys.exit(1)
				
try: password = sys.argv[2]
except IndexError:
                print(" [!] Your account file is written improperly! (Check your password)")
                print("  Format: (program name) email password [protocol://proxy:port]\n")
                print("  Example: money.py pocketrocket123@dikbut.co.nz foobar 192.168.0.0:80")
                time.sleep(2)
                sys.exit(1)

try: proxy = sys.argv[3]
except IndexError: 
	pass
	print("[!] No proxy server detected")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--start-muted")
try: proxy
except NameError:
	proxy = ""
	print("Using local IP.") 
	chrome_options.add_argument("--start-muted")
	chrome_options.add_argument("--disable-dev-tools")
	chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36")
else: 
	chrome_options.add_argument("--proxy-server=" + proxy)
	chrome_options.add_argument("--start-muted")
	chrome_options.add_argument("--disable-dev-tools")
	chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36")
	print("Using proxy " + proxy)
	

try: driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = 'res/chromedriver.exe')
except:
    print("error")
    sys.exit(1)

print("ok\nattempting login: ", end="")
try:
    driver.get("https://freebitco.in/?op=home")
    time.sleep(3)
    driver.find_elements_by_class_name('login_menu_button')[0].click()
    driver.find_element_by_id('login_form_btc_address').send_keys(gmail)
    time.sleep(2)

    driver.find_element_by_id('login_form_password').send_keys(password)
    driver.find_element_by_id('login_button').click()
    time.sleep(2)
except:
    print("error")
    sys.exit(1)

print("ok\nur gucci enjoi ", end="")
