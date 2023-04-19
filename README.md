# Remote Job Postings Scraper

This Python script scrapes remote job postings from [https://weworkremotely.com](https://weworkremotely.com) based on selected categories: Customer Support, Contract, and DevOps & System Admin.

## Issues to Look Into

1. Initialization needs to be outside the program loop to prevent resetting of `oldPostings` and `newPostings` in each iteration.
2. Need to figure out how to keep `oldPostings` and `newPostings` consistent with URL selections. The while loop currently keeps executing as long as `oldPostings` and `newPostings` are the same, implying that the loop breaks when there is a mismatch or a new posting is found.

## Dependencies

The following Python libraries are required to run this script:

- requests
- BeautifulSoup

You can install the dependencies using pip:
```
pip install requests
pip install beautifulsoup4
```

## Usage

1. Run the script in a Python environment.
2. Select a category by entering the corresponding number:
```
Please Select a Category:

1. Customer Support
2. Contract
3. DevOps & System Admin
```

3. The script will scrape remote job postings from the selected category and print out the URLs of the new postings.
4. The number of new postings and the number of old postings will be displayed at the end of the output.
5. The `oldPostings` list will be updated with the URLs of the new postings for future comparison.

Note: The URLs of the job postings are printed one per line.

## Future Improvements

1. Move the initialization of `oldPostings` and `newPostings` outside the loop to prevent resetting in each iteration.
2. Implement a mechanism to keep `oldPostings` and `newPostings` consistent with URL selections to improve the accuracy of identifying new postings.
3. Add error handling for cases where the website structure or URL format changes.
4. Consider adding options to filter or sort job postings based on additional criteria such as location, job type, etc.
