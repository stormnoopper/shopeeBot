import pyautogui as pg
import time

#Run Code using Shift+Enter

#Some of Item have to select product information
#You can add code like ButButton

#BuyButton
pg.click(455,518,2)
time.sleep(0.75)

#ConfirmCartButton
pg.click(575,486,2)
time.sleep(0.75)

#ConfirmPayment
pg.scroll(-10000)
time.sleep(0.75)
pg.click(591,418,2)

#After This have to vertify your payment