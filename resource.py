# NOTE: INSTRUCTIONS

# git clone the repo
# install python if you don't have it
# run "pip install requirements.txt"
# Comment all the urls and only uncomment the one with your name at the top
# goto your terminal, and navigate to the directory.
# finally run "python main.py"

BASE_URL = "https://www.hfr.health.gov.ng/facilities/hospitals-search?_token=7ku8aWpTppSbctWH3ytOBaFCEgaOtpBz7YJ07NXo&state_id=1&ward_id=0&facility_level_id=0&ownership_id=0&operational_status_id=1&registration_status_id=0&license_status_id=0&geo_codes=0&service_type=0&service_category_id=0&entries_per_page=5000"

# FAILA
urls = [
    f"{BASE_URL}&page=1",
    f"{BASE_URL}&page=2",
]

# HASSAN
# urls = [
#     f"{BASE_URL}&page=3",
#     f"{BASE_URL}&page=4",
# ]

# PROF
# urls = [
#     f"{BASE_URL}&page=5",
#     f"{BASE_URL}&page=6",
# ]

# Other person
# urls = [
#     f"{BASE_URL}&page=7",
#     f"{BASE_URL}&page=8",
# ]