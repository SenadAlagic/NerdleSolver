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
    #getRowsLegacy()
    global timesGuessed
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
    getRows()
    analyzeGuess()
    timesGuessed+=1


def getRowsLegacy():
    global rows
    rows=[]
    grid=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]')
    rows=grid.find_elements(By.XPATH,'.//*')
    print("len rows",len(rows))

def getRows():
    global rows
    rows=[]
    for i in range(0,6):
        row=[]
        for j in range(0,7):
            row.append(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div['+str((i+1))+']/div['+str((j+1))+']'))
        rows.append(row)

def analyzeGuess():
    global presentCharacters
    for i in range(0, len(rows[timesGuessed])):
        if "present" in rows[timesGuessed][i].get_attribute('aria-label'):
            presentCharacters.append(rows[timesGuessed][i].get_attribute('aria-label')[0])
        elif "correct" in rows[timesGuessed][i].get_attribute('aria-label'):
            correctGuess[i]=rows[timesGuessed][i].get_attribute('aria-label')[0]

link='https://nerdlegame.com/'
service=Service("drivers/geckodriver.exe")
buttons=[]
rows=[]
timesGuessed=0
presentCharacters=[]
correctGuess=['#','#','#','#','#','#','#','#']
driver=webdriver.Firefox(service=service)

Boot()
ButtonsSetup()
getRows()
playGuess('9*8-7=65')
playGuess('0+12/4=3')

#first rows xpath
#/html/body/div[1]/div/div[3]/div[1]
#first row first element
#/html/body/div[1]/div/div[3]/div[1]/div[1]

#second rows xpath
#/html/body/div[1]/div/div[3]/div[2]


