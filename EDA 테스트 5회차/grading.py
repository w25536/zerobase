import pandas as pd

points_list = [0] * 12

def result_deco(func):
    def wrapper(*args, **kwargs):
        global points_list
        question_no, points, result = func(*args, **kwargs)
        if result:
            points_list[question_no] = points
            print(f'정답입니다! {points}점 누적 되었습니다!')
        else:
            points_list[question_no] = 0
            print('오답입니다. 다시 한번 확인해주세요.')        

        print('현재 누적 점수:', sum(points_list), '/ 100')
        
    return wrapper

# 1-1
@result_deco
def check_01_01(df: pd.core.frame.DataFrame):
    question_no, points = 0, 10

    condition_dict = {
        'condition01': len(df) == 2117,
        'condition02': df.isna().sum().sum() == 0,
        'condition03': df.apply(lambda col: col.dtype != object, axis=0).sum() == 0,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-1
@result_deco
def check_02_01(df: pd.core.frame.DataFrame):
    question_no, points = 1, 5

    def check_str(value):
        if value == '':
            return True
        else:
            return False

    condition_dict = {
        'condition01': len(df) == 2117,
        'condition02': df.isna().sum().sum() == 9088,
        'condition03': df.apply(lambda col: col.dtype != object, axis=0).sum() == 0,
        'condition04': df.소재지지번주소.isna().sum() == 1416,
        'condition05': df.경도.isna().sum() == 1,
        'condition06': df.관람료기타정보.isna().sum() == 1391,
        'condition07': df.apply(lambda row: row.apply(check_str)).sum().sum() == 0,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-2
@result_deco
def check_02_02(df: pd.core.frame.DataFrame):
    question_no, points = 2, 5

    def check_str(value):
        if value == '':
            return True
        else:
            return False
    
    type_int_col = ['어른관람료', '청소년관람료', '어린이관람료']
    type_float_col = ['위도', '경도']

    condition_dict = {
        'condition01': len(df) == 2117,
        'condition02': df.isna().sum().sum() == 9087,
        'condition03': df[type_int_col].apply(lambda col: col.dtype == int).sum() == 3,
        'condition04': df[type_float_col].apply(lambda col: col.dtype == float).sum() == 2,
        'condition05': df.소재지지번주소.isna().sum() == 1416,
        'condition06': df.경도.isna().sum() == 0,
        'condition07': df.관람료기타정보.isna().sum() == 1391,
        'condition08': df.apply(lambda row: row.apply(check_str)).sum().sum() == 0,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-3
@result_deco
def check_02_03(df: pd.core.frame.DataFrame):
    question_no, points = 3, 5
    
    type_int_col = ['어른관람료', '청소년관람료', '어린이관람료']

    condition_dict = {
        'condition01': len(df) == 2117,
        'condition02': df.isna().sum().sum() == 0,
        'condition03': df[type_int_col].apply(lambda col: col.dtype == int).sum() == 3,
        'condition04': len(df.columns) == 11,
        'condition05': df.index.is_monotonic_increasing,
        'condition06': df.index.to_list() == list(range(0, len(df))),
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-4
@result_deco
def check_02_04(df: pd.core.frame.DataFrame):
    question_no, points = 4, 5
    
    type_int_col = ['어른관람료', '청소년관람료', '어린이관람료']

    del_idx = [176, 479, 518, 638, 967, 1832]
    condition_dict = {
        'condition01': len(df) == 2111,
        'condition02': df.isna().sum().sum() == 0,
        'condition03': df[type_int_col].apply(lambda col: col.dtype == int).sum() == 3,
        'condition04': len(df.columns) == 11,
        'condition05': df.index.is_monotonic_increasing,
        'condition06': df.index.to_list() != list(range(0, len(df))),
        'condition07': sum(idx in del_idx for idx in df.index) == 0,

    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 3-1
@result_deco
def check_03_01(df: pd.core.frame.DataFrame):
    question_no, points = 5, 10

    del_idx = [263, 1174, 1433, 1523, 1655, 1704, 1815, 1905, 1915, 2082]

    condition_dict = {
        'condition01': len(df) == 1361,
        'condition02': sum(idx in del_idx  for idx in df.index) == 0,
        'condition03': df.시설명.str.contains('휴관').sum() == 0,
        'condition04': df.index.is_monotonic_increasing,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 3-2
@result_deco
def check_03_02(df: pd.core.frame.DataFrame):
    question_no, points = 6, 10

    del_idx = [263, 1174, 1433, 1523, 1655, 1704, 1815, 1905, 1915, 2082]

    condition_dict = {
        'condition01': len(df) == 1361,
        'condition02': sum(idx in del_idx for idx in df.index) == 0,
        'condition03': df.시설명.str.contains('휴관').sum() == 0,
        'condition04': df.index.is_monotonic_increasing,
        'condition05': (df.평일관람가능시간 == 24).sum() == 42,
        'condition06': (df.공휴일관람가능시간 == 24).sum() == 41,
        'condition07': (df.공휴일관람가능시간 == 0).sum() == 220,
        'condition08': (df.평일관람가능시간 == 9.5).sum() == 13,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 3-3
@result_deco
def check_03_03(df: pd.core.frame.DataFrame):
    question_no, points = 7, 10

    condition_dict = {
        'condition01': len(df) == 1361,
        'condition02': df.index.is_monotonic_increasing,
        'condition03': (df.소재지도로명주소.str.endswith(' ')).sum() == 0,
        'condition04': df.광역.str.contains('세종특별시').sum() == 0,
        'condition05': ((df.광역.str.contains('세종'))&(~df.기초.isna())).sum() == 0,
        'condition06': ((df.광역.str.contains('제주'))&(df.기초.str.contains('서귀포시'))).sum() != 0,
        'condition07': sum(col in df.columns for col in ['광역', '기초', '상세']) == 3,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 4-1
@result_deco
def check_04_01(df: pd.core.frame.DataFrame):
    question_no, points = 8, 10
    
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
    ordered_idx = [7, 6, 2, 5, 3, 1, 4, 10, 11, 12, 14, 16, 15, 13, 9, 0, 8]
    
    condition_dict = {
        'condition01': {province: idx for idx, province in enumerate(df.index)} == province_dict,
        'condition02': (df.iloc[0] > df.iloc[1] * 4).values[0],
        'condition03': (df.iloc[0] < df.iloc[8]).values[0],
        'condition04': (df.reset_index().sort_values(by='박물관미술관수').index != ordered_idx).sum() == 0,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 4-2
@result_deco
def check_04_02(df: pd.core.frame.DataFrame):
    question_no, points = 9, 10
    
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
    
    condition_dict = {
        'condition01': df.광역.map(province_dict).is_monotonic_increasing,
        'condition02': df[(df.광역.str.contains('경기'))].기초.is_monotonic_decreasing,
        'condition03': df.기초.isna().sum() == 1,
        'condition04': (df.박물관미술관수 == 8).sum() == 8,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 4-3
@result_deco
def check_04_03(df: pd.core.frame.DataFrame):
    question_no, points = 10, 10
    
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
    
    condition_dict = {
        'condition01': df.index.get_level_values(0).map(province_dict).is_monotonic_increasing,
        'condition02': (df.index.get_level_values(1) == '사립').sum() == 2,
        'condition03': df.apply(lambda row: row.apply(lambda x: (type(x)==int) and (x%10==0))).sum().sum() == 6,
        'condition04': (df.관람료차이 < 0).sum() == 1,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 4-4
@result_deco
def check_04_04(df: pd.core.frame.DataFrame):
    question_no, points = 11, 10
    
    gallery = ['미술관', '갤러리', '아트']
    kinds = ['국립', '대학']

    condition_dict = {
        'condition01': sum(any([symbol in name for symbol in gallery]) for name in df.시설명) == len(df),
        'condition02': sum(kind in df.박물관미술관구분 for kind in kinds) == 0,
        'condition03': (df.어른관람료 > 2000).sum() == 0,
        'condition04': (df.공휴일관람가능시간 < 7).sum() == 0,
        'condition05': df.시설명.str.contains('제주').sum() == 4,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result