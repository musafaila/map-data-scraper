
from resource import entries_per_page, number_of_pages, BASE_URL
from scraper import scraper


def main():

    name = input('Please enter Your Name: ')

    for i in range(number_of_pages['min'], number_of_pages['max'] + 1):

        url = f"{BASE_URL}&entries_per_page={entries_per_page}&page={i}"

        data = scraper(url=url, name=name, page=i )

        if data:
            print(f"scraped page {i} with {len(data)} number of hospitals")
            # print(len(data))


main()
