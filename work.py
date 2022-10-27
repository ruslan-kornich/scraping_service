import requests
import codecs
from bs4 import BeautifulSoup

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'}

url = 'https://www.work.ua/jobs-dnipro-python/'
resp = requests.get(url, headers=headers)
jobs = []
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, 'html.parser')
    main_div = soup.find('div', id='pjax-job-list')
    div_list = main_div.find_all('div', attrs={'class': 'job-link'})
    for div in div_list:
        title = div.find('h2').text
        job_url = 'https://www.work.ua' + str(div.find('h2').find('a').get('href'))
        content = div.p.text
        company = div.find('div', class_='add-top-xs').find('span').text
        #city = div.find('div', class_='add-top-xs').find_all('span')[-1].text

        jobs.append({'title': title, 'url': job_url, 'description': content, 'company': company})

    print(jobs)