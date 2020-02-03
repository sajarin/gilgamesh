# Author: Sajarin Dider
# Description: This program reads in a pdf file, converts it to text and then applies LexRank to summarize the text. It outputs the summarization in a separte text file 

import pdfminer
import pdfminer.high_level
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer 
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

#open the file
filename = './c.pdf'

#extract text from filename
text = pdfminer.high_level.extract_text(filename, password='', page_numbers=None, maxpages=10, caching=True, codec='utf-8', laparams=None)

#test if text is empty
if text == "":
    print("No text extracted")

#create text files for extracted text and summarized output file
text_file = open("example.txt", "w", encoding="utf-8", errors="ignore")
summary = open('summary.txt', "a")

n = text_file.write(text)
text_file.close()
parser = PlaintextParser.from_file(text_file.name, Tokenizer('english'))
stemmer = Stemmer("english")

summarizer = LexRankSummarizer(stemmer)

for sentence in summarizer(parser.document, 20):

    print(sentence, "\n")
    summary.write(str(sentence))
