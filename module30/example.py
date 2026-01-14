
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9",
    }

def get_page_content(url):
    response = request.get(url,headers)
    if response.status_code == 200:
        return response.content
    return None

def extract_article(content):
    soup = BeautifulSoup(content, 'html.parser')

    articles = []

    for article in soup.find_all('div', class_='search-item'):
        title_div = article.find('div', class_='search-txt')

        title = 'No title found'
        link = 'No link found'
        date = 'No date found'
        description = 'No description found'

        if title_div:
            title_tag = title_div.find('a')
            if title_tag:
                title = title_tag.get_text(strip=True)
                link = title_tag['href']

            meta_ul = title_div.find('ul', class_='story-meta')
            if meta_ul:
                date_li = meta_ul.find_all('li')[0]
                if date_li:
                    date = date_li.get_text(strip=True)

        description_tag = article.find('p')
        if description_tag:
            description = description_tag.get_text(strip=True)

        articles.append({
            'title': title,
            'link': link,
            'date': date,
            'description': description
        })

    return articles


