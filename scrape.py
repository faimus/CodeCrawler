# Issues that need looking into:

# 1. Initialization needs to be outside program loop
# oldPostings = []
# newPostings = []

# 1. Need to figure out how to keep oldPostings and newPostings consistent with URL selections
#  - While loop keeps executing for oldPostings == newPostings. Implying that loop breaks when there is a mismatch (or a new posting)


import requests
from bs4 import BeautifulSoup
import time 


# URLs based on categories
customerSupport = "https://weworkremotely.com/categories/remote-customer-support-jobs#job-listings"
contract = "https://weworkremotely.com/remote-contract-jobs#job-listings"
devOpsSysAdm = "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs#job-listings"

# Initialization needs to be outside program loop
oldPostings = []
newPostings = []

# Need to figure out how to keep oldPostings and newPostings consistent with URL selections
selection = input("Please Select a Category: \n1. Customer Support \n2. Contract \n3. DevOps & System Admin\n")

if selection == "1":
  url = customerSupport
elif selection == "2":
  url = contract
elif selection == "3":
  url = devOpsSysAdm
else:
  print ("Selection is Invalid")

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the <li> tags on the page and pick out class set as feature and <blank>
list_items = soup.find_all("li", {"class": ["feature", ""]})


# Find all the <a> tags within the <li> tags
for li in list_items:
  links = li.find_all("a")
  for link in links:
    if "/remote-jobs" in link.get("href"):
      site = "https://weworkremotely.com" + link.get("href")
      newPostings.append(site)

for item in newPostings:
  if item not in oldPostings:
    print (item)
  else:
    print ("No new postings found")

# for item in newPostings:
#   print(item) # Loops thro list and Prints 1 per line      

print ("\nNumber of New Postings: " + str(len(newPostings))) # Length of list gives the number of postings
print ("\nNumber of Old Postings: " + str(len(oldPostings))) # Length of list gives the number of postings

oldPostings = newPostings