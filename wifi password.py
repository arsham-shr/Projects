import subprocess
import wifiPassword

name = subprocess.getoutput("netsh wlan show profiles").replace("Profiles on interface Wi-Fi:","").replace("Group policy profiles (read only)","").replace("---------------------------------","").replace("<None>","").replace("\n","").replace("User profiles","").replace("-------------","").replace("All User Profile","").replace(":","")
name2 = name.split()
for i in name2:
    a = subprocess.getoutput("wifipassword " + i)
    print(a)