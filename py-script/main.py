import sys
# sys.path.append(".py-script/help_foos.py")
import help_foos as hf

import json
import wikipedia

import nltk #nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.summarization.summarizer import summarize

from keras.models import load_model
from flask import Flask 

# app = Flask(__name__)
# @app.route("/")

# def main():

#     INPUT_1 = '{"text": "   Pneumonia.  ! Pneumonia "}'
#     INPUT_2 = '{"text": "Subject was administered 100mg remdesivir intravenously over a period of 120 min"}'

#     LANG = 'english'
#     WIKI_LANG = 'en'

#     MODEL_PATH = './model/'

#     wikipedia.set_lang(WIKI_LANG) 

#     data = json.loads(INPUT_1)
#     text = data.get('text')

#     clear_text = hf.preproc_text(text)

#     if hf.is_text_definition(clear_text, LANG):
#         try:  
#             text = summarize(wikipedia.summary(clear_text))
#             return text
             
#         except:
#             print('Cant find the definition')
        
#     else:
#         pass
#         # model_cwi = load_model(MODEL_PATH)
#         # simple_text = hf.simplify_text(clear_text, LANG)
        
#         vec = hf.get
#         return vec


# if __name__ == "__main__":
#     app.run()


INPUT_1 = '{"text": "   Pneumonia.  ! Pneumonia "}'
INPUT_2 = '{"text": "Subject was administered 100mg remdesivir intravenously over a period of 120 min"}'

LANG = 'english'
WIKI_LANG = 'en'

MODEL_PATH = './model/'

wikipedia.set_lang(WIKI_LANG) 

data = json.loads(INPUT_2)
text = data.get('text')

clear_text = hf.preproc_text(text)

if hf.is_text_definition(clear_text, LANG):
    try:  
        print(summarize(wikipedia.summary(clear_text)))
        
    except:
        print('Cant find the definition')
    
else:
    
    # model_cwi = load_model(MODEL_PATH)
    # simple_text = hf.simplify_text(clear_text, LANG)
    # print(simple_text)

    vects = hf.get_doc2vec_from_text(clear_text)

