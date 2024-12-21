import requests
from requests import Response
from requests.exceptions import RequestException, HTTPError
from io import StringIO
from csv import DictReader
import streamlit as st

@st.cache_data
def get_youbikes() -> list[dict]:
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'

    try:
        r: Response = requests.request('GET', url)
        r.raise_for_status()
    except HTTPError as e:
        raise Exception(f"伺服器有問題: {e}")
    except RequestException as e:
        raise Exception(f"連線有問題: {e}")
    except Exception as e:
        raise Exception(f"其他問題: {e}")
    else:
        st.success('下載成功')
        file: StringIO = StringIO(r.text)
        reader: DictReader = DictReader(file)
        list_reader: list[dict] = list(reader)
        return list_reader
