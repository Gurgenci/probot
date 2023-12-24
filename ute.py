import requests
from bs4 import BeautifulSoup

TEST=False
SEP="-+-+-+-+"

# The following function is used to get the content of a web page
# The `url` is the URL address and the `filename` is the name of the file to save
# Remove all HTML tags and save the content to the file
def rdweb(url, filename):
    # Get the content of the web page
    r = requests.get(url)
    # Parse the content of the web page
    soup = BeautifulSoup(r.content, "html.parser")
    # Get the text of the web page
    text = soup.get_text()
    # Save the text to the file
    save=(not filename==None)
    if save:
        with open(filename, "w") as f:
            f.write(text)
    return text

if TEST:
    (url1, filename1)="https://halimgur.substack.com/p/the-requiem-for-a-dream-israels-untaken", "data/requiem.txt"
    sep="-+-+-+-+"
    text=rdweb(url1, filename1, save=False)

# The following function takes a text string `text` and separates it to a list
# of strings using the separator `sep`
def sepstr(text, sep):
    # Split the text to a list of strings
    lst=text.split(sep)
    # Remove the empty strings
    lst=[s for s in lst if s]
    # Remove the first string
    lst=lst[1:]
    return lst

if TEST:
    sa=sepstr(text, SEP)
    for (i, s) in enumerate(sa):
        print("Section %d\n" % (i+1))
        print(s)
        print()

# Establish OpenAI API key (see below for how to get one)
import os
import openai
from openai import OpenAI
import numpy as np
Client=None
LLM=None
def set_openai_key():
    global Client, LLM
    openai.api_key = os.getenv("OPENAI_API_KEY")
    Client = OpenAI()
    LLM="text-embedding-ada-002"

# Generate the embedding for the text
def get_embedding(text):
    global Client, LLM
    if Client==None:
        set_openai_key()
    response = Client.embeddings.create(
        input=text,
        model=LLM
    )
    return np.array(response.data[0].embedding)

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
