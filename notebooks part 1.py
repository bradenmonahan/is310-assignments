# Step 0: Import libraries

from bs4 import BeautifulSoup
import requests
import json
import pandas as pd



def scrape_webpage(url): #rename function to be more meaningful
    response = requests.get(url)

    html_string = response.text
    return html_string

# Step 1: Create a function for getting the urls wuth title
#lowercase and underscores are the normal convention for naming functions in Python. Camelcasing like you had is more normal in JavaScript or for classes.
def get_content(url='', keyword='', filename='', url_head="https://humanist.kdl.kcl.ac.uk/Archives/Converted_Text/"):
    content = scrape_webpage(url)
    soup = BeautifulSoup(content, "html.parser")
 
    links = soup.find_all('a')
    # linkList = []
    # volumeList = [] #Save yourself having to zip your lists by just creating your dictionary from the ouset
    result = {} #Create a dictionary to store the results, and give a more descriptive name to the variable
    for link in links:
        text = link.get_text().lower()
        if keyword in text:
            result[text] = url_head + link.get('href')
            # linkList.append(url_head + link.get('href'))
            # volumeList.append(text)

    # res = dict(zip(volumeList, linkList))

    # Saving into new py doc

    with open(filename, 'w') as file:
        file.write(json.dumps(result, indent=2))
    return result

ls=[]    
res = get_content(
    url="https://humanist.kdl.kcl.ac.uk/Archives/Converted_Text/",
    keyword="humanist",
    filename="main_page.json")
clean_links=list(res.values())
for link in clean_links:
    url=link
    page=requests.get(url)
    page_text=page.text
    ls.append(page_text)
data={'url':clean_links,
        'text':ls}
humanist_vols = pd.DataFrame(data)
humanist_vols.to_csv('web_scraped_humanist_listserv.csv')





