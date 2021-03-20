import re 

import nltk
from nltk.corpus import stopwords
import langdetect 

from azure.ai.textanalytics import TextAnalyticsClient
from azure.identity import DefaultAzureCredential

import torch
from transformers import BertTokenizer, BertModel, BertForMaskedLM



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
    
  
def cleaner(word):
  #Remove links
  word = re.sub(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*', 
                '', word, flags=re.MULTILINE)
  word = re.sub('[\W]', ' ', word)
  word = re.sub('[^a-zA-Z]', ' ', word)
  return word.lower().strip()


    
def simplify_text(input_text, LANG):

    # summarize()
    
    # from tika import parser
    # parsed = parser.from_file('/path/to/file')
    # print(parsed["metadata"])
    # print(parsed["content"])
    
    # input_text = list(input_text)
    
    # # credential = DefaultAzureCredential()
    # # text_analytics_client = TextAnalyticsClient(endpoint="https://en-us.api.cognitive.microsoft.com/",
    # #                                             credential=credential)

    # # simple_text = text_analytics_client.analyze_sentiment(input_text)
    
    # from tika import language

    # lang = language.from_file(input_text)
    print('WORKING WITH:', input_text)
    
    bert_model = 'bert-large-uncased'
    tokenizer = BertTokenizer.from_pretrained(bert_model)
    model = BertForMaskedLM.from_pretrained(bert_model)
    model.eval()
    
    input_padded, index_list, len_list = process_input(input_text)
    pred_cwi = model_cwi.predict(input_padded)
    pred_cwi_binary = np.argmax(pred_cwi, axis = 2)
    complete_cwi_predictions = complete_missing_word(pred_cwi_binary, index_list, len_list)
    bert_candidates =   get_bert_candidates(input_text, complete_cwi_predictions)
    for word_to_replace, l_candidates in bert_candidates:
      tuples_word_zipf = []
      for w in l_candidates:
        if w.isalpha():
          tuples_word_zipf.append((w, zipf_frequency(w, 'en')))
      tuples_word_zipf = sorted(tuples_word_zipf, key = lambda x: x[1], reverse=True)
      new_text = re.sub(word_to_replace, tuples_word_zipf[0][0], new_text) 
    
    print("Original text: ", input_text )
    print("Simplified text:", new_text, "\n")
     
    
    return simple_text
    


def build_vocabulary(sentences, embedding_model, dimension):
    all_words = [tpl[0] for sentence in sentences for tpl in sentence['seq']] + list(wordlist_lowercased)
    print('# Words : {}'.format(len(all_words)))
    counter = Counter(all_words)
    vocab_size = len(counter) + 1
    print('# Vocab : {}'.format(vocab_size))
    print('# embeding model  : {}'.format(len(embedding_model.vocab)))   
    word2index = {word : index for index, (word, count) in enumerate(counter.most_common(), 1)}
    index2word = {index : word for word, index in word2index.items()}
    # +1 required for pad token
    embedding_matrix = np.zeros(((vocab_size), dimension))
    missing_embed_words = []
    i_ = 0
    for word, index in word2index.items():
        if word in embedding_model.vocab:
            embedding = embedding_model[word]
        else:
             i_ +=1
             continue
        embedding_matrix[index] = embedding
    missing_embed_count = len(missing_embed_words)
    print('# Words missing embedding : {}'.format(missing_embed_count))
    print('Embedding shape : {}'.format(embedding_matrix.shape))
    print("i: ", i_ )
    return word2index, index2word, embedding_matrix





def process_input(input_text):
  word2index, index2word, embedding = build_vocabulary(sentences, embedding_model, dimension)
  input_text = cleaner(input_text)
  clean_text = []
  index_list =[]
  input_token = []
  index_list_zipf = []
  for i, word in enumerate(input_text.split()):
    if word in word2index:
      clean_text.append(word)
      input_token.append(word2index[word])
    else:
      index_list.append(i)
  input_padded = pad_sequences(maxlen=sent_max_length, sequences=[input_token], padding="post", value=0)
  return input_padded, index_list, len(clean_text)

    
    
def complete_missing_word(pred_binary, index_list, len_list):
  list_cwi_predictions = list(pred_binary[0][:len_list])
  for i in index_list:
    list_cwi_predictions.insert(i, 0)
  return list_cwi_predictions 
    
    
    
    
def get_bert_candidates(input_text, list_cwi_predictions, numb_predictions_displayed = 10):
  list_candidates_bert = []
  for word,pred  in zip(input_text.split(), list_cwi_predictions):
    if (pred and (pos_tag([word])[0][1] in ['NNS', 'NN', 'VBP', 'RB', 'VBG','VBD' ]))  or (zipf_frequency(word, 'en')) <3.1:
      replace_word_mask = input_text.replace(word, '[MASK]')
      text = f'[CLS]{replace_word_mask} [SEP] {input_text} [SEP] '
      tokenized_text = tokenizer.tokenize(text)
      masked_index = [i for i, x in enumerate(tokenized_text) if x == '[MASK]'][0]
      indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
      segments_ids = [0]*len(tokenized_text)
      tokens_tensor = torch.tensor([indexed_tokens])
      segments_tensors = torch.tensor([segments_ids])
      # Predict all tokens
      with torch.no_grad():
          outputs = model(tokens_tensor, token_type_ids=segments_tensors)
          predictions = outputs[0][0][masked_index]
      predicted_ids = torch.argsort(predictions, descending=True)[:numb_predictions_displayed]
      predicted_tokens = tokenizer.convert_ids_to_tokens(list(predicted_ids))
      list_candidates_bert.append((word, predicted_tokens))
  return list_candidates_bert
    
        