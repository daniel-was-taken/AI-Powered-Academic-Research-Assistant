from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Models
from sumy.summarizers.lex_rank import LexRankSummarizer
from M_PreProcess import preprocess

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







