#proj2.py
import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse 
import re

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
first_ten_headings=[]
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        first_ten_headings.append(story_heading.a.text.replace("\n", " ").strip())
    else: 
        first_ten_headings.append(story_heading.contents[0].strip())
for ahead in first_ten_headings[:10]:
	print(ahead)








#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url = 'https://www.michigandaily.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for ol in soup.find_all("div",class_="view-most-read"):
	for li in ol.find_all("li"):
		print(li.a.text)
	









#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here

base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
img=soup.find_all("img")
# print(img)
for a_img in img:
	alt_text=a_img.get("alt")
	if alt_text!= None:

		print(alt_text)
	else:
		print("No alternative text provided!!")







#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
page=0
count=1

emails=[]
contact_links=[]
for i in range(0,7):
	page_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4&page='+str(page)
	r1 = requests.get(page_url,headers={'User-Agent': 'SI_CLASS'})
	soup1 = BeautifulSoup(r1.text, "html.parser")
	for contact in soup1.find_all("a", text="Contact Details"):
		contact_links.append("https://www.si.umich.edu"+contact.get("href"))
	page+=1


#print (len(contact_links))
for a_prof in contact_links:
	r2 = requests.get(a_prof,headers={'User-Agent': 'SI_CLASS'})
	soup2 = BeautifulSoup(r2.text, "html.parser")
	for email in soup2.find_all('a',href=re.compile('mailto:')):
		emails.append(str(count)+" "+email.get_text())
	count+=1

for email in emails:
	print(email)
	


			

