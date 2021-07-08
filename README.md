# Aaj Ka Anand Newspaper Downloader
During this lockdown period many people were not recieving newspaper daily including my mother so I have developed a bot which returns a pdf file of daily AAJ-KA-ANAND Newspaper

# Modules / Libraries Used :closed_book:

1. BeautifulSoup
2. Requests
3. PyPDF2
4. URLopen
5. DateTime
6. os

# Procedure :biking_man:

- Checks If you are connected to internet
- Visits official Aaj ka Anand [Website](http://aajkaanand.epapers.in)
- Automatically updates the url to current date and page 1
- Downloads Page 1 of newspaper saves as a PDF file
- Updates the URL for next page and downloads all 17 pages of newspaper
- Once all pages are downloaded merges all pdf files into one file using [PyPDF2](https://pythonhosted.org/PyPDF2/) module
- Whole Newspaper File is saved on Desktop

# Improvements you can do :blush:

- Always open for more easy way of approach for a problem
- All 17 pages are not deleted can write a script to delete files after all are merged

# THANK YOU :v:
