import nltk
from nltk.tokenize import sent_tokenize
nltk.download()
with open('dusty.txt', 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
sent_tokenize_list = sent_tokenize(data)
print(sent_tokenize_list)
