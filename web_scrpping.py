# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin 

# def fetch_links(url= "https://books.toscrape.com", links= []):
#     r = requests.get(url)
#     print(r.url, flush=True)
#     soup = BeautifulSoup(r.text, "html.parser")
#     for link in soup.select("h3 a"):
#         links.append(urljoin(url, link.get("href")))
#     next_page = soup.select_one("li.next a")
#     if next_page:
#         return fetch_links(urljoin(url, next_page.get("href"), links))
#     else:
#         return links
    
# def refresh_links():
#     links = fetch_links()
#     with open('links.csv', 'w') as f:
#         for link in links:
#             f.write(link + '\n')

# refresh_links()


import csv
import re
import time
import requests

def get_links():
	links = []
	with open("links.csv", "r") as f:
		reader = csv.reader(f)
		for i, row in enumerate(reader):
			links.append(row[0])
	return links

def get_response(session, url):
	with session.get(url) as resp:
		print('.', end='', flush=True)
		text = resp.text
		exp = r'(<title>).*(<\/title>)'
		return re.search(exp, text, flags=re.DOTALL).group(0)

def main():
	start_time = time.time()
	with requests.Session() as session:
		results = []
		url= "https://books.toscrape.com"
		for url in get_links():
			result = get_response(session, url)
			print(result)
	print(f"{(time.time() - start_time):.2f} seconds")


main()
