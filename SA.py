from transformers import pipeline
import nltk
import os
import pandas as pd
import sys
import numpy as np
from nltk.tokenize import word_tokenize
nltk.download('punkt')
SentimentAnalysis=pipeline("sentiment-analysis")
os.chdir(r'D:\SUDHEENDRA  INFO 5082 Project\Project\STT_apr')


def run_sa(filename):
    with open(os.sep.join([os.getcwd(),'text files',filename]), 'rb') as text:
        text_data=str(text.read())
        set_of_sentences=word_tokenize(text_data)
        sum_of_positive_sentiment=[]
        sum_of_negative_sentiment = []
        sentences_all=[]
        sentiment_all=[]
        for sentences in set_of_sentences:
            sentiment_value=SentimentAnalysis(sentences)[0]
            if sentiment_value['label']=='POSITIVE':
                sum_of_positive_sentiment.append(sentiment_value['score'])
                sentences_all.append(sentences)
                sentiment_all.append(sentiment_value['score'])
            else:
                sum_of_negative_sentiment.append(sentiment_value['score'])
                sentences_all.append(sentences)
                sentiment_all.append(-1*sentiment_value['score'])

        final_value=round(((np.sum(sum_of_positive_sentiment)-np.sum(sum_of_negative_sentiment))/len(set_of_sentences)),2)
        final_sentiment=''
        final_sentiment_value=0
        if final_value>0:
            final_sentiment='POSITIVE'
            final_sentiment_value=final_value
        else:
            final_sentiment = 'NEGATIVE'
            final_sentiment_value = final_value
        return (final_sentiment,final_sentiment_value)



if __name__ == '__main__':
    fname_argument="IHFL Q2-21.txt"
    (final_sentiment,final_sentiment_value)=run_sa(fname_argument)
    print(final_sentiment,final_sentiment_value)
