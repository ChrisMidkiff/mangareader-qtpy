from __future__ import print_function
import requests
from searchclass import searchclass
import json
import urllib
kavitaSession = requests.Session()


def login():
    r = kavitaSession.post('http://192.168.1.94:5000/api/Account/login',
                           json={'apiKey': 'e9cedc02-5b82-4269-9fd4-53fa86e05d88', 'username': 'chris', 'password': 'password'})
    kavitaSession.headers['Authorization'] = 'Bearer ' + r.json()['token']


def getmangaiconfromurl(url):
    print('image: ' + url)
    if 'series-detail' in url:
        seriesId = url.split('?seriesId=')[1]
        url = 'http://192.168.1.94:5000/api/image/series-cover?apiKey=e9cedc02-5b82-4269-9fd4-53fa86e05d88&seriesId=' + seriesId
    return url


def image_lists(url):
    images = []
    chapter = kavitaSession.get(url).json()
    pageCount = chapter['pages']
    chapterId = url.split('chapterId=')[1]
    volumeId = str(chapter['volumeId'])
    seriesId = str(chapter['seriesId'])
    for x in range(1, pageCount+1):
        images.append('http://192.168.1.94:5000/api/reader/image?apiKey=e9cedc02-5b82-4269-9fd4-53fa86e05d88&chapterId=' + chapterId + '&page=' + str(x))
    nextElement = None
    prevElement = None
    r = kavitaSession.get('http://192.168.1.94:5000/api/reader/prev-chapter?seriesId=' +
                          seriesId + '&volumeId=' + volumeId + '&currentChapterId=' + chapterId)
    if r.text != '-1':
        prevElement = {'href': 'http://192.168.1.94:5000/api/reader/chapter-info?includeDimensions=true&chapterId=' + r.text}
    r = kavitaSession.get('http://192.168.1.94:5000/api/reader/next-chapter?seriesId=' +
                          seriesId + '&volumeId=' + volumeId + '&currentChapterId=' + chapterId)
    if r.text != '-1':
        nextElement = {'href': 'http://192.168.1.94:5000/api/reader/chapter-info?includeDimensions=true&chapterId=' + r.text}
    return [images, prevElement, nextElement]


def getSearchResult(text):
    text = str(text)
    text = urllib.quote(text)
    login()
    r = kavitaSession.get('http://192.168.1.94:5000/api/search/search?queryString=' + text)
    results = r.json()['series']
    data = []
    for result in results:
        seriesId = str(result['seriesId'])
        meta = kavitaSession.get('http://192.168.1.94:5000/api/series/metadata?seriesId=' + seriesId)
        authors = meta.json()['writers']
        author = ''
        if len(authors) > 0:
            author = authors[0]['name']
        newres = searchclass()
        newres.setUrl('http://192.168.1.94:5000/api/series/series-detail?seriesId=' + seriesId)
        newres.setTitle(result['name'])
        newres.setAuthor(author)
        newres.setIcon('http://192.168.1.94:5000/api/image/series-cover?apiKey=e9cedc02-5b82-4269-9fd4-53fa86e05d88&seriesId=' + seriesId)
        data.append(newres)
    print(data)
    return data


def processing_chapters(url):
    print(url)
    login()
    r = kavitaSession.get(url)
    chapters = r.json()['chapters'] + r.json()['specials']
    print(chapters)
    for v in r.json()['volumes']:
        for c in v['chapters']:
            c['title'] = c['titleName']
            c['number'] = v['number']
            chapters.append(c)
    data = []
    chapters = sorted(chapters, key=lambda x: x['number'])
    for chapter in chapters:
        chapterId = str(chapter['id'])
        meta = kavitaSession.get('http://192.168.1.94:5000/api/series/chapter-metadata?chapterId=' + chapterId)
        authors = meta.json()['writers']
        author = ''
        if len(authors) > 0:
            author = authors[0]['name']
        newres = searchclass()
        newres.setUrl('http://192.168.1.94:5000/api/reader/chapter-info?includeDimensions=true&chapterId=' + chapterId)
        newres.setTitle(chapter['title'])
        newres.setAuthor(author)
        newres.setIcon('http://192.168.1.94:5000/api/image/chapter-cover?apiKey=e9cedc02-5b82-4269-9fd4-53fa86e05d88&chapterId=' + chapterId)
        data.append(newres)
    return data


if __name__ == '__main__':
    print(getSearchResult('ring'))
