import requests
from bs4 import BeautifulSoup

class ScraperAgent:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception('Failed to fetch data')

    def parse_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # Parsing logic goes here
        data = []  # Example placeholder for parsed data
        for item in soup.find_all('div', class_='your-target-class'):
            data.append(item.text.strip())
        return data

    def run(self):
        print(f'Starting scraper for {self.url}')
        html = self.fetch_data()
        parsed_data = self.parse_data(html)
        print('Data fetched and parsed successfully!')
        return parsed_data

if __name__ == '__main__':
    scraper = ScraperAgent('https://magna.isa.gov.il/')
    data = scraper.run()
    print(data)