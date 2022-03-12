from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

moodle_url = 'http://52.39.5.126/'
hmpg_title = 'Software Quality Assurance Testing'

print()
print('------------------------- Moodle App Scenario by CCTB Cohort 3 --------------------------------------')
print()
print('set up, log in admin, create user, search user, log out, log in new user,
      log out, log in admin, delete new user, log out, tear down')


def setUp():
    print()
    print(f'--------------------------------------- SET UP FUNCTION --------------------------------------------')
    print()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(moodle_url)
    if driver.current_url == moodle_url and driver.title == hmpg_title:
        print(f'Moodle app launched successfully.')
        print(f'homepage url:{driver.current_url}, title: {driver.title}')
        sleep(0.25)
    else:
        print(f'Moodle did not launch. Check your code or app.')
        print(f'current url: {driver.current_url}, page title: {driver.title}')

def log_in_admin():
    print(f'------------------------------LOGIN FUNCTION----------------------------------------------------')
    if driver.current_url == locators.moodle_url: # check we are on the homepage
        driver.find_element(By.LINK_TEXT, 'Log in').click()
    if driver.current_url == locators.moodle_login_page_url  and driver.title == locators.moodle_login_page_title:
        print(f'{locators.app} App Login page is displayed! Continue to log in.')
        sleep(0.25)
        driver.find_element(By.ID, 'username').send_keys(username)
        sleep(0.25)
        driver.find_element(By.ID, 'password').send_keys(password)
        sleep(0.25)
        driver.find_element(By.ID,'loginbtn').click() # method 1 using ID
        # validate login successful Dashboard page is displayed
        if driver.current_url == locators.moodle_dashboard_url and driver.title == locators.moodle_dashboard_title:
            assert driver.current_url == locators.moodle_dashboard_url
            assert driver.title == locators.moodle_dashboard_title
            print(f'Login is successful. {locators.app} Dashboard is displayed - Page title: {driver.title}')
        else:
            print(f'Dashboard is not displayed. Check your code or website and try again.')
      

      
      
def log_out():
    print(f'------------------------------LOGOUT FUNCTION---------------------------------------------------')
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()  # // means to search everywhere in the file;
    # . search anything that has after the .
    sleep(0.25)
    if driver.current_url == locators.moodle_url:
        print(f'-----Logout is done! {datetime.datetime.now()}')
      
      
      create_new_user():
    # Navigate to 'Add a new user' form
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT,'Users').is_displayed()
    linkchek = driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    print(f'------ User link is displayed: {linkchek}')
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT,'Add a new user').click()
    sleep(.025)
     # Validate we are on 'Add a new user  page
    assert driver.find_element(By.LINK_TEXT,'Add a new user').is_displayed()
    assert driver.title == locators.moodle_add_new_user_page_title
    print(f'---------Navigate to Add a new user page -Page Title: {driver.title}')
    sleep(0.25)
    driver.find_element(By.ID,'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By. ID,'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID,'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID,'id_email').send_keys(locators.email)
    sleep(0.25)
    Select(driver.find_element(By.ID,'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID,'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    Select(driver.find_element(By.ID,'id_country')).select_by_visible_text(locators.country)
    sleep(0.25)
    Select(driver.find_element(By.ID,'id_timezone')).select_by_value('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID,'id_description_editoreditable').clear()
    driver.find_element(By.ID,'id_description_editoreditable').send_keys(locators.description)
    sleep(0.5)

      

      
setUp()
log_in_admin()
log_out()
create_new_user()
