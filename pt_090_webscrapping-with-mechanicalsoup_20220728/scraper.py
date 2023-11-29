import mechanicalsoup
import pandas as pd
import sqlite3

"""
from: https://www.youtube.com/watch?v=MkGQmZoMuRM
Web Scraping Databases with Mechanical Soup and SQlite
Dec 5, 2021 - Python Simplified

data source:
https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions
on 2022-07-28
"""

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")

# extract table headers
th = browser.page.find_all("th", attrs={"class":"table-rh"})
distribution = [value.text.replace("\n", "") for value in th]
distribution = distribution[:distribution.index("Zorin OS") + 1]

# test print
# print(distribution)

# extract table data
td = browser.page.find_all("td")
columns = [value.text.replace("\n", "") for value in td]

# test print
# print(columns.index("AlmaLinux Foundation"))
# print(columns.index("Binary blobs"))

columns = columns[columns.index("AlmaLinux Foundation"):columns.index("Binary blobs")]

# test print
# print(columns)

# select every 11-th item (11 columns)
# 1-st column:    columns[0:][::11]
# 2-nd column:    columns[1:][::11]
# 3-rd column:    columns[2:][::11]
# ...

column_names = ["Founder",
                "Maintainer",
                "Initial_release_year",
                "Current_stable_version",
                "Security_updates_years",
                "Release_date",
                "System_distribution_commitment",
                "Forked_from",
                "Target_audience",
                "Cost",
                "Status"]

dictionary = {"Distribution": distribution}

for idx, key in enumerate(column_names):
    dictionary[key] = columns[idx:][::11]

df = pd.DataFrame(data = dictionary)
print(df)

# insert datat into database
connection = sqlite3.connect("linux_distro.db")
cursor = connection.cursor()
cursor.execute("create table linux (Distribution, " + ", ".join(column_names) + ")")

for i in range(len(df)):
    cursor.execute("insert into linux values (?,?,?,?,?,?,?,?,?,?,?,?)", df.iloc[i])

connection.commit()

connection.close()
