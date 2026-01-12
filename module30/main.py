from bs4 import BeautifulSoup
#metoda find()
element = soup.find(name,attrs,recursive,string,**kwargs)

first_Link =soup.find('a')

#metoda find_all
element = soup.find_all(name,attrs,recursive,string,**kwargs)
all_Links= soup.find_all('a')

#metoda select
elements= soup.select(selector)


example=soup.select('.example')

#metoda get_text()
text = element.get_text(seperator,strip)

text = element.get_text()

#metoda attrs

Attribute = element.attrs

link = soup.find('a')
href = link.attrs['href']

parent = element.parent
parents = element.parents

parent = element.parents
children = element.children
descendants = element.descendants
