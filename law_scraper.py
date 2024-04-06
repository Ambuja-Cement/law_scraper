#I want to make a webscraper using beautiful soup to go over multuple pages of a website and get the data that I need and put it into an organized json file.
#The data has the following parameters year of the act, name of the act,and the act no associated with it.
import requests
from bs4 import BeautifulSoup
import json
from rich import print_json
import re
#url of the website
base_url = "https://lddashboard.legislative.gov.in/documents/legislative-references/list-of-acts-yearwise?field_acts_yearwise_tid=All"
suffix = "&page="

def get_url(page):
    if page == 0:
        return base_url
    else:
        return base_url + suffix + str(page)
    
def get_raw_data(page):
    url = get_url(page)
    #Getting SSL error, so I am using the following line of code to ignore it
    response = requests.get(url, verify=False).text.encode("utf-8")
    
    soup = BeautifulSoup(response, "html.parser")
    #I want all the elements that have the scroll-table1 class
    table = soup.find_all("table", class_="views-table")
    return table

#Now we need to clean up the data and put it into a json file by extracting relevant info from the list of tables
def get_clean_data(page):
    raw_data = get_raw_data(page)
    table_data = []
    for table in raw_data:
        rows = table.find_all("tr")
        table_data.append(rows)
        
    #Putting the data from table_data into a json file, the table has s.no, Name of Acts, Attachment File, Acts No.
    data = []
    for row in table_data:
        for i in range(1, len(row)):
            data.append({
                "s.no": row[i].find_all("td")[0].text,
                "year": "" ,
                "name": row[i].find_all("td")[1].text,
                "act_no": row[i].find_all("td")[3].text,
                "download_link": row[i].find_all("td")[2].a["href"]
            })
            
        #Go through all the data and get the year of the act using regex from the name of the act
    
    return data

# def regex_dates(data):
#     for i in range(len(data)):
#         data[i]["year"] = re.findall(r"\d{4}", data[i]["name"])

# my_data = get_clean_data(0)
# final_data =  regex_dates(my_data)

print_json(data=get_clean_data(1))


    