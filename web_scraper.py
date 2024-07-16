#this program will scrape information from a stocks site and give the data as an excel file
import sys
import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL, timeout=20)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_info=results.find_all("div", class_="card-content")
#create arrays to store each of these data
job_location_array=[]
job_company_array=[]
job_title_array=[]
link_url_array=[]

#now run a for loop to check for the particular info and save it in the array needed
for job_info in job_info:
    job_title=job_info.find("h2", class_="title is-5").text.strip()
    job_company=job_info.find("h3", class_="subtitle is-6 company").text.strip()
    job_location=job_info.find("p", class_="location").text.strip()
    link_url= job_info.find_all("a")[1]["href"]
    job_title_array.append(job_title)
    job_company_array.append(job_company)
    job_location_array.append(job_location)
    link_url_array.append(link_url)

#create a dataframe in excel where the information would be stored 
df = pd.DataFrame(
    {
        'Job Titles': job_title_array,
        'Company': job_company_array,
        'Location': job_location_array,
        'Apply Here': link_url_array
    }
)
output_file= r'C:\Users\TUBORR\Desktop\WEB3 DEV JOURNEY\PYTHON\Exercises\Web-Scraper/Jobs-Scraped.xlsx'
#now that the data frame and excel file has been created, write the information into the excel file
try:
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Jobs-Scraped', index=False)
    print (f"Data Set has been scraped successfully into '{output_file}'  Thank You.")
except Exception as e:
    print(f"An Error occurred when trying to store Data: {e}")
    
