## Prerequisites with Virtual env
If you use virtual env you can directly run these commands:
```bash
cd path/to/ebook_study
python3 -m venv ebook_env
#python -m venv ebook_env #try this command in case the previous one fails
source ebook_env/bin/activate
pip install -r requirements.txt
sh basic.sh
```

## Extra
To use another corpus, just replace the ebooks in the folder "corpus"

# Description
This project aims at analysing Epub in swedish.

# Usage
If you already have a text in the txt format you can use directly the python script
```
python stats.py example.txt
```
Make sure your file example.txt is in Swedish and that you have installed the prerequisites above.

As an output you will get
- outputs (the folder in which you will find the files below)
- example.lemma.txt (your text lemmatized)
- example.stop.txt (your text without stopwords)
- example.lemma.stop.txt (your text both lemmatized and without stopwords)
- example.data.txt (some quick stats about your text)
- example.xlsx (Name entity detections)

# Authors:
Original project of [AnnaCarin Billing](https://www.katalog.uu.se/empinfo/?id=N96-2024). Pilot project at CDHU
Engineer:
Marie Dubremetz
Gitlab:
[@mardub](https://gitlab.com/mardub)
Github:
[@mardub1635](https://github.com/mardub1635)
Website:
[http://www.uppsala.ai](http://www.uppsala.ai)
e-mail:
mardubr-github@yahoo.com

