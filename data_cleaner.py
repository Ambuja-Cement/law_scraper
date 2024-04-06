#This is the json sample
    # {
    #     "s.no": "             988          ",
    #     "year": "",
    #     "name": "             The Fatal Accidents Act, 1855           ",
    #     "act_no": "             13          ",
    #     "download_link": "https://lddashboard.legislative.gov.in/sites/default/files/A1855-13.pdf"
    # }

import json
import re

def clean_data():
    with open("law_data.json", "r") as f:
        data = json.load(f)
        
    for i in range(len(data)):
        data[i]["s.no"] = data[i]["s.no"].strip()
        data[i]["name"] = data[i]["name"].strip()
        data[i]["act_no"] = data[i]["act_no"].strip()
        
        if re.findall(r"\d{4}", data[i]["name"]) != []:
            data[i]["year"] = re.findall(r"\d{4}", data[i]["name"])[0]
            print("Year found in", data[i]["name"], "is", data[i]["year"])
        else:
            data[i]["year"] = ""
            print("No year found in", data[i]["name"])
            
    #Save the cleaned data
    with open("cleaned_law_data.json", "w") as f:
        json.dump(data, f)
        print("Data cleaned and saved to cleaned_law_data.json")
        

clean_data()

