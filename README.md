# Job_Searching_Tool
A Tool that scrape all the best place to work from [BestWorkPlace](https://www.greatplacetowork.ca/en/best-workplaces/best-workplaces-in-canada-2019-1000-employees) website and search all the companies from the list on Linkedin Job page and scraping all the open positions and save as an excel file. The Tool will also include a searching web application that enable to search job on certain keywords from the web scraping results (Open Job positions).


### Demo:
* Main Page:
![image]('https://github.com/wangfan950309/Job_searching_Tool/tree/master/pic/main_page.PNG')

* Search Results:
![image]('https://github.com/wangfan950309/Job_searching_Tool/tree/master/pic/search_results_sample.PNG')

### Setup
* Driver Setup:
[install ChromeDriver](http://chromedriver.chromium.org/) 
* Python Setup:

```python
pip install -r requirements_dev.txt
python setup.py build
python setup.py install
```

### Functional
* Scraping best company to work

 Parse all the best-to-work companies from BestWorkPlace web page and save it as an excel and the data will be stored in **data** folder:
```python
python web_scraping/scraping.py
```
* Searching all companies from Linkedin and scraping all the opening positions

Read all company name and search on Linkedin and save the job details and save it as an excel and the data will be stored in **data** folder:
```python
python web_scraping/Job_searching.py
```

* Search jobs on keywords

Run the below code, use the URL output in an internet browser to use the searching tool
```python
set FLASK_APP=app.py
python app.py
``` 

### Items to Work On

1. Simulate/ Having the action of click on next page in Linkedin and then parse further pages (Perhaps use Linkedin API).
2. Remove unrelated/incorrect company search results.
3. Display full job link in searching results and enable the hyperlink functionality
