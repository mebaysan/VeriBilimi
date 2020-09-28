import pandas as pd
import requests


def get_data():
    raw = requests.get("https://covid19.saglik.gov.tr/covid19api?getir=liste")
    raw_json = raw.json()
    DF = pd.DataFrame(raw_json)
    cols = DF.columns.tolist()
    cols.insert(1, cols.pop(cols.index('hastalarda_zaturre_oran')))
    DF = DF.reindex(columns=cols)
    DF['toplam_vaka'] = DF['toplam_vaka'].apply(lambda x: str(f'{x}')).astype('string')
    for col_name in DF.loc[:, 'gunluk_test':].columns:
        DF[f'{col_name}'] = DF[f'{col_name}'].str.replace('.', '').astype('string')
        DF[f'{col_name}'] = pd.to_numeric(DF[f'{col_name}'])

    DF.fillna(0, inplace=True)
    for col_name in DF.loc[:, 'gunluk_test':].columns:
        DF[f'{col_name}'] = DF[f'{col_name}'].astype('int')
    DF['hastalarda_zaturre_oran'] = DF['hastalarda_zaturre_oran'].str.replace(',', '.')
    DF['hastalarda_zaturre_oran'] = pd.to_numeric(DF['hastalarda_zaturre_oran'])
    DF['tarih'] = pd.to_datetime(DF['tarih'])
    return DF
