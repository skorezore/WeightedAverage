import sys, random, time, os, platform, datetime, json
from selenium import webdriver
from random import randint
import datetime as d

systeminforma = sys.platform

def solve_recaptcha(self, website_url, captcha_key, client_key):
        return bloop('gRecaptchaResponse', {'clientKey': client_key, 'task': {'type': 'NoCaptchaTaskProxyless',
                                                                                          'websiteURL': website_url,
                                                                                          'websiteKey': captcha_key,
                                                                                          'softId': 0,
                                                                                          'languagePool': 'en'}})
def bloop(type, arguments):
        response = requests.post('https://api.anti-captcha.com/createTask', data = json.dumps(arguments)).json()

        if response['errorId'] != 0:
            raise RuntimeError(response['errorDescription'])

        task_id = response['taskId']

        arguments = {'clientKey': arguments['clientKey'], 'taskId': task_id}

        while True:
            time.sleep(2)
            fudge = requests.post('https://api.anti-captcha.com/getTaskResult', data = json.dumps(arguments)).json()

            if fudge['status'] == 'ready':
                return fudge['solution'][type]

            if fudge['errorId'] != 0:
		raise RuntimeError(fudge['errorDescription'])

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

while True:
	time.sleep(3660)
	
	driver.execute_script('document.getElementById("g-recaptcha-response").value = "' + solve_recaptcha('https://www.freebitco.in', '6Lc6zQQTAAAAAD8TgxgC59CXtm1G56QLu8G7Q53K', '95b51d0b3eae21b747fdbbb1eba25b1f') + '"')
	driver.find_element(button).click()
