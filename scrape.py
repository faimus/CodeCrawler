import requests
from bs4 import BeautifulSoup

# URLs based on categories
customerSupport = "https://weworkremotely.com/categories/remote-customer-support-jobs#job-listings"
contract = "https://weworkremotely.com/remote-contract-jobs#job-listings"
devOpsSysAdm = "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs#job-listings"

# URL of the website you want to scrape
url = contract

# Send a GET request to the URL
kresponse = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the <li> tags on the page
list_items = soup.find_all("li", {"class": ["feature", ""]})

count = 0
oldPostings = []
newPostings = []

# Find all the <a> tags within the <li> tags
for li in list_items:
  links = li.find_all("a")
  for link in links:
    if "/remote-jobs" in link.get("href"):
      site = "https://weworkremotely.com" + link.get("href")
      newPostings.append(site)

for item in newPostings:
  print(item) # Loops thro list and Prints 1 per line      
print ("\nNumber of Postings: " + str(len(newPostings))) # Length of list gives the number of postings