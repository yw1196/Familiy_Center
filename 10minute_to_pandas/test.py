import pandas as pd
import re

# 샘플 데이터프레임 생성
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Phone': ['(123)456-7890', '987-654-3210(010-1234-5678)', '555-1234567']}
df = pd.DataFrame(data)

# 새로운 데이터프레임 생성
new_df = pd.DataFrame(columns=df.columns)

# 'Phone' 열에 괄호가 있는 행들만 모아서 새로운 데이터프레임에 추가
for index, row in df.iterrows():
    if '(' in row['Phone'] and ')' in row['Phone']:

        extracted_number = re.search(r'\((.*)\)', row['Phone']).group(1)
        new_row = row.to_frame().T
        new_row['Phone'] = extracted_number
        new_df = pd.concat([new_df, new_row], ignore_index=True)

# 결과 확인
print(new_df)