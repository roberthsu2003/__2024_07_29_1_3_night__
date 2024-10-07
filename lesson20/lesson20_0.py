import os
import pandas as pd
import json

def parse_data(filename):
    df1 = pd.read_csv(filename)
    df2 = df1.rename(columns={"trnOpDate":"乘車日",
            "staCode":"車站代碼",
            "gateInComingCnt":"進站人數",
            "gateOutGoingCnt":"出站人數"})
    with open('車站基本資料集.json',encoding='utf-8') as file:
        json_data = json.load(file)
        stations_info = pd.DataFrame(json_data,columns=['stationCode','stationName'])
        stations_info = stations_info.astype({'stationCode':'int32'})
    df3 = pd.merge(df2,stations_info,left_on='車站代碼',right_on='stationCode')
    df4 = df3.rename(columns={'stationName':'車站名稱'})
    df5 = df4.reindex(columns=['乘車日','車站名稱','進站人數','出站人數'])
    df5['乘車日'] = pd.to_datetime(df5['乘車日'].astype(str))
    return df5

def main():
    current_dir = os.getcwd()
    csv_dir = os.path.join(current_dir,'每日各站進出站人數')
    files_and_dirs = os.listdir(csv_dir)
    all_csv_files = [filename for filename in files_and_dirs if '每日各站進出站人數' in filename]
    sorted_csv_files = sorted(all_csv_files)
    all_final_dfs = [] 
    for filename in sorted_csv_files:
        abs_filename = os.path.join(csv_dir,filename)
        all_final_dfs.append(parse_data(abs_filename))
    df_done = pd.concat(all_final_dfs)
    df_done1 = df_done.set_index('乘車日')
    print(df_done1.info())


if __name__ == '__main__':
    main()