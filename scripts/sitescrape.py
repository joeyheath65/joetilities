import requests
from bs4 import BeautifulSoup
import csv
import time
import os

os.system('clear')

# copy and paste this in the header of each script
print()
print("        ********************************************************************\n"
      "        **                                                                **\n"      
      "        **            W E L C O M E  TO  J O E T I L I T I E S!           **\n"
      "        **                                                                **\n"
      "        **               This Joetility is the Web Scraper!!              **\n"
      "        **                                                                **\n"
      "        ********************************************************************\n")
print()
# since you're forgetful, add this note to each script tellling what it does bruh
print("        ******                --> USAGE  NOTE <--                     ******\n"
      "        * This Joetility prompts the user for a URL to scrape and send the *\n"
      "        * output to a csv file, which the user gets to name!               *\n"
      "        *                                                                  *\n")

time.sleep(3)

# URL of the webpage to scrape
url = input('\nPlease enter a valid and SPECIFIC URL to scrape: ')  # User enters URL

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the data you want from the HTML (example: extracting all <a> tags)
    links = soup.find_all('a')

    # Create a list to hold the data
    data = []

    for link in links:
        # Extract the text and href attribute of each <a> tag
        link_text = link.get_text()
        link_href = link['href']

        # Add the data to the list
        data.append([link_text, link_href])

    # Define the CSV file name
    filename = input('\nWhat would you like to name this file?: ')
    file_ext = 'csv'
    csv_file_name = (filename + '.' + file_ext)
      
    
    # Write the data to a CSV file
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header row (optional)
        csv_writer.writerow(['Link Text', 'Link Href'])
        # Write the data rows
        csv_writer.writerows(data)

    print(f'Data has been scraped and saved to {csv_file_name}')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
