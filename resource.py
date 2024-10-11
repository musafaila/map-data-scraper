# NOTE: INSTRUCTIONS

# git clone the repo
# install python if you don't have it
# run "pip install -r requirements.txt"
# Comment all the settings(number of pages) and only uncomment the one with your name at the top
# goto your terminal, and navigate to the directory.
# finally run "python main.py"

entries_per_page = 500
BASE_URL = f"https://www.hfr.health.gov.ng/facilities/hospitals-search?_token=7ku8aWpTppSbctWH3ytOBaFCEgaOtpBz7YJ07NXo&state_id=1&ward_id=0&facility_level_id=0&ownership_id=0&operational_status_id=1&registration_status_id=0&license_status_id=0&geo_codes=0&service_type=0&service_category_id=0"

# FAILA
number_of_pages = {"min": 1, "max": 10}

# HASSAN
# number_of_pages = {"min": 11, "max": 20}

# PROF
# number_of_pages = {"min": 21, "max": 30}

# Others
# number_of_pages = {"min": 31, "max": 40}
