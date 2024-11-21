import os
import requests
from bs4 import BeautifulSoup

base_url = 'https://metanit.com/cpp/tutorial/'

def get_subpage_links(base_url):
    response = requests.get(base_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.menT a')  
    subpage_links = [base_url + link['href'] for link in links if link['href'].startswith('1.')]
    return subpage_links

def parse_and_save(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    code_block = soup.find('div', class_='item center menC')
    
    if code_block:
        code_html = str(code_block)
        file_name = url.split('/')[-1].replace('.php', '.html')
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(code_html)
        print(f"Код сохранен в файл '{file_name}'")
    else:
        print(f"Блок  не найден на {url}")

subpage_links = get_subpage_links(base_url)

if not os.path.exists('extracted_codes'):
    os.makedirs('extracted_codes')

os.chdir('extracted_codes')

for link in subpage_links:
    parse_and_save(link)
