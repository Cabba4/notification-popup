import requests
import xml.etree.ElementTree as ET

# news url will be changed

DISPLAY_URL = "http://feeds.bbci.co.uk/news/world/rss.xml"


def loadDISP():
    # making request to url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    resp = requests.get(DISPLAY_URL, headers=headers)
    # returning content
    return resp.content


def parseXML(resp):  # parsing xml from content
    root = ET.fromstring(resp)
    # element tree root object

    # empty string for news
    newsitems = []

    # loading news item
    for item in root.findall('./channel/item'):
        news = {}
        # iterate child elements of item

        for child in item:
            # some check for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf-8')
            newsitems.append(news)
    return newsitems


def topStories():
    # main funct to generate and rename news items

    resp = loadDISP()
    # parse Display
    newsitems = parseXML(resp)
    return newsitems

if __name__ == '__main__':
    display = topStories()
    print(display)