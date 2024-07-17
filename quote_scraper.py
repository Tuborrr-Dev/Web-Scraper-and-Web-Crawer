import sys
import pandas
import pandas as pd
from bs4 import BeautifulSoup
import requests

#this program will crawl through the different pages of a site and scrape the data from each page
#And save to an excel file
counter=0
i=0
url = 'http://quotes.toscrape.com'
url_list=[url, ]
html_pages=[]
parsed_pages=[]
not_last_page=True
#first decorator to get the last url from the url lsit and load up the page and save the page
def process_url(function):
    def url_processor(*args, **kwargs):
        #in this inner function we have to first confirm that there are urls in the lst
        if url_list==None:
            print("There are no URLS present in the list")
            return
        url=url_list[-1]
        page= requests.get(url, timeout=50)
        if page.status_code==200:
            html_pages.append(page)
            function(*args, **kwargs)
        else:
            print(f"Connection was Unsuccessful with {url} with error code {page.status_code}")
        
    return url_processor
#the second decorator now parses the page that was just appended 
def parser(function):
    def page_parser(*args, **kwargs):
        #here the page is parsed using beautiful soup 
        if html_pages==None:
            print ("There are no pages available to be parsed")
            return 
        else:
            last_page_forparsing=html_pages[-1]
            soup = BeautifulSoup(last_page_forparsing.content, "html.parser")
            parsed_pages.append(soup)
            function(*args, **kwargs)
    return page_parser
#now that we have parsed the page we can go ahead and search for the element containing the link for next page

@process_url
@parser
def search_for_nxtpg():
    global not_last_page
    #now we search for the next page element
    try:
        if not parsed_pages:
            print("No parsed pages available")
            not_last_page = False
            return
        
        last_parsed_page = parsed_pages[-1]
        next_page_element = last_parsed_page.find('li', {'class': 'next'})
        
        if next_page_element:
            nxtpg_link = next_page_element.find('a')['href']
            nxtpg_url = url + nxtpg_link
            print(f"This page URL is: {nxtpg_url}")
            url_list.append(nxtpg_url)
        else:
            print("No 'next' element found. Ending search.")
            not_last_page = False
    except AttributeError:
        print("Error: No 'next' element found in the parsed HTML.")
        not_last_page = False
    except Exception as e:
        print(f"An error occurred: {e}")
        not_last_page = False
while not_last_page==True:
    search_for_nxtpg()
    counter+=1
print(counter)
#now that we have all the URL in our list
#we need a loop to scrape the data of each site


quotes = []
authors = []

    
#this time around we try to use the parsed soup data in the extraction instead of going through
#each of the URL again
while i < counter:
    present_page_frmParser=parsed_pages[i]
    try:
        cards = present_page_frmParser.find_all('div', class_ = 'quote')
        for card in cards:
            quote = card.find('span', class_='text').text
            author = card.find('small', class_='author').text
            quotes.append(quote)
            authors.append(author)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred fetching {present_page_frmParser}: {e}")
    except Exception as e:
        print(f"An error occurred processing {present_page_frmParser}: {e}")
    i += 1
    
    

# Create a DataFrame to store scraped data
df = pd.DataFrame({
    'QUOTES': quotes,
    'AUTHORS': authors
})

# Define the output file path for Excel
output_file = r'C:\Users\TUBORR\Desktop\WEB3 DEV JOURNEY\PYTHON\Exercises\Web-Scraper\Quotes-Scraped.xlsx'

# Write DataFrame to Excel
try:
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Quotes-Scraped', index=False)
    print(f"Data set has been scraped successfully into '{output_file}'. Thank you.")
except Exception as e:
    print(f"An error occurred when trying to store data: {e}")



