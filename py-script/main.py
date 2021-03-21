import sys
import pandas as pd
import numpy as np
# sys.path.append(".py-script/help_foos.py")
import help_foos as hf

import json
import wikipedia

import nltk #nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.summarization.summarizer import summarize

from keras.models import load_model
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/api",methods=['POST'])

def main():
    # INPUT_1 = '{"text": "   Pneumonia.  ! Pneumonia "}'
    # INPUT_2 = '{"text": "Subject was administered 100mg remdesivir intravenously over a period of 120 min"}'

    LANG = 'english'
    WIKI_LANG = 'en'
    MODEL_PATH = './model/'
    wikipedia.set_lang(WIKI_LANG) 

    if request.method == "POST":
        if not request.is_json:
            return {'message':'format not JSON'}
        if request.is_json:    
            data = request.get_json()
            # return {'message':'successfully received string: ' + data} 

            # text = data.get('text')

            clear_text = hf.preproc_text(data)
            # return {'message':clear_text} # this line works

            # if hf.is_text_definition(clear_text, LANG):
        #     try:  
        #         text = summarize(wikipedia.summary(clear_text))
                # return {'message':'success'}
             
        #     except:
        #         return {'message':'failed'}
        
            
            sample_dataset = hf.prepare_sample_dataset()
            
            vects = hf.get_doc2vec_from_text(clear_text)
            
            result = hf.find_most_similar_article(sample_dataset, vects)

            return {'message':str(result)}
                # result


if __name__ == "__main__":
    app.run()


# INPUT_1 = '{"text": "   Pneumonia.  ! Pneumonia "}'
# INPUT_2 = '{"text": "Subject was administered 100mg remdesivir intravenously over a period of 120 min"}'

# LANG = 'english'
# WIKI_LANG = 'en'

# wikipedia.set_lang(WIKI_LANG) 

# data = json.loads(INPUT_2)
# # text = data.get('text')

# text = """Medulloblastoma is a type of embryonal tumor — a tumor that starts in the fetal (embryonic) cells in the brain. Based on different types of gene mutations, there are at least four subtypes of medulloblastoma. Though medulloblastoma is not inherited, syndromes such as Gorlin's syndrome or Turcot's syndrome might increase the risk of medulloblastoma."""

# clear_text = hf.preproc_text(text)

# if hf.is_text_definition(clear_text, LANG):
#     try:  
#         print(summarize(wikipedia.summary(clear_text)))
        
#     except:
#         print('Cant find the definition')
    
# else:
#     sample_dataset = hf.prepare_sample_dataset()
    
#     vects = hf.get_doc2vec_from_text(clear_text)
    
#     result = hf.find_most_similar_article(sample_dataset, vects)

#     print(result.title)