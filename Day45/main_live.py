from bs4 import BeautifulSoup
import requests

# Step 1: Fetch and parse the Hacker News page
yc_web_page = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(yc_web_page.text, 'html.parser')

# Step 2: Find all title spans and score spans
article_spans = soup.find_all('span', class_='titleline')
upvote_spans = soup.find_all('span', class_='score')

# Step 3: Store all articles in a list
articles = []

for index, span in enumerate(article_spans):
    a_tag = span.find('a')
    title = a_tag.getText()
    link = a_tag.get('href')

    try:
        score_text = upvote_spans[index].getText()
        score = int(score_text.split()[0])
    except IndexError:
        score = 0  # If there's no score, set it to 0

    articles.append({
        'title': title,
        'link': link,
        'upvotes': score
    })

# Step 4: Find and print the article with the most upvotes
top_article = max(articles, key=lambda article: article['upvotes'])

print(f"Top Article Title: {top_article['title']}")
print(f"Link: {top_article['link']}")
print(f"Upvotes: {top_article['upvotes']}")
