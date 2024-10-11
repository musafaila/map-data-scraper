
from resource import urls
from scraper import scraper


def main():

    name = input('Please enter Your Name: ')

    for i in range(len(urls)):
        data = scraper(url=urls[i], name=name, index=i )
        print(len(data))


main()
