from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Models
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.kl import KLSummarizer

file = 'text/textcontent.txt'
parser = PlaintextParser.from_file(file, Tokenizer('english'))
doc = parser.document


def print_out(sentences):
    for sent in sentences:
        print(sent)

print("\n LEX \n")

lex = LexRankSummarizer()
print_out(lex(doc, 2))



# ------------------------------

# import spacy 
# import pytextrank
# from spacy.lang.en.stop_words import STOP_WORDS
# from string import punctuation

# stopwords = STOP_WORDS

# nlp = spacy.load("en_core_web_lg")

# nlp.add_pipe("textrank")

# example_text = ""

# with open("text/textcontent.txt", "r", encoding="utf-8") as f:
#         example_text = f.read()

# doc = nlp(example_text)


# for sent in doc._.textrank.summary(limit_sentences = 3):
#     print(sent)






