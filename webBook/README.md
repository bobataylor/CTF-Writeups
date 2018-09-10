# Web Book
A 75 point problem from <a href="https://www.hackerrank.com/codefest-ctf-18">Codefest CTF 2018</a>


"It is expected to complete reading a book/novel to pass the course, but the students being clever avoid reading the whole book by going through the summary only. 
Santosh(their course teacher) comes up with a new idea, he creates a magic book (you can only go to next page, that is: you can't go to next page without reading the previous one and so on, and you can only start from the beginning). 
It is know that the flag is hidden somewhere in the book, so the only way to pass the course is to read the whole book, find the flag. The book has 1000 pages so better be fast. And if you are lucky, you may even find the key on the very first page itself."

The problem statement above then links the player to <a href="http://34.216.132.109:8083/fp/">http://34.216.132.109:8083/fp/</a>

This problem was nothing more than a scripting exercise, but it was new to me in that I had to find a way to actually click the ```Next``` button. Simply going to the page the button pointed to would result in a ```Not authorized``` message.

In order to click the button I used Selenium to find the button element, click it, read the text off the page, check for a flag, then continue.
``` python
from selenium import webdriver

web_base = "http://34.216.132.109:8083"

driver = webdriver.Firefox()
driver.get(web_base + '/fp/')
 
# click radio button
button = driver.find_elements_by_xpath("html/body/form/button")[0]
button.click()
 
# get text
text = driver.find_elements_by_xpath("html/body")[0].text

with open('data.txt', 'w') as file:
	while "CTF{" not in text:
		file.write(text)
		button = driver.find_elements_by_xpath("html/body/form/button")[0]
		button.click()
		text = driver.find_elements_by_xpath("html/body")[0].text

print(text)
```
I ended up printing to the file because the script was failing to stop on the flag page, turned out the flag was not in the standard ```codefestCTF{FLAG}``` format. Searching through the file I tried matching on `_` and got the flag.