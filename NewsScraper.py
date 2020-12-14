import requests;
from bs4 import BeautifulSoup;

def scrapeNews():
    #URL of the web page to be scraped for content.
    URL = "https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html";

    #Using the requests API's get method to retrieve the content in the webRequest variable. 
    webRequest = requests.get(URL);

    #Creates a bs4 variable that parses the html content into the tree structure of the soup variable.
    soup = BeautifulSoup(webRequest.content, 'html.parser');

    #Using list comprehension, the story variable will search through the tags and and find all the tags
    #that use the css class css-158dogj.  Once these elements are found, the text is extracted from within
    #the tags and added to the story variable in a list.  
    return [p.text for p in soup.find_all("p", {"class": "css-158dogj"})];


def createTextFile():
    #Catches the list of text data created by the scrapeNews function
    story = scrapeNews();
    #Creates and opens a new text file called NYTimesOpEd.txt to write to.
    articleFile = open('NYTimesOpEd.txt', 'w');

    #Iterates through the story list and writes each line to the text file.
    for p in story:
        articleFile.write(p);
        articleFile.write('\n');

    #Closes the text file.
    articleFile.close();

    #Displays a message that lets the user know the program executed correctly.
    print('Success!');

createTextFile();



