import subprocess
import time
from subprocess import Popen
#import keyboard
i = 0
toWho = "DonateTo"
#Be aware of trovo invite limit. (5 per account.)
who = "FirstName"
pc_name = "test"

def rerun():
    time.sleep(1)
    global i
    i += 1
    while i <= 50:
      if i >= 5:
        global who
        who = "trovoUserName"
      if i >= 10:
        who = "trovoUserName"
      if i >= 15:
        who = "trovoUserName"
      if i >= 20:
        who = "trovoUserName"
      if i >= 25:
        who = "trovoUserName"
      if i >= 30:
        who = "trovoUserName"
      if i >= 35:
        who = "trovoUserName"
      if i >= 40:
        who = "trovoUserName"
      if i >= 45:
        who = "trovoUserName"
      print(i)
      run_opera_private()
    else:
       print("Gotovo farmanje mane by aleks4k")
       exit()

def run_opera_private():
    cmd = r"C:\Users\{}\AppData\Local\Programs\Opera\launcher.exe --private --remote https://trovo.live/{}?adtag=user.{}.clip".format(pc_name, toWho, who)
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(18)
   # keyboard.press_and_release('ctrl+w') # closes the last tab
    Popen('taskkill /F /IM opera.exe', shell=True) #ovo je kad igras neku igricu ili bilo sta za potpuni afk farm
    rerun()

if __name__ == '__main__':
    run_opera_private()