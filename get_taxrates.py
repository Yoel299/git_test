""" 
    This code outputs the federal income tax rates and brackets
    which is scraped from the IRS web page.
"""
last_updated = "5/15/2024"

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.irs.gov/filing/federal-income-tax-rates-and-brackets'

r = requests.get( url )

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find_all('table', class_ = "table complex-table table-striped table-bordered table-responsive")

# Title for tables
year_soup = soup.find_all('div', class_ = "field field--name-body field--type-text-with-summary field--label-hidden field--item")[1]
year_txt = year_soup.find( 'h2' )
year = year_txt.text.strip().split()[0]

data_title = [
    f"{year} tax rates for \033[4ma single taxpayer\033[0m",
    f"{year} tax rates for \033[4ma married filing jointly or qualifying surviving spouse\033[0m",
    f"{year} tax rates for \033[4ma married filing separately\033[0m",
    f"{year} tax rates for \033[4ma head of household\033[0m",
]

# Scrape data for each table on website (four)
for i in range(len(table)):
    # Select corresponding table
    cur_table = table[i]

    col_titles = cur_table.find_all('th')
    col_table_titles = [ title.text.strip() for title in col_titles ]
    # print( col_table_titles )

    # Create empty dataframe
    df = pd.DataFrame(columns = col_table_titles)

    col_data = cur_table.find_all("tr")
    for row in col_data[1:]:
        row_data = row.find_all('td')
        indiv_row_data = [ data.text.strip() for data in row_data ]
        # print( indiv_row_data )
        
        # Input data in each row
        length = len(df)
        df.loc[length] = indiv_row_data

    print( data_title[i] )
    print( df )
    print()

# Print latest updated date
print( f"Last updated: {last_updated}")
