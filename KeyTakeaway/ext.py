from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Models
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.kl import KLSummarizer
from KeyTakeaway.preprocess_test import preprocess
# output_file = 'OCR_Rec/Text/' + "imageCap" + '.txt'
def lexrank(filename):
    preprocess(filename)
    file = 'KeyTakeaway/cleanTest.txt'
    parser = PlaintextParser.from_file(file, Tokenizer('english'))
    doc = parser.document
    lex = LexRankSummarizer()
    sent_list = lex(doc, 3)
    sentences = []
    for sent in sent_list:
        sentences.append(str(sent))
    return sentences



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






