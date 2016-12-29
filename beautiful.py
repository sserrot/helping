from bs4 import BeautifulSoup


soup = BeautifulSoup(open("test_html.html"), "html.parser")

text = soup.find_all('p') # list of p tags

# lets create a giant string of our p tags with just the text

giant_string = ''
i = 0
while i < len(text):
    giant_string = giant_string + text[i].text
    i += 1

print(giant_string.encode('utf-8'))

