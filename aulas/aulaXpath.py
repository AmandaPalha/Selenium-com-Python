from parsel import Selector

with open('index.html') as f:
    content = f.read()

response = Selector(text=content)

response.xpath("/html/head")

print(response.xpath("/html/head").get())
