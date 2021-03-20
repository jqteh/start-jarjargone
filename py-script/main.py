import json

import wikipedia

import help_foo as hf

import nltk
#nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from gensim.summarization.summarizer import summarize


INPUT_1 = '{"text": "   Pneumonia.  ! Pneumonia "}'
INPUT_2 = '{"text": "Subject was administered 100mg remdesivir intravenously over a period of 120 min"}'


LANG = 'english'
WIKI_LANG = 'en'

wikipedia.set_lang(WIKI_LANG) 

data = json.loads(INPUT_2)

text = data.get('text')

clear_text = hf.preproc_text(text)


if hf.is_text_definition(clear_text, LANG):
    try:
        wiki = wikipedia.summary(clear_text) #, sentences=15
    
        print(summarize(wiki))
        
    except:
        print('Cant find the definition')
    
else:
    simple_text = hf.simplify_text(clear_text, LANG)
    
    print(simple_text)