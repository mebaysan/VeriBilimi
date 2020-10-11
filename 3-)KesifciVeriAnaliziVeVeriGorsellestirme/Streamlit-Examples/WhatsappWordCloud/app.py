import mydata
import pandas as pd
import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


@st.cache(persist=True) # her seferinde veriyi tekrar tekrar yüklemiyoruz, ramde tutuyoruz
def load_data():
    df = mydata.get_data(
        'WHATSAPP_CHAT_PATH')
    return df


df = load_data()

st.title('Whatsapp Sohbet Kelime Analizi')


kelimeler = ' '.join(df['Mesaj'])
islenmis_kelimeler = ' '.join([kelime for kelime in kelimeler.split() if 'Media' not in kelime and 'omitted' not in kelime and 'message' not in kelime and 'deleted' not in kelime])
word_cloud = WordCloud(stopwords=STOPWORDS, background_color='white',
                       height=640, width=800).generate(islenmis_kelimeler)
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.imshow(word_cloud)
plt.xticks([])
plt.yticks([])
st.pyplot()