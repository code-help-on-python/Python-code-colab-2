import requests, random
from bs4 import BeautifulSoup

# List of Wikipedia URLs
urls = [
    "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population",
    "https://en.wikipedia.org/wiki/List_of_highest-grossing_films",
    "https://en.wikipedia.org/wiki/List_of_programming_languages",
    "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue",
    "https://en.wikipedia.org/wiki/List_of_tallest_buildings"
]

# Fetch a random URL
#url = random.choice(urls)
url = 'https://en.wikipedia.org/wiki/List_of_tallest_buildings'
r = requests.get(url)

# Parse HTML
soup = BeautifulSoup(r.text, 'html.parser')

# Extract paragraphs
paragraphs = soup.find_all('p')

# Clean and store text
cleaned_paragraphs = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
content = []
# Print the cleaned paragraphs
print(f"Extracted paragraphs from: {url}\n")
for i, para in enumerate(cleaned_paragraphs[:10], 1):  # Limit output to first 10 paragraphs
    content.append( f"{i}. {para}\n")

with open('info.txt', 'w') as f:
    f.writelines(i for i in content)
