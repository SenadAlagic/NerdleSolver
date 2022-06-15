from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import schedule
import time


def Boot():
    driver.get(link)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]').click()

def ButtonsSetup():
    global buttons
    allButtons=driver.find_elements(By.TAG_NAME,'button')
    allButtons.pop()
    del allButtons[0]
    del allButtons[0]
    del allButtons[0]
    allButtons[0]=allButtons[10]
    del allButtons[10]
    buttons=allButtons
    '''
    for button in allButtons:
        print("Button",button.get_property("innerHTML"))
        button.click()
    '''
    
def playGuess(guess):
    for char in guess:
        if char.isdigit():
            buttons[int(char)].click()
        elif char=='+':
            buttons[10].click()
        elif char=='-':
            buttons[11].click()
        elif char=='*':
            buttons[12].click()
        elif char=='/':
            buttons[13].click()
        elif char=='=':
            buttons[14].click()
    buttons[15].click()

def getRows():
    global rows
    grid=driver.find_element(By.XPATH,'/html/body/div/div/div[3]')
    rows=grid.find_elements(By.XPATH,'.//*')

link='https://nerdlegame.com/'
service=Service("drivers/geckodriver.exe")
buttons=[]
rows=[]
driver=webdriver.Firefox(service=service)

Boot()
ButtonsSetup()
getRows()
playGuess('9*8-7=65')
playGuess('0+12/4=3')



