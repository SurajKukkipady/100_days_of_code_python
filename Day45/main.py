from bs4 import BeautifulSoup

with open('website.html', 'r') as file:
    contents = file.read()
#print(contents)

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
# print(soup.prettify())

print(soup.a)  # First <a> tag
all_anchor_tags = soup.find_all('a')  # All <a> tags
#print(all_anchor_tags)  # All <a> tags

#for tag in all_anchor_tags:
    #print(tag.getText())  # Print the href attribute of each <a> tag
    #print(tag.get('href'))  # Print the href attribute of each <a> tag


heading = soup.find(name='h1', id='name')
print(heading)
section_heading = soup.find(name='h3', class_='heading')
print(section_heading)

company_url = soup.select_one(selector='p a')
print(company_url)

heading = soup.select(".heading") 
print(heading)


