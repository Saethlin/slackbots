import wikipedia

import urllib2
from bs4 import BeautifulSoup

def find_other_names(target):
    
    target = target.lower()
    
    page_name = wikipedia.search(target)[0]
    
    page = wikipedia.page(page_name)
    url = page.url
    
    opener = urllib2.build_opener()
    the_page = opener.open(url).read()
    soup = BeautifulSoup(''.join(the_page), 'html5lib')
    
    table = soup.find_all('table')[0]
    entries = table.find_all('tr')
    
    row = None
    for entry in entries:
        if 'other designations' in entry.get_text().lower():
            row = entry.get_text()
            break
    
    if row is None:
        return None
    
    row = row.strip()
    row = row.split('\n')[-1]
    
    return row.split(', ')
    
if __name__ == "__main__":
    print(find_other_names('wild duck cluster'))
