# Tutorial Project - Crawling with Scrapy

## 2 spiders - fundrazr_scrape and SportsDirect
  1. Scraping https://fundrazr.com/ and saving the scraped data as a CSV file. Tutorial source: https://youtu.be/O_j3OTXw2_E
  2. Scraping https://www.sportsdirect.com/ and saving the scraped product data as a JSON file and downloading 
     specifc product image files. Tutorial source: https://youtu.be/4I6Xg6Y17qs

# Install
```
pip install -r requirements.txt
```

# Running the crawlers/spiders

###### FundRazr spider 
From the FundRazr directory run the following command:
```
scrapy crawl FundRazr -o <filename>.csv
```

###### SportsDirect spider 
From the simple_crawler directory run the following command:
```
scrapy crawl sportsdirect --set FEED_URI=<filename>.jl
```


# Output

###### FundRazr spider 
![Alt text](screens/fundrazr_screen.png?raw=true "FundRazr csv")

###### SportsDirect spider 
![Alt text](screens/sportsdirect_screen.png?raw=true "SportsDirect JSON")
![Alt text](screens/sportsdirect_screen2.png?raw=true "SportsDirect Downloads")
