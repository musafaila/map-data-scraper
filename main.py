
from resource import urls
from scraper import scraper


def main():

    # name = input('Please enter Your Name: ')

    for url in urls:

        url_to_scrape = url.get('url')
        state = url.get('state')


        scraper(url=url_to_scrape, state=state )

        print(f'Done scraping hospitals for {state}')

main()
