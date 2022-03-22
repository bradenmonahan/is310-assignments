import requests,json
from bs4 import BeautifulSoup
url_list=[]
clean_url_list=[]
with open('raw_script_urls.txt', encoding='ISO-8859-1') as f:
    for index,line in enumerate(f):
        x=(line.split('+++$+++'))
        urls=(x[-1])
        url_list.append(urls)
new_file=open('spring_break_assignment_file','w')
for url in url_list:
    url=url.strip()
    clean_url_list.append(url)

for url in clean_url_list[:50]:

        if 'html' in url:
            response = requests.get(url)
            html_string = response.text
            document = BeautifulSoup(html_string, "html.parser")
            y=document.find("pre").text
            new_file.write(y)
        if "txt" in url:
            r=requests.get(url).text
            new_file.write(str(r))

    
new_file.close()
    
