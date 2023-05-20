# -*- coding:utf-8 -*-
import requests
import pandas as pd
SERVICE_KEY = '564b7852646a686a34336f4f6c5571'

def main():
    data = None
    for j in range(1,20):
        url = f'http://openapi.seoul.go.kr:8088/{SERVICE_KEY}/json/tbLnOpendataRtmsV/{1+((j-1)*1000)}/{j*1000}'
        print(url)
        req = requests.get(url)
        content = req.json()
        con = content['tbLnOpendataRtmsV']['row']
        result = pd.DataFrame(con)
        data = pd.concat([data, result])
    data = data.reset_index(drop=True)
    data['DEAL_YMD'] = pd.to_datetime(data['DEAL_YMD'], format=("%Y%m%d"))
    data.to_csv('./data/seoul_real_estate.csv', index=False)

if __name__ == "__main__":
    main()
