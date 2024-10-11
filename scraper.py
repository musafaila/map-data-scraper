import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

from parser import parse_hospital_details
from utils import save_to_json


def scraper(url, state):
    print(f'scraping "{url}"')

    HOSPITALS_DETAILS = []
    ERRORS = []

    driver = None
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')

        driver = webdriver.Firefox(options=options)
    except Exception as e:
        print(e)

    try:
        if not driver:
           return

        print("")
        print('fired')
        print("")

        driver.get(url)

        # Wait for the hospital table to be visible
        hospitals_table = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"hosp"))
        )

        hospitals = (hospitals_table.find_element(By.TAG_NAME, "tbody")
                     .find_elements(By.TAG_NAME, "tr"))

        for hospital in hospitals:
            hospital_id = None
            try:
                hospital_id = hospital.find_elements(By.TAG_NAME, "td")[3].text.strip()

                hospital_infos = hospital.find_elements(By.TAG_NAME, "td")

                details_button = WebDriverWait(hospital_infos[-1],10).until(
                    EC.visibility_of_element_located((By.TAG_NAME,"button"))
                )
                details_button.click()

                time.sleep(1)

                page = BeautifulSoup(driver.page_source, "html.parser")

                hospital_details = page.find(id="accordion").find_all(class_="panel")

                hospital_details = parse_hospital_details(hospital_details)

                # Close the modal by clicking the close button
                modal_close_btn = WebDriverWait(driver,10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME,"close"))
                )
                modal_close_btn.click()

                HOSPITALS_DETAILS.append(hospital_details)

                print(f'{hospital_id} details added!')
            except Exception as e:
                print("Error in Fetching Hospital Details: ", e)
                ERRORS.append(hospital_id)
                continue

    except Exception as e:
        print(e)
    finally:
        driver.quit()


        if len(ERRORS) > 0:
            save_to_json(f'{state}-errors.json', ERRORS)

        print("DONE!")