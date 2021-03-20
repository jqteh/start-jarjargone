#import help_foos as hf

import json
import wikipedia

import nltk #nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.summarization.summarizer import summarize

from keras.models import load_model
from flask import Flask 

app = Flask(__name__)
@app.route("/")



def preproc_text(input_text):
    """
    Function that takes string as input removes punctuation and whitespaces.
    and converts text to lowercase.
    
    Parameters
    ----------
    text : STR

    Returns
    -------
    clear_text : STR

    """
    
    #remove punctuation
    clear_text = re.sub(r'[^\w\s]', '', input_text) 
    
    #remove whitespaces
    clear_text = " ".join(clear_text.split())
    
    #to lower
    clear_text = clear_text.lower()
    
    return clear_text
    


def is_text_definition(input_text, LANG):
    
    """
    True = Definition
    False = text
    """
    
    text_to_check = input_text.split(" ")
    
    stopwoprds = stopwords.words(LANG)
    
    
    if len(text_to_check) <= 2:
        return True
    
    elif len(text_to_check) == 3:
        for word in text_to_check:
            if word in stopwoprds:
                return False
        return True
            
    else:
        return False


def main():

    INPUT_1 = '{"text": "   Pneumonia.  ! Pneumonia "}'
    INPUT_2 = '{"text": "Subject was administered 100mg remdesivir intravenously over a period of 120 min"}'

    LANG = 'english'
    WIKI_LANG = 'en'

    MODEL_PATH = './model/'

    wikipedia.set_lang(WIKI_LANG) 

    data = json.loads(INPUT_2)
    text = data.get('text')

    clear_text = preproc_text(text)

    if is_text_definition(clear_text, LANG):
        try:  
            print(summarize(wikipedia.summary(clear_text)))
            
        except:
            print('Cant find the definition')
        
    else:
        pass
        # model_cwi = load_model(MODEL_PATH)
        # simple_text = hf.simplify_text(clear_text, LANG)
        # print(simple_text)

if __name__ == "__main__":
    app.run()


# INPUT_1 = '{"text": "   Pneumonia.  ! Pneumonia "}'
# INPUT_2 = '{"text": "Subject was administered 100mg remdesivir intravenously over a period of 120 min"}'

# LANG = 'english'
# WIKI_LANG = 'en'

# MODEL_PATH = './model/'

# wikipedia.set_lang(WIKI_LANG) 

# data = json.loads(INPUT_2)
# text = data.get('text')

# clear_text = hf.preproc_text(text)

# if hf.is_text_definition(clear_text, LANG):
#     try:  
#         print(summarize(wikipedia.summary(clear_text)))
        
#     except:
#         print('Cant find the definition')
    
# else:
#     pass

#     #model_cwi = load_model(MODEL_PATH)
#     simple_text = hf.simplify_text(clear_text, LANG)
#     print(simple_text)
