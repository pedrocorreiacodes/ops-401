# The below Python script is one possible way to return the cookie from a site.
import requests

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
# Comment this out if you're using the line above
targetsite = "http://www.whatarecookies.com/cookietest.asp"
response = requests.get(targetsite)
cookie = response.cookies


def bringforthcookiemonster():  # Because why not!
    print('''
              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
        ''')


bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

#################################
#### POSSIBLE SOLUTION BELOW ####
#################################

response = requests.get(targetsite, cookies=cookie)
print(response.text)

# Student should also save the response to a file and open it with Firefox, which is not shown here.
