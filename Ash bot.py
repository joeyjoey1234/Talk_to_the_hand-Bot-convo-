import requests
import pyperclip
from pynput.mouse import Button,Controller
import time
import clipboard
mouse = Controller()
import keyboard


###Set your initial positions of where you want your chat to copy text and where to past responses from the BOT
chat_box_position = (-789, 625)
inital_position_behind_sentence = (-846, 494)
start_of_sentence = (-823, 497)
end_of_sentence = (-109, 547)



## Throw your cookie information into this field from the https://www.pandorabots.com/mitsuku/ bot when talking to "her"
## you can change these to what ever bot you want
sessionid = '403638653'
channel = "6"
botkey = "n0M6dW2XZacnOgCWTp0FRYUuMjSfCkJGgobNpgPv9060_72eKnu3Yl-o1v2nFGtSXqfwJBG2Ros~"
client_name = "cw16dcb9b5a69"



while True:
    mouse.position = inital_position_behind_sentence
    mouse.press(Button.left)
    time.sleep(1)
    mouse.position = end_of_sentence
    time.sleep(1)
    mouse.release(Button.left)
    time.sleep(1)
    mouse.position = start_of_sentence
    ###This Mouse move position below is the position of the copy button when opening the right click menu
    mouse.click(Button.right)
    time.sleep(1)
    mouse.move(50, 10)
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)
##copy user response, its in clipboard now
    ash_answer = clipboard.paste()
    #ash_answer = "donate"
    print(ash_answer)
    #this is where i sent the post to the BOT, change this to what ever bot you want.
    r = requests.post("https://miapi.pandorabots.com/talk",data={'input': ash_answer, 'sessionid': sessionid, 'channel': channel,'botkey':botkey,'client_name':client_name},headers={'Content-type': 'application/x-www-form-urlencoded','Origin': 'https://www.pandorabots.com','Referer': 'https://www.pandorabots.com/mitsuku/','Sec-Fetch-Mode': 'cors','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'})
    response = r.text
    response = response.split('"')
    print(response)
    print(response[7])
    answer = response[7]
    clipboard.copy(answer)
    ###This Mouse position setting is for the response, it clicks on the text box for and copy and pastes the Bots response and presses enter.
    mouse.position = (-789, 625)
    mouse.click(Button.left)
    keyboard.press_and_release('ctrl+v, enter')
    ##this input pauses the script, Press enter when response is ready to be sent and done move the mouse.
    huh = input("Press enter once user responds")





