import requests
from bs4 import BeautifulSoup #This is the beautifulsoup4 module that was installed early

response = requests.get("https://stackoverflow.com/questions")
#print(response.text) #text returns the HTML content in the Webpage
soup = BeautifulSoup(response.text,"html.parser") #Here we create a beautiful soup object and pass the HTML content
                             #As second argument we are going to pass the type parsam in the HTML file(parse) 

#This soup object mirrors the structure of out HTML content, so we ca easily navigate this document and find various elements.

# Now we are going to use soup to find things
questions = soup.select(".s-post-summary--content-title") # This returns a list and works as css selector
print(questions[0].select(".s-link")) #We use select to find another css class from the class
                                      #we already use. This will return an array

print(questions[0].select_one(".s-link")) #Only returns one element

#The next step is to get the actual text (the title)
print(questions[0].select_one(".s-link").getText()) #It'ss used to return the text inside the ancher

#Now we are going to iteratiate in each of the questions to get their title.
for question in questions:
    print(question.select_one(".s-link").getText()) 

#Get number of votes in each question
votes = soup.select(".s-post-summary--stats-item-number")
print(votes)

for vote in votes:
    print(vote.getText())