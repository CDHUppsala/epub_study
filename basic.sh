# convert all the files of the current directory txt
for file in corpus/*
do
# get the filename without the path
    filename=$(basename "$file")
    # get the filename without the extension
    filename="${filename%.*}"
    ebook-convert "$file" corpus_txt/$filename.txt # copy the file to the new directory
    python stats.py corpus_txt/$filename.txt
    ssconvert corpus_txt/$filename.loc.csv corpus_txt/$filename.loc.xlsx
    ssconvert corpus_txt/$filename.csv corpus_txt/$filename.xlsx
    rm corpus_txt/$filename.loc.csv 
    rm corpus_txt/$filename.csv  
done
#remove all the none corpus files to the output file
mv corpus_txt/*.xlsx outputs/
mv corpus_txt/*.*.* outputs/

# count the number words in all corpus files
cat corpus_txt/* | wc -w
cat corpus_txt/* > all_corpus.txt
python stats.py corpus_txt/all_corpus.txt
