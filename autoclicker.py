import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

print("\033[1;32;40m\n""""{}
 _____ _   _______ _____ _____                                          
/  ___| | | |  _  \  _  /  ___|                                         
\ `--.| | | | | | | | | \ `--.                                          
 `--. \ | | | | | | | | |`--. \                                         
/\__/ / |_| | |/ /\ \_/ /\__/ /                                         
\____/ \___/|___/  \___/\____/                                          
                                                                        
                                                                        
  ___  _   _ _____ _____   _____  _     _____ _____  _   __ ___________ 
 / _ \| | | |_   _|  _  | /  __ \| |   |_   _/  __ \| | / /|  ___| ___ \'
/ /_\ \ | | | | | | | | | | /  \/| |     | | | /  \/| |/ / | |__ | |_/ /
|  _  | | | | | | | | | | | |    | |     | | | |    |    \ |  __||    / 
| | | | |_| | | | \ \_/ / | \__/\| |_____| |_| \__/\| |\  \| |___| |\ \ 
\_| |_/\___/  \_/  \___/   \____/\_____/\___/ \____/\_| \_/\____/\_| \_|
                                                                                                                                   
{}\n\t[+] Welcome To Sudos's Auto Clicker (•◡ •) /\n\t[+] *Ctrl + c To Stop*\n\t[+] Subscribe To Sudo On YT\n{}""".format("="*100,"="*100,"="*100))

delay1 = input("[+] Enter your delay here --> ")
start = input("[+] Enter your start key here --> ")
end = input("[+] Enter your end key here --> ")

delay = float(delay1)
button = Button.left
start_stop_key = KeyCode(char=start)
exit_key = KeyCode(char=end)

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True
        print("[+] Clicking has started")

    def stop_clicking(self):
        self.running = False
        print("[+] Clicking has ended")

    def exit(self):
        self.stop_clicking()
        self.program_running = False
        print("[+] Exiting...")

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()