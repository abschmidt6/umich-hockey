# import libraries
import urllib2
from bs4 import BeautifulSoup

quote_page = 'http://mgoblue.com/schedule.aspx?schedule=436'

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
page = opener.open(quote_page)

soup = BeautifulSoup(page, 'html.parser')

result_box = soup.find(aria_label='Games Schedule')
print(result_box.text.strip())
