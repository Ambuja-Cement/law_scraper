import requests

#url of the website
base_url = "https://lddashboard.legislative.gov.in/documents/legislative-references/list-of-acts-yearwise?field_acts_yearwise_tid=All"
suffix = "&page="

def get_url(page):
    if page == 0:
        return base_url
    else:
        return base_url + suffix + str(page)
    
def get_page(page):
    url = get_url(page)
    #Getting SSL error, so I am using the following line of code to ignore it
    response = requests.get(url, verify=False)
    return response.text.encode("utf-8")

print(get_page(0))