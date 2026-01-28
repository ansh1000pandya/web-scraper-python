import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.text

print("Page Title:")
print(title)

headings = soup.find_all("h1")


print("\nHeadings: ")
for h in headings:
    print(h.text)