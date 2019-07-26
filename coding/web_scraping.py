from bs4 import BeautifulSoup
import urllib3
import re

URL = 'https://www.pinterest.com/pin/325033298107933621/'

http = urllib3.PoolManager()
r = http.request('GET', URL)
html_page = r.data      # raw data
html_page = html_page.decode()  # convert to `str`

# Create an object of `bs4`
"""
    NOTE: Here, "lxml" parser is given to the function, although it is not needed.
    But it gives WARNING.
"""
soup = BeautifulSoup(html_page, "lxml")
links = []  # empty list

# extract only those links where 'rel' attribute is present with 'link' tag 
for link in soup.findAll('link', {'rel': 'alternate'}):
    if link.has_attr('href'):
        links.append(link['href'])

# -----------------------------------------------------------------------------------------
# Write content to a Text file

# open a file and if doesn't exist, create one in the same directory
f = open('work-7.txt', 'w+')

# write the content
for l in links:
    f.write(f'{l} \n')      # along a column

# Don't forget to close the opened file
f.close()