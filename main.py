import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

from parser import parse_hospital_details
from utils import save_to_json


def main():
    HOSPITALS_DETAILS = []
    try:
        url = ("https://www.hfr.health.gov.ng/facilities/hospitals-search?_token"
               "=E3321E8IgvQTOPw8JH4IiX8U2TBmjoqDfTwOfzEq&state_id=133&ward_id=0&facility_level_id=0&ownership_id=0"
               "&operational_status_id=1&registration_status_id=0&license_status_id=0&geo_codes=0&service_type=0"
               "&service_category_id=0&entries_per_page=2000#")

        driver = webdriver.Firefox()

        driver.get(url)

        # Wait for the hospital table to be visible
        hospitals_table = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"hosp"))
        )

        hospitals = (hospitals_table.find_element(By.TAG_NAME, "tbody")
                     .find_elements(By.TAG_NAME, "tr"))

        for hospital in hospitals:
            try:
                hospital_id = hospital.find_elements(By.TAG_NAME, "td").text.strip()

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
            except Exception as e:
                print("Error in Fetching Hospital Details: ", e)
                continue

    except Exception as e:
        print(e)
    finally:
        driver.quit()
        save_to_json('hospitals.json', HOSPITALS_DETAILS)
        print("DONE!")


main()
