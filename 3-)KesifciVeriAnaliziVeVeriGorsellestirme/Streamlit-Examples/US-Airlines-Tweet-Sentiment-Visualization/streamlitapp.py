import streamlit as st # pip install streamlit
import pandas as pd # pip install pandas
import numpy as np # pip install numpy
import plotly.express as px # pip install plotly
from wordcloud import WordCloud, STOPWORDS # pip install wordcloud
import matplotlib.pyplot as plt # pip install matplotlib

# Dataset -> https://www.kaggle.com/crowdflower/twitter-airline-sentiment?select=Tweets.csv

st.title("US Airlines'a ait tweetlerin Sentiment Analizi") # sayfadaki ana bölüme ait başlık
st.sidebar.title("US Airlines'a ait tweetlerin Sentiment Analizi") # sidebar başlığı

st.markdown("""
## Ilk Streamlit Dashboard'im
""") # ana bölüme markdown ekler
st.sidebar.markdown("""
### Bu dashboard tweetlerin sentiment analizi icin olusturulmustur 🤓
""") # sidebar'a markdown ekler

@st.cache(persist=True) # bu fonksiyonun ramde tutulmasını sağlar
def load_data():
    data = pd.read_csv('Tweets.csv')
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data

df = load_data()

st.sidebar.subheader('Rastgele tweet goster') # sidebar'a alt başlık açar
random_tweet = st.sidebar.radio('Sentiment', ('positive','neutral','negative')) # sidebar'a radio box ekler. ilk parametre başlık, ikinci tuple ise radio'nun alacağı değerlerdir. Bize radio'dan seçilen değeri döner
st.sidebar.markdown(df.query(f'airline_sentiment == "{random_tweet}"')[['text']].sample(n=1).iat[0,0]) # random_tweet'in değerine göre veri setini filtreledik ve rastgele bir tanesini markdown ile sidebar'a yazdık

st.sidebar.markdown("### Sentiment'e göre tweet sayısı")
select = st.sidebar.selectbox('Görselleştirme tipi',['Histogram','Pie Chart'], key='my-selectbox') # sidebar'a bir selectbox oluşturuyoruz. Seçilen değer select değişkenine aktarılıyor. İlk parametre selectbox adı, ikinci liste ise gelebilecek değerler
sentiment_count = df['airline_sentiment'].value_counts() # sütunun değerlerini ayrı bir değişkene atıyoruz
sentiment_count = pd.DataFrame({'Sentiment':sentiment_count.index, 'Tweets':sentiment_count.values}) # yeni bir df oluşturuyoruz


if not st.sidebar.checkbox('Chart\'i Gizle',True): # sidebar'a bir checkbox OLUŞTURUYORUZ. İlk parametre checkbox adı ikincisi ise default başlangıç değeri
    st.markdown('### Sentiment\'e gore tweet sayisi')
    if select == 'Histogram': # eğer yukarda oluşturduğumuz selectbox'ın değeri 'Histogram' ise chart oluştur
        fig = px.bar(data_frame=sentiment_count,x='Sentiment',y='Tweets',color='Tweets',height=500) # plotly express ile chart oluşturuyoruz
        st.plotly_chart(fig) # plotly_chart fonksiyonu sayesinde plotly figürlerini gösterebiliyoruz
    else:
        fig = px.pie(data_frame=sentiment_count,values='Tweets',names='Sentiment')
        st.plotly_chart(fig)



st.sidebar.subheader('Tweetler nereden ve ne zaman geliyor?')

hour = st.sidebar.slider('Günün hangi saati',0,23) # sidebar'a slider ekliyoruz. (Ad, min değer, max değer)
modified_df = df[df['tweet_created'].dt.hour == hour] # seçilen saate göre df'i filtreliyoruz

if not st.sidebar.checkbox('Haritayi Gizle',True,key = 'my-hour'): # checkbox oluşturuyoruz. Default değerini set ediyoruz. Bu sayede eğer False ise aşağıdaki bloğu çalıştır diyebiliyoruz.
    st.markdown('### Secilen saate gore tweet sayisi ')
    st.markdown(f'{hour}:00 ile {(hour+1) % 24}:00 arasnda toplam {len(modified_df)} tweet atilmis')
    st.map(modified_df)
    if st.sidebar.checkbox('Ham veriyi goster',False):
        st.write(modified_df)

st.sidebar.subheader('Havayollarina ait tweetleri sentiment\'e gore ayirma')
choice = st.sidebar.multiselect('Havayolu sec',('US Airways','United','American','Southwest','Delta','Virgin America'),key='my-multichoice') # multiple selectbox oluşturuyoruz. (Ad,(Seçilebilecek,Opsiyonlar),key). Liste olarak seçilenleri döner

if len(choice) > 0:
    choice_df =df[df['airline'].isin(choice)]
    fig_choice = px.histogram(data_frame=choice_df,x='airline',y='airline_sentiment',histfunc='count',color='airline_sentiment',
    facet_col='airline_sentiment',labels={'airline_sentiment':'tweet sayisi'},height=600,width=800) # airline_sentiment sütununa göre ayrı ayrı kolonlarda grafik oluşturuyoruz
    st.plotly_chart(fig_choice)


st.sidebar.header('Kelime Bulutu')

word_sentiment = st.sidebar.radio('Sentiment\'e göre kelime bulutu goster',('positive','neutral','negative'),key='word-cloud')

st.set_option('deprecation.showPyplotGlobalUse', False)
if not st.sidebar.checkbox('Gizle',True,key='my-word-cloud-check'):
    st.header(f'{word_sentiment} icin kelime bulutu')
    word_df = df[df['airline_sentiment'] == word_sentiment]
    words = ' '.join(word_df['text'])
    processed_words = ' '.join([word for word in words.split() if 'http' not in word and not word.startswith('@') and word != 'RT'])
    word_cloud = WordCloud(stopwords=STOPWORDS,background_color='white',height=640,width=800).generate(processed_words)
    plt.imshow(word_cloud)
    plt.xticks([])
    plt.yticks([])
    st.pyplot()