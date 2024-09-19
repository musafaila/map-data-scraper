
def parse_hospital_details(details: []):

    HOSPITAL_DETAILS = {}

    for detail in details:
        detail_title = detail.find("h4", class_="panel-title").text.strip()

        details_rows = ((detail.find(class_="panel-collapse")
                        .find(class_="panel-body"))
                        .find_all(class_="row"))

        data = []
        for row in details_rows:
            detail_label = row.find("label").text.strip().split(":")[0]

            detail_value = None

            if detail_label == "Specific Clinical Services":
                services = row.find(id="specialservice").find_all("span")
                services = [service.text.strip() for service in services]
                detail_value = services
            else:
                detail_value = row.find("div").text.strip()

            data.append({
                "label": detail_label,
                "value": detail_value
            })

        hospital_details_values = {item["label"]: item["value"] for item in data}

        HOSPITAL_DETAILS[detail_title] = hospital_details_values


    return HOSPITAL_DETAILS


'''
 {
    identifiers: {facility_code: 12345},
    location: {title, data},
 }
'''