**Steps to consider before running the project**

Step 1: Website clone location of Boots: Please be noted that the local/developed location of the extracted Sleep Aid Clone is D:/Downloads/Sleep Aid Clone/
        Please point this to your local path before running the project. Line number: 25 

Step 2: The Absolute path of the output.json is D:/data/output.json. Please change that as well to match your local machine's path. Line number: 104

**Dependencies to Consider**

Please add the following external dependencies to the project

1. BeautifulSoup from bs4
2. webdriver from selenium

**Run the boots_temp.py** 

This will generate output.json in the below format after considerable amount of execution time since the scraping is happening on the local website clone.

{
    "Products": [
        {
            "Title": "Boots Sleepeaze Tablets 50 mg - 20s",
            "Price": "5.79",
            "Price_Unit": "£",
            "Short_Desc": "20UNI | £0.29 per 1UNI",
            "Rating": "4.1",
            "Page_size": 41.4208984375
        },
        {
            "Title": "Boots Sleepeaze Tablets 25 mg - 20s",
            "Price": "3.90",
            "Price_Unit": "£",
            "Short_Desc": "20UNI | £0.20 per 1UNI",
            "Rating": "2.7",
            "Page_size": 41.2275390625
        }
        ]
}



