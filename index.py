import requests

print("Select file type:")
options = ["html", "php"]

def let_user_pick(options):
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,element))
    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return (options[int(i)-1])
    except:
        pass
    return None

selected_option = let_user_pick(options)
print(selected_option)

r = requests.get('https://raw.githubusercontent.com/paul-baiju/Automation-boilerplate/main/resources/index.html')
'Requests:' in r.text
r.headers['Content-Type']
'text/plain; charset=utf-8'

f = open('index.html','w')
f.write(r.text)
f.close()