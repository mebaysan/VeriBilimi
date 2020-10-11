import os
import re
import pandas as pd


def get_data(path):
    whatsapp_file = path
    # Whatsapp dosyasını okuyoruz
    if os.path.exists(whatsapp_file):
        file_data = open(whatsapp_file, 'r', encoding="utf8")
        whatsapp_content = file_data.read()

    # Tarihi Alıyoruz
    date_regex = re.compile(r'(\d+/\d+/\d+)')
    date = date_regex.findall(whatsapp_content)

    # Zamanı Alıyoruz
    time_regex = re.compile(r'(\d{1,2}:\d{2})')
    time = time_regex.findall(whatsapp_content)

    # Kullanıcıyı Alıyoruz
    user_regex = re.compile(r'-(.*?):')
    user = user_regex.findall(whatsapp_content)

    # Mesajı Alıyoruz
    message_regex = re.compile(r'([^:]+):?$')
    me_regex = re.compile(r"(\n)(?<=)(\d+/\d+/\d+)(.*)")
    mess = me_regex.findall(whatsapp_content)
    message = [''.join(message_regex.findall(''.join(msg))).strip()
               for msg in mess]

    # Aldığımız tüm verileri bir arada zipliyoruz
    data = []
    for w, x, y, z in zip(date, time, user, message):
        data.append([str(w), str(x), str(y), str(z)])

    # DataFrame oluşturuyoruz
    df = pd.DataFrame(data, columns=("Tarih", "Zaman", "Kullanici", "Mesaj"))

    # Mesajları temizliyoruz
    df['Mesaj'] = df['Mesaj'].str.replace('\'(.*?): ', '')

    # Tarih sütununu DataTime tipinde güncelliyoruz
    df['Tarih'] = pd.to_datetime(df['Tarih'])

    # Yıl sütununu Tarih'in yılı olarak set ediyoruz (oluşturuyoruz)
    df['Yil'] = df['Tarih'].dt.year

    # Ay sütununu Tarih'in yılı olarak set ediyoruz (oluşturuyoruz)
    df['Ay'] = df['Tarih'].dt.month

    # Gun sütununu Tarih'in günü olarak set ediyoruz (oluşturuyoruz)
    df['Gun'] = df['Tarih'].dt.day

    # İstersek günün hangi saatinde atıldığını da alabiliriz
    #df['Zaman'] = pd.to_datetime(df['Zaman'])
    #df['Saat']=df.Zaman.apply(lambda x: x.hour)

    # Mesajdan kelimeleri ayıklıyoruz
    df['Kelimeler'] = df['Mesaj'].str.strip().str.split('[\W_]+')

    # Toplam kelime sayısı
    df['Kelime Sayisi'] = df['Kelimeler'].apply(len)

    # Mesaj karakter sayisi
    df['Mesaj Karakter Sayisi'] = df['Mesaj'].map(str).apply(len)-3

    # Mesajdan medyaları alıyoruz
    df['Medya'] = df['Mesaj'].str.contains('<Media omitted>')

    # DataFrame'i return ediyoruz
    return df
