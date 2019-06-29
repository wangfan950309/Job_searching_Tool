# Web_Scraping
A Tool that scrape the data from BestWorkPlace website and search all the companies from the list on Linkedin Job page and save all the job from those companies into an excel file for a better and easier view.

### Setup

```python
python setup.py build
python setup.py install
```

### Functional

1. Parse all the best-to-work companies from BestWorkPlace web page and save it as an excel and the data will be stored in **data** folder:
```python
python web_scraping/web_scraping.py
```
2. Read all company name and search on Linkedin and save the job details and save it as an excel and the data will be stored in **data** folder:
```python
python web_scraping/Job_searching.py
```

### Items to Work On

1. Simulate/ Having the action of click on next page and then parse further pages.
2. Remove unrelated/incorrect search results.
