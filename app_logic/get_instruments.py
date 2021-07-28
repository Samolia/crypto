import re
import requests
import pandas as pd

BINANCE_URL = 'https://api.binance.com/api/v3/exchangeInfo'
OKEX_URL = 'https://www.okex.com/api/spot/v3/instruments'
COLUMN_NAMES = ['unify name', 'binance name', 'okex name']


def get_binance_instruments():
    """Список инструментов с binance"""
    response = requests.get(BINANCE_URL).json()
    binance_instruments = [item['symbol'] for item in response['symbols']]

    return binance_instruments


def get_okex_instruments():
    """Список инструментов с okex"""
    response = requests.get(OKEX_URL).json()
    okex_name = [item['base_currency'] for item in response]
    okex_unify = [re.sub('\W', '', item['instrument_id']) for item in response]

    return okex_name, okex_unify


def create_df_instruments():
    df1 = pd.DataFrame({
        'binance name': get_binance_instruments(),
        'unify name': get_binance_instruments()
    })
    df2 = pd.DataFrame({
        'okex name': get_okex_instruments()[0],
        'unify name': get_okex_instruments()[1]
    })
    df = df1.merge(df2, on='unify name', how='outer')[COLUMN_NAMES]
    df = df.sort_values('unify name', ignore_index=True)

    return df
