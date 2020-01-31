#Author Sajarin Dider

from youtube_transcript_api import YouTubeTranscriptApi as youtube
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer 
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

video_url = 'L3LMbpZIKhQ' #MIT OCW Discrete Math 
# video_url = 'tKTZoB2Vjuk' #Google Python Class
subtitles = youtube.get_transcript(video_url, languages=['en'])
transcript= ""
for subtitle in subtitles:  
    transcript += subtitle['text'] + " " 
    # print(subtitle['text'])

transcription = open("transcription.txt", "w", encoding="utf-8", errors="ignore")
summarized = open('vid_summary.txt', "a")
n = transcription.write(transcript)
parser = PlaintextParser.from_file(transcription.name, Tokenizer('english'))
stemmer = Stemmer("english")
summarizer = LexRankSummarizer(stemmer)

for sentence in summarizer(parser.document, 20):

    print(sentence)
    # output.cell(width,height, str(sentence))
    # width += 10
    summarized.write(str(sentence))
