from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from importconfig import get_config


def search(driver, word):
    """
    Searches for a set word and returns the driver at the bing search page
    :param driver: current selenium web driver
    :param word: current word to be searched
    :return: return a webdriver at the bing search page
    """
    search_field = driver.find_element_by_id("sb_form")
    search_field.click()

    search_field = driver.find_element_by_name("q")

    # enter search textbox
    search_field.send_keys(str(word))
    search_field.submit()
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "b_content")))
    finally:
        to_bing(driver)


def to_bing(driver):
    """
    Returns the webdriver to bing.com
    :param driver: current webdriver
    :return: VOID
    """
    driver.get("https://www.bing.com/")
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sbox")))
    except:
        print("ERROR")





def start():
    """
    VOID FUNCTION, starts the search process assuming a correctly configured words.txt and config.cfg
    :return:
    """
    print("MicrosoftRewards V 1.0")
    print("Loading Config...")
    try:
        user_list = get_config()
        print("Word file opened...")

    except:
        print("Config could not be found or read. Please ensure you have a valid config.cfg in the root directory")
        exit_quit()

    print("Loading word file...")
    word_file = "words.txt"

    try:
        words = open(word_file).read().splitlines()
        print("Word file opened...")

    except FileNotFoundError:
        print("Could not open word file, are you sure you have a words.txt in the root directory?")
        exit_quit()

    for user in user_list:
        execute(user, words)


def execute(user, words):
    """
    For a set user execute searches with a given word list
    :param user: current instantiated user class, see Users.py for more information
    :param words: list of words
    :return: VOID
    """
    driver = start_browser()
    # Eventually need to implement logging in, currently user just performs the same action regardless of current acct
#    driver = microsoft_login(driver, user)
    for i in range(user.get_num_times()):
        current_word = random.choice(words)
        search(driver, current_word)
        to_bing(driver)

    print("Successfully completed user {}".format(user.get_key()))
    quit_browser()


def start_browser():
    """
    Opens Edge browser and navigate to https://www.bing.com/
    :return: return the instantiated web driver
    """
    # Create new Edge session
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.get("https://www.bing.com/")
    return driver


def microsoft_login(driver, user):
    """
    Login to microsoft account
    :param driver: current webdriver
    :param user: current user to be logged in
    :return: return updated webdriver
    """
    return driver

def quit_browser(driver):
    driver.quit()

def exit_quit():
    """
    ERROR QUIT CASE
    :return:
    """
    print()
    print("FATAL ERROR HAS OCCURRED, EXITING")
    exit()


if __name__ == "__main__":
    start()