
"""
this the core of the search engine
"""

from bs4 import BeautifulSoup
import re



class ProcessHtml:
    """
    this class parses a html code
    and gives some data about it
    """

    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.tags_number = 0
        self.pattern = re.compile(r'\b\w{2,50}\b')
        self.tags = {}
        self.words_number = 0
        self.words = {}
        self.links = []
        self.images = {}
        self.process()

    def process(self):
        """
        this parse the html code and store some
        meta data
        """
        tags = self.soup.find_all()
        self.tags_number = len(tags)
        words = self.pattern.findall(self.soup.text)
        self.words_number = len(words)

        for tag in tags:

            # storing links
            if tag.name == 'a':
                self.links.append(tag.get('href'))
            
            if tag.name == 'img':
                self.images[tag.get('src')] = tag.get('alt')
            # counting every tag and storing their repetition
            if tag.name in self.tags:
                self.tags[tag.name] += 1
            else:
                self.tags[tag.name] = 1

        for word in words:
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1
        
        


