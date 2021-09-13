import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = """World War I, also known as the Great War, began in 1914 after the assassination of Archduke Franz Ferdinand of Austria. His murder catapulted into a war across Europe that lasted until 1918. During the conflict, Germany, Austria-Hungary, Bulgaria and the Ottoman Empire (the Central Powers) fought against Great Britain, France, Russia, Italy, Romania, Japan and the United States (the Allied Powers). Thanks to new military technologies and the horrors of trench warfare, World War I saw unprecedented levels of carnage and destruction. By the time the war was over and the Allied Powers claimed victory, more than 16 million people—soldiers and civilians alike—were dead."""
               
               
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

# Stemming
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)   
    
