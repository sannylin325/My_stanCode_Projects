"""
File: webcrawler.py
Name: Sanny Lin
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Print the number of top200 male and female on Console.
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'

        with webdriver.Chrome() as driver:
            driver.get(url)
            try:
                element_present = EC.presence_of_element_located((By.ID, 'specific-element-id'))
                WebDriverWait(driver, 5).until(element_present)
            except TimeoutException:
                print("Timed out waiting for page to load")
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, features="lxml")

            # calculate
            male_total = 0
            female_total = 0

            tags = soup.find_all('table', {'class', 't-stripe'})
            for tag in tags:
                text = tag.tbody.text.split()
                for i in range(len(text) - 22):
                    if i % 5 == 2:  # male
                        male_total += int(text[i].replace(',', ''))
                    elif i % 5 == 4:  # female
                        female_total += int(text[i].replace(',', ''))

            print('Male Number:', male_total)
            print('Female Number:', female_total)


if __name__ == '__main__':
    main()
