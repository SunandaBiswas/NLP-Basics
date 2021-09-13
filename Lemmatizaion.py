### Lemmatization: A technique that is used to reduce words to the root form. The Stemming method is used for this purpose as well but Lemmatization is used to extract meaningful words. 
## The process of lemmatization is more time consuming than stemming. Basically, it is applied to build chatbots, as meaningful response is important there.


#importing necesssary libraries
import nltk
from nltk.stem import WordNetLemmatizer  #for lemmatiization
from nltk.corpus import stopwords

paragraph = """Humans live out their own lives effectively trapped in their own mind and, despite being exceptional survivors and a highly social species, our inner mental world is often misaligned with reality. In order to understand why, John Edward Terrell and Gabriel Stowe Terrell suggest current dual-process models of the mind overlook our mind’s most decisive and unpredictable mode: creativity. Using a three-dimensional model of the mind, the authors examine the human struggle to stay in touch with reality—how we succeed, how we fail, and how winning this struggle is key to our survival in an age of mounting social problems of our own making.

Using news stories of logic-defying behavior, analogies to famous fictitious characters, and analysis of evolutionary and cognitive psychology theory, this fascinating account of how the mind works is a must-read for all interested in anthropology and cognitive psychology."""
               
#sentence tokenizaion               
sentences = nltk.sent_tokenize(paragraph)

lemmatizer = WordNetLemmatizer()

# Lemmatization
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)  
