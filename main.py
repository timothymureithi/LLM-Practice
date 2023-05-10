import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

nltk.download('punkt')

LANGUAGE = "english"
SENTENCES_COUNT = 3

parser = PlaintextParser.from_file("https://www.tutorialspoint.com/php/php_tutorial.pdf", Tokenizer(LANGUAGE))
summarizer = LexRankSummarizer()
summarizer.stop_words = nltk.corpus.stopwords.words(LANGUAGE)

summary = []
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    summary.append(str(sentence))

print(" ".join(summary))
