from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.random import RandomSummarizer

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer


def _lsa_summarizer(text, sentence_len):
    summarizer = LsaSummarizer()
    summary = summarizer(text.document, sentence_len)
    for sentence in summary:
        print(sentence)


def _lex_rank_summarizer(text, sentence_len):
    summarizer = LexRankSummarizer()
    summary = summarizer(text.document, sentence_len)
    for sentence in summary:
        print(sentence)


def _edmundson_summarizer(text, sentence_len):
    summarizer = EdmundsonSummarizer()
    summary = summarizer(text.document, sentence_len)
    for sentence in summary:
        print(sentence)


def _luhn_summarizer(text, sentence_len):
    summarizer = LuhnSummarizer()
    summary = summarizer(text.document, sentence_len)
    for sentence in summary:
        print(sentence)


def _text_rank_summarizer(text, sentence_len):
    summarizer = TextRankSummarizer()
    summary = summarizer(text.document, sentence_len)
    for sentence in summary:
        print(sentence)


def _sum_basic_summarizer(text, sentence_len):
    summarizer = SumBasicSummarizer()
    summary = summarizer(text.document, sentence_len)
    for sentence in summary:
        print(sentence)


def _kl_summarizer(text, sentence_len):
    summarizer = KLSummarizer()
    summary = summarizer(text.document, sentence_len)
    for sentence in summary:
        print(sentence)


def _random_summarizer(text, sentence_len):
    summarizer = RandomSummarizer()
    summary = summarizer(text.document, sentence_len)
    for sentence in summary:
        print(sentence)


def summarize_article(article, mode, sentence_len=2, lang='english'):
    summarize_funcs = {'lsa': _lsa_summarizer,
                       'lex_rank': _lex_rank_summarizer,
                       'edmundson': _edmundson_summarizer,
                       'luhn': _luhn_summarizer,
                       'text_rank': _text_rank_summarizer,
                       'sum_basic': _sum_basic_summarizer,
                       'kl': _kl_summarizer,
                       'random': _random_summarizer,
                       }
    article = PlaintextParser.from_string(article, Tokenizer(lang))
    summarize_funcs[mode](article, sentence_len)


if __name__ == '__main__':
    article = """
    Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and 
    dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing 
    whether that nation, or any nation so conceived and so dedicated, can long endure.
    We are met on a great battle-field of that war.
    We have come to dedicate a portion of that field,
    as a final resting place for those who here gave their lives that that nation might live.
    It is altogether fitting and proper that we should do this. But, in a larger sense, 
    we can not dedicate we can not consecrate we can not hallow this ground. 
    The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract.
     The world will little note, nor long remember what we say here, but it can never forget what they did here. 
     It is for us the living, rather,
      to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced.
       It is rather for us to be here dedicated to the great task remaining before us that from these honored dead 
       we take increased devotion to that cause for which they gave the last full measure of devotion that we here
       highly resolve that these dead shall not have died in vain that this nation, under God, shall have a new birth 
       of freedom and that government of the people, by the people, for the people, shall not perish from the earth."""

    # text = PlaintextParser.from_string(text, Tokenizer("english"))
    summarize_article(article, 'lsa', sentence_len=2, lang='english')
