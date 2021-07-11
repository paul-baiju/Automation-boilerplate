import requests
import os
from bs4 import BeautifulSoup as Soup

def resource_finder(selected_option):
    return {
        'html': 'https://raw.githubusercontent.com/paul-baiju/Automation-boilerplate/main/resources/base/index.html',
        'php': 'https://raw.githubusercontent.com/paul-baiju/Automation-boilerplate/main/resources/base/index.html',
        'css': 'https://raw.githubusercontent.com/paul-baiju/Automation-boilerplate/main/resources/base/index.css'
    }[selected_option]

def add_css(data_css):
    if not os.path.exists("css/"):
        os.makedirs("css/")
        f = open('css/style.css','w')
    else:
        f = open('css/style.css','a')
    f.write(data_css)
    f.close()

print("Select file type:")
options = ["html", "php"]

def let_user_pick(options):
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,element))
    i = input("Enter option number: ")
    try:
        if 0 < int(i) <= len(options):
            return (options[int(i)-1])
    except:
        pass
    return None

selected_option = let_user_pick(options)
print(selected_option)

r = requests.get(resource_finder(selected_option))
'Requests:' in r.text
r.headers['Content-Type']
'text/plain; charset=utf-8'

pageData = r.text
soupData = Soup(pageData, "html.parser")
title = soupData.find('title')

data_title = input("Enter the title: ")
title.insert(1,data_title)    

if selected_option == "php":
    f = open('index.php','w')
else:
    f = open('index.html','w')

r = requests.get(resource_finder("css"))
add_css(r.text)

pageData = str(soupData)
f.write(pageData)
f.close()