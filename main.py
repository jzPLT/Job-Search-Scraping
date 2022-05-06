from bs4 import BeautifulSoup
import requests

url = 'https://www.wantedly.com/projects?type=mixed&page=1&occupation_types%5B%5D=jp__marketing&hiring_types%5B%5D=mid_career&hiring_types%5B%5D=newgrad'


while(url):

    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')

    jobs = soup.find_all('div', class_ ='project-index-single-outer')

    for job in jobs:
        title = job.find('h1', class_ = 'project-title').text
        description = job.find('p', class_ = 'project-excerpt').text

        if '営業' not in title and '営業' not in description:

            company_name = job.find('div', class_ = 'company-name').find('h3').text
            tags = job.find('div', class_ = 'project-tag small normal').text.replace('\n', '')
            type = job.find('div', class_ = 'project-tag small inverted').text
            more_info = 'https://www.wantedly.com' + job.find('h1', class_ = 'project-title').find('a')['href']

            print(f"Company name: {company_name.strip()}")
            print(f"Tags: {tags.strip()}")
            print(f"Type: {type}")
            print(f"Description: {description}")
            print(f"More Info: {more_info}")
            print("\n")


    url = soup.find('div', class_ = 'project-index-pagination').find('a', {'rel': 'next'})

    print(url)

    if(url):
        url = 'https://www.wantedly.com' + url['href']
    else:
        break
