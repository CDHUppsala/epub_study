import sys
import spacy
from spacy.tokens import Doc
file=sys.argv[1]
from collections import Counter
#import spacy for swedish
nlp = spacy.load('sv_core_news_lg')
#open file
with open(file, 'r') as f:
    text = f.read()
#tokenize
doc = nlp(text)
spacy.tokens.Token.set_extension('_hl', default=False)
#remove 20 words before and after the word "ISBN" or "EPUB"
def remove_words_around(doc0, word, n=20):
    """
    Remove n words before and after the words 
    (Function to help remove metadata information based on keywords)
    >>> remove_words_around(doc("This is an ISBN" yadayada. Once upon a time.), "ISBN", n=2)
    This is an Once upon a time.
    """
    for i, token in enumerate(doc0):
        if token.text.lower()==word.lower():
            #remove 20 words before and after the word "ISBN" or "EPUB"
            #merge the two parts of the text
            doc1 = nlp(doc0[:i-n].text)
            doc2 = nlp(doc0[i+n:].text)
            doc0 = Doc.from_docs([doc1]+[doc2])
    return doc0

meta_markers = ["ISBN", "EPUB","©","copyright","e-bok"]
for marker in meta_markers:
    doc = remove_words_around(doc, marker)
#get the name entities of the text
ents = Counter()
for ent in doc.ents:
    ents[f"{ent.text},{ent.label_}"] += 1
#open csv file for writing
with open(file[:-4]+".csv", "w") as f:
    #write the header
    f.write("Entity,Type(PRS=Person LOC=Location...),Count")
    for key, val in ents.items():
        #write the entity and its count
        f.write("\n")
        f.write(f"{key},{val}".replace("\n",""))


#get all entities of the text into a li
entities=[]
type_entity=[]
sentences=[]

#loop through the entities
#make a csv file that rempresent location and their associated adjectives
with open(file[:-4]+".loc.csv", "w") as f:
    f.write("Location,Adjective")
    for ent in doc.ents:
        #if entity is LOC
        if ent.label_=="LOC":
        #Get adjectives related to the entity
            for token in ent.root.head.children:
                if token.pos_=="ADJ":
                    
                    #write the entity and its adjective om the csv file
                    f.write("\n")
                    f.write(f"{ent.text},{token.text}".replace("\n",""))

#Get number of sentences
f = open(file[:-4]+".data.txt", "w")
for sent in doc.sents:
    sentences.append(sent.text)
num_sentences=len(sentences)
f.write("Name of the file: "+file)
f.write("\n\nNumber of sentences: "+str(len(sentences)))
#Get the everage number of words in sentences:
words=[]
for sent in doc.sents:
    for token in sent:
        words.append(token.text)

num_words=len(words)
f.write("\nNumber of words: "+str(len(words)))
f.write("\nNumber of words per sentences: "+str(len(words)/len(sentences)))
def get_top_most_common_words(doc, type="ADJ",n=20):
    #get the most common words
    from collections import Counter
    words = Counter()
    for token in doc:
        if token.pos_==type:
            words[token.text] += 1
    return words.most_common(n)
n = 20



#Get the most common words by type
f.write("\nTop "+str(n)+" most common adjectives: \n"+str(get_top_most_common_words(doc, type="ADJ",n=20)))
f.write("\nTop "+str(n)+" most common nouns: \n"+str(get_top_most_common_words(doc, type="NOUN",n=20)))
f.write("\nTop "+str(n)+" most common verbs: \n"+str(get_top_most_common_words(doc, type="VERB",n=20)))
f.write("\nTop "+str(n)+" most common averbes: \n"+str(get_top_most_common_words(doc, type="ADP",n=20)))
f.write("\nTop "+str(n)+" most common proper nouns: \n"+str(get_top_most_common_words(doc, type="PROPN",n=20)))
f.close()
#Remove all the stopwords from the text
#stopwords = spacy.lang.sv.stop_words.STOP_WORDS
words = [token.text for token in doc if not token.is_stop]
f_stop = open(file[:-4]+".stop.txt", "w")
#write the text without stopwords in the file
f_stop.write(" ".join(words))
f_stop.close()

#lemmatising the text
lemmas = [token.lemma_ for token in doc]
f_lemma = open(file[:-4]+".lemma.txt", "w")
#write the text with lemmas in the file
f_lemma.write(" ".join(lemmas))
f_lemma.close()

#lemmatising the text
lemmas = [token.lemma_ for token in doc]
#removing the stopwords of the lemmas
#list of stopwords
stopwords = spacy.lang.sv.stop_words.STOP_WORDS
#Add personalized stopwords
nlp.Defaults.stop_words |= {"skola", "se", "ta","ju"}
print(lemmas[50])
#Remove stopwords
lemmas = [lemma for lemma in lemmas if lemma.lower() not in stopwords]
removing_stopwords_lemmas = open(file[:-4]+".lemma.stop.txt", "w")
#write the text with lemmas in the file
removing_stopwords_lemmas.write(" ".join(lemmas))
removing_stopwords_lemmas.close()