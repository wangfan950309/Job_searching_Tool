from web_scraping.scraping import *
import requests
from tqdm import tqdm

def search_job(data):
    s = 0
    f = 0
    target_company = data['Company_Name'].tolist()
    df = pd.DataFrame(columns=['Job_Name', 'Company_Name', 'Job_Location', 'Job_link'])
    for company in tqdm(target_company):
        company = company.replace('Canada','')
        company = company.strip()
        url = 'https://www.linkedin.com/jobs/search/?keywords={}&location=Toronto%2C%20Canada%20Area&locationId=ca%3A4876'.format(company)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
 #       print(soup.prettify())
        container = soup.find('ul',class_='jobs-search__results-list')
#        print(container)
        try:
            job_list = container.find_all('li')

            for job_list in job_list:
                try:
                     job_name = job_list.a.span
                     job_company = job_list.div.h4.a.text
                     job_location = job_list.div.div.span
                     job_link = job_list.a['href']
                except:
                    f = f+1
                 #   print('Cant reach a proper page for %s' % company)

                else:
                 #   print('successfully parsed %s' % company)
         #        if job_company.lower() == company.lower():
                    s = s+1
                    df = df.append({'Job_Name': job_name.text,
                                     'Company_Name': job_company,
                                     'Job_Location': job_location.text,
                                     'Job_link': job_link}, ignore_index=True)
        except:
            pass
    print('Successfully searched and parsed %s jobs where %s failures accrued' % (s, f))
    return df





if __name__ == '__main__':
    path = os.getcwd()
    path = os.path.abspath(os.path.join(path, '..'))
#    os.makedirs('%s/data' % path)
    data = pd.read_csv('%s/data/ranking_list.csv' % path)
    new_df = search_job(data)
    new_df.to_csv('%s/data/Job_search.csv' % path, index=False)


















