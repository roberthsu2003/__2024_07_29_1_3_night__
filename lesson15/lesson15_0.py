import requests
from requests import Response
from pprint import pprint
from pydantic import BaseModel, RootModel, Field,field_validator, field_serializer
from datetime import datetime
import pandas as pd

youbike_url = 'https://data.ntpc.gov.tw/api/datasets/c51d5111-c300-44c9-b4f1-4b28b9929ca2/json?size=1000'
try:
    respons:Response = requests.request('GET',youbike_url)
    respons.raise_for_status()
except Exception:
    print("下載錯誤")
else:
    content = respons.text

class Factory(BaseModel):
    名稱: str = Field(alias='organizer')
    註冊號碼: str = Field(alias='no')
    地址: str = Field(alias='address')
    統編: str = Field(alias='tax_id_number')
    緯度: float|None = Field(alias='wgs84ax') # Field 的資料類型可以設為 xxxx:float | None
    經度: float|None = Field(alias='wgs84ay') # Field 的資料類型可以設為 xxxx:float | None
    日期: datetime = Field(alias='date')

    @field_validator('緯度', '經度', mode='before') # 先自訂驗證
    @classmethod
    def validate_coordinates(cls, value):
        if value == None:
            return None
        else:
            return round(float(value), ndigits=5)

    @field_serializer('日期')
    def date_serial(self, date: datetime) -> str:
        return date.strftime(f'中華民國{date.year-1911}年%m月%d日 %H:%M:%S')

class Companys(RootModel):
    root: list[Factory]

companys: Companys = Companys.model_validate_json(content)
companys_list = companys.model_dump()

df = pd.DataFrame(data=companys_list)
df.to_csv('companys_output.csv',index=False,encoding='utf-8')
df.to_excel('companys_output.xlsx',index=False)