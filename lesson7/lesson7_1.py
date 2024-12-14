import requests
from requests import Response, RequestException, HTTPError
from io import StringIO
from csv import DictReader

url = 'https://data.tpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'

try:

    r:Response = requests.request('GET', url)
    r.raise_for_status()
    print('下載成功')
    file:StringIO = StringIO(r.text)
    reader:DictReader = DictReader(file)
    list_reader:list[dict] = list(reader)
    for row in list_reader:
        print(row)        

except HTTPError as e:
    print(e)

except RequestException as e:
    print(e)

except Exception as e:
    print(e)

