import feedparser, time

URL = "https://ehddud100677.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
### Hi there 👋
My name is **DongYoung**, major in **computer science**💻 since 2017 at **Pusan National University** in Pusan, South Korea.  
**Front-end developer**, write code with **react & typescript**.

Blog | [https://ehddud100677.tistory.com/](https://ehddud100677.tistory.com)

### ✏️ My latest posts
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()