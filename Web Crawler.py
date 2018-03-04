import urllib.request
from bs4 import BeautifulSoup
import newspaper

link = "https://www.allsides.com/unbiased-balanced-news"
link2 = "http://www.bbc.com/news/world-us-canada-42999286"

# Load Page
WebPage = urllib.request.urlopen(link)

# Get source code
source_code = WebPage.read()

# Get tags
tags = source_code.split(b'<')

i = 0

for tag in tags:
    if tag.startswith(b'a href="https://www.allsides.com/news/'):
        newLink = tag[7:]
        # Get all article Links
        if newLink.startswith(b'"https'):
            newLink = newLink.split(b'">', 1)[0]
            newLink = newLink.split(b'" ', 1)[0]
            newLink = newLink[1:]

            # Handle redirection from allsides.com
            WebPage = urllib.request.urlopen(newLink.decode('ASCII'))
            soup = BeautifulSoup(WebPage, 'html.parser')
            aLink = soup.find('iframe')
            newLink = aLink['src']

            # Get contents of the article
            article = newspaper.Article(url=newLink)
            article.download()
            article.parse()

            # Write article.text to a file
            file_directory = ('/Users/akshay/Desktop/data/file%d.txt' % i)
            file = open(file_directory, 'w')
            i += 1
    else:
        pass

article = newspaper.Article(url=link2)
article.download()
article.parse()
file_directory = ('/Users/akshay/Desktop/data/file%d.txt' % i)
file = open(file_directory, 'w')
file.write("\n\n\n*** ARTICLE %d ***\n\n\n" % i)
file.write(article.text)
file.close()
