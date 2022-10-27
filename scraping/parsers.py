import requests
import codecs
from bs4 import BeautifulSoup
from random import randint


__all__ = ('work', 'dou', 'djinni')

headers = [{
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8',
},
    {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8',
    },
    {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8',
    }
]


def work(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://www.work.ua'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            div_list = main_div.find_all('div', attrs={'class': 'job-link'})
            for div in div_list:
                title = div.find('h2').text
                job_url = 'https://www.work.ua' + str(div.find('h2').find('a').get('href'))
                content = div.p.text
                company = div.find('div', class_='add-top-xs').find('span').text
                jobs.append({'title': title, 'url': job_url,
                             'description': content, 'company': company})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors


url = 'https://jobs.dou.ua/vacancies/?city=%D0%94%D0%BD%D1%96%D0%BF%D1%80%D0%BE&category=Python'


def dou(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            main_div = soup.find('div', id='vacancyListId')
            if main_div:
                li_list = main_div.find_all('li', attrs={'class': 'l-vacancy'})
                for li in li_list:
                    title = li.find('div', attrs={'class': 'title'}).a.text
                    job_url = li.find('div', attrs={'class': 'title'}).find('a').get('href')
                    content = li.find('div', attrs={'class': 'sh-info'}).text
                    company = li.find('div', attrs={'class': 'title'}).find_all('a')[1].text.strip()
                    jobs.append({'title': title, 'url': job_url,
                                 'description': content, 'company': company})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors


def djinni(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            main_ul = soup.find('ul', attrs={'class': 'list-jobs'})
            if main_ul:
                li_lst = main_ul.find_all('li', attrs={'class': 'list-jobs__item'})
                for li in li_lst:
                    title = li.find('div', attrs={'class': 'list-jobs__title'}).find('span').text
                    job_url = 'https://djinni.co' + li.find('div', attrs={'class': 'list-jobs__title'}).find('a').get(
                        'href')
                    content = li.find('div',
                                      attrs={'class': 'list-jobs__description'}).text

                    company = li.find('div',
                                      attrs={'class': 'list-jobs__details__info'}).find('a').text.strip()
                    jobs.append({'title': title, 'url': job_url,
                                 'description': content, 'company': company})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors


if __name__ == '__main__':
    url = 'https://djinni.co/jobs/?location=%D0%9A%D0%B8%D0%B5%D0%B2&primary_keyword=Python'
    jobs, errors = djinni(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()

