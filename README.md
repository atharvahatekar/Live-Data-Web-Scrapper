## Live Data Web Scrapper

developed a web scraper that able to collect live transaction data from the `https://www.primeopinion.com/` site.
It helps to track the live payout feed at the top of the page, outlined in the image below in orange.

![alt text](feed.png "Feed")

For each payout appearing in the feed, I stored the following information:
- Name of the payout provider e.g. *"PayPal"*
- The amount of currency earned e.g. 10.0
- The kind of currency, e.g. *"USD"* or *"EUR"*
- A timestamp in isoformat, marking the time the information was parsed

```
# example structure of a data entry
"PayPal", 10.0, "US", "2024-06-11T15:52:30.127535+00:00"
```

The stored in a local file (.csv) in the format described above.

## tools Used

[selenium web driver](https://www.selenium.dev/documentation/webdriver/getting_started/), there are implementations for 
python, java and other languages that are quite convenient to use, although I use python since that is what 
I am currently working on. <br>

