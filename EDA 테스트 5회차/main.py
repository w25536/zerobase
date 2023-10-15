import json
# 채점을 위한 코드입니다. 반드시 실행해주세요.
from grading import *

with open('./datas/전국박물관미술관정보표준데이터.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)


# 1-1

import pandas as pd


fields = json_data['fields']
records = json_data['records']

# Extracting column names from 'fields'
column_names = [field['id'] for field in fields]

# Creating the DataFrame
df_target = pd.DataFrame(records, columns=column_names)

check_01_01(df_target)

# 2-1


df_target.replace("", None, inplace=True)


check_02_01(df_target)


# 2-2

type_int_col = ['어른관람료', '청소년관람료', '어린이관람료']
type_float_col = ['위도', '경도']

df_target[type_int_col] = df_target[type_int_col].fillna(0)
df_target[type_float_col] = df_target[type_float_col].fillna(0)
df_target[type_int_col] = df_target[type_int_col].astype(int)
df_target[type_float_col] = df_target[type_float_col].astype(float)


check_02_02(df_target)


drop_cols = ['소재지지번주소', '위도', '경도', '운영기관전화번호','운영기관명', '운영홈페이지', '편의시설정보', '휴관정보', 
            '관람료기타정보', '박물관미술관소개', '교통안내정보', '관리기관전화번호', '관리기관명', '제공기관코드', '제공기관명']



df_target.drop(columns=drop_cols, inplace=True)


check_02_03(df_target)


condition1 = (df_target[type_int_col] % 10 == 0)
condition2 = (df_target[type_int_col] < 100000)

combined_condition = condition1 & condition2

df_target = df_target[combined_condition.all(axis=1)]

check_02_04(df_target)


df_target = df_target[~df_target['시설명'].str.contains('휴관')]

df_target['시설명_temp'] = df_target['시설명'].str.replace(" ", "")

df_target.sort_values(by=['시설명_temp', '데이터기준일자'], inplace=True)

df_target.drop_duplicates(subset=['시설명_temp'], keep='last', inplace=True)

df_target.drop(columns=['시설명_temp'], inplace=True)

df_target.sort_index(inplace=True)

check_03_01(df_target)

def calculate_hours(start_time, end_time):
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    
    if start_time == '00:00' and end_time == '00:00':
        return 0.0
    
    hours = end_hour - start_hour + (end_minute - start_minute) / 60.0
    
    if hours > 23:
        hours = 24.0
    
    return round(hours, 2)

df_target['평일관람가능시간'] = df_target.apply(
    lambda row: calculate_hours(row['평일관람시작시각'], row['평일관람종료시각']), axis=1)

df_target['공휴일관람가능시간'] = df_target.apply(
    lambda row: calculate_hours(row['공휴일관람시작시각'], row['공휴일관람종료시각']), axis=1)

df_target.to_csv('./datas/DEBUG/df_target2.csv', index=False)

check_03_02(df_target)



df_target['소재지도로명주소'] = df_target['소재지도로명주소'].str.replace('세종특별시', '세종특별자치시')

df_target['광역'] = df_target['소재지도로명주소'].str.split().str[0]

df_target['기초'] = df_target['소재지도로명주소'].str.split().str[1]

df_target.loc[df_target['광역'] == '제주특별자치도', '기초'] = df_target['소재지도로명주소'].str.split().str[1]

df_target.loc[df_target['광역'] == '세종특별자치시', '기초'] = None

df_target['상세'] = df_target['소재지도로명주소'].apply(lambda x: " ".join(x.split()[2:]))

df_target['소재지도로명주소'] = df_target['소재지도로명주소'].str.strip()
df_target['광역'] = df_target['광역'].str.strip()
df_target['기초'] = df_target['기초'].str.strip()
df_target['상세'] = df_target['상세'].str.strip()


# def check_03_03_test(df: pd.core.frame.DataFrame):

#     condition_dict = {
#         'condition01': len(df) == 1361,
#         'condition02': df.index.is_monotonic_increasing,
#         'condition03': (df.소재지도로명주소.str.endswith(' ')).sum() == 0,
#         'condition04': df.광역.str.contains('세종특별시').sum() == 0,
#         'condition05': ((df.광역.str.contains('세종'))&(~df.기초.isna())).sum() == 0,
#         'condition06': ((df.광역.str.contains('제주'))&(df.기초.str.contains('서귀포시'))).sum() != 0,
#         'condition07': sum(col in df.columns for col in ['광역', '기초', '상세']) == 3,
#     }

    
#     return print(condition_dict.values())

df_target.to_csv('./datas/DEBUG/DEBUG_target.csv', index=False)

check_03_03(df_target)


province_dict = {
    '서울특별시': 0,
    '부산광역시': 1,
    '대구광역시': 2,
    '인천광역시': 3,
    '광주광역시': 4,
    '대전광역시': 5,
    '울산광역시': 6,
    '세종특별자치시': 7,
    '경기도': 8,
    '강원도': 9,
    '충청북도': 10,
    '충청남도': 11,
    '전라북도': 12,
    '전라남도': 13,
    '경상북도': 14,
    '경상남도': 15,
    '제주특별자치도': 16
}



df_result = df_target.groupby('광역').size().reset_index(name='박물관미술관수')

df_result['sorted_order'] = df_result['광역'].map(province_dict)

df_result = df_result.sort_values(by=['sorted_order'], ascending=[True])

df_result = df_result.drop('sorted_order', axis=1)

df_result = df_result.set_index('광역')

df_result.to_csv('./datas/DEBUG/DEBUG_result.csv', index=True)


check_04_01(df_result)


#- 광역자치단체-기초자치단체(행정시)의 박물관/미술관의 총 수가 8개인 광역-기초자치단체(행정시)를 확인하고자 합니다.
df_result = df_target.groupby(['광역', '기초']).size().reset_index(name='박물관미술관수')

#- 조건1: df_target의 '광역'과 '기초' Column(열)에 있는 광역자치단체/기초자치단체(행정시) data를 이용하여 광역자치단체-기초자치단체(행정시)별 박물관/미술관의 총 수가 8개인 곳을 찾아주세요.
df_result = df_result[df_result['박물관미술관수'] == 8]





check_04_02(df_result)

    #'condition03': df.기초.isna().sum() == 1,
    #'condition04': (df.박물관미술관수 == 8).sum() == 8,


import numpy as np 
df_filtered = df_target[(df_target['어른관람료'] != 0) & (df_target['어린이관람료'] != 0)]

# Group by '광역' and '박물관미술관구분', then calculate the mean for adult and child admission fees
df_grouped = df_filtered.groupby(['광역', '박물관미술관구분']).agg({
    '어른관람료': np.mean,
    '어린이관람료': np.mean
}).reset_index()

# Calculate the difference between average adult and child admission fees
df_grouped['관람료차이'] = df_grouped['어른관람료'] - df_grouped['어린이관람료']

# Round to the nearest integer
df_grouped['어른관람료'] = np.round(df_grouped['어른관람료']).astype(int)
df_grouped['어린이관람료'] = np.round(df_grouped['어린이관람료']).astype(int)
df_grouped['관람료차이'] = np.round(df_grouped['관람료차이']).astype(int)

# Sort by '광역' according to the province_dict
province_dict = {
    '서울특별시': 0,
    '부산광역시': 1,
    '대구광역시': 2,
    '인천광역시': 3,
    '광주광역시': 4,
    '대전광역시': 5,
    '울산광역시': 6,
    '세종특별자치시': 7,
    '경기도': 8,
    '강원도': 9,
    '충청북도': 10,
    '충청남도': 11,
    '전라북도': 12,
    '전라남도': 13,
    '경상북도': 14,
    '경상남도': 15,
    '제주특별자치도': 16
}

df_grouped['sorted_order'] = df_grouped['광역'].map(province_dict)
df_grouped = df_grouped.sort_values(by=['sorted_order', '박물관미술관구분'])
df_grouped = df_grouped.drop('sorted_order', axis=1)

# Set multi-index
df_result = df_grouped.set_index(['광역', '박물관미술관구분'])

df_result
check_04_03(df_result) 