import requests
from bs4 import BeautifulSoup 
from selenium.webdriver import Chrome, ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def get_page_source(url, headers):
    exec_path = ChromeDriverManager().install()
    service = ChromeService(executable_path=exec_path)
    with Chrome(service=service) as driver:
        driver.get(url=url)
        sleep(10)
        driver.find_element(By.XPATH, r'/html/body/div[1]/div[2]/div/div[2]/div/button').click()
        sleep(3)
        while True:
            try:
                driver.find_element(By.XPATH, r'/html/body/div[5]/div/div/div/div[1]/button').click()
                break
            except Exception as e:
                continue
        sleep(3)
        file_path = "C:\\Users\\luan_\\vscode-projects\\100days-of-dsa\\pages\\index.html"
        with open(file_path, 'w', encoding='utf8') as f:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            print(soup.prettify(), file=f)
            print('terminei')

def get_problem_params(file_path):
    with open(file=file_path, mode='r', encoding='utf8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        return {
            'title': soup.title.get_text().strip(), 
            'description': \
                soup.find('meta', {'name':"description"})['content']\
                    .removeprefix('Can you solve this real interview question?')\
                        .strip()
        }

def set_readme(file_path):
    params = get_problem_params(file_path) 
    with open('pages\\README.md', 'w', encoding='utf8') as f:
        print(f"# {params['title']}", file=f)
        print(f'{params['description']}', file=f)

def main():
    # url = 'https://leetcode.com/problems/two-sum/'
    url = 'https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/'
    headers = {'User-Agent':'Mozilla/5.0'} 
    f_path = "C:\\Users\\luan_\\vscode-projects\\100days-of-dsa\\pages\\index.html"
    set_readme(f_path)
    
if __name__ == '__main__':
    main()