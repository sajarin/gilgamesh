# Author: Sajarin Dider
# from fpdf import FPDF
import pdfminer
import pdfminer.high_level
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer 
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# output=FPDF()
filename = './c.pdf'
# pdf_reader = PyPDF2.PdfFileReader(pdf)


# count = 0
# text = ""
# page_num = pdf_reader.numPages

# while count < page_num: 
#     page = pdf_reader.getPage(count)
#     count += 1
#     text += page.extractText()

text = pdfminer.high_level.extract_text(filename, password='', page_numbers=None, maxpages=10, caching=True, codec='utf-8', laparams=None)

if text == "":
    print("No text extracted")

text_file = open("example.txt", "w", encoding="utf-8", errors="ignore")
summary = open('summary.txt', "a")

n = text_file.write(text)
text_file.close()
parser = PlaintextParser.from_file(text_file.name, Tokenizer('english'))
stemmer = Stemmer("english")

summarizer = LexRankSummarizer(stemmer)
# output.add_page()
# output.set_font('Arial')

# height = 10
# width = 40 
for sentence in summarizer(parser.document, 20):

    print(sentence, "\n")
    # output.cell(width,height, str(sentence))
    # width += 10
    summary.write(str(sentence))
# output.output('output.pdf','F')
