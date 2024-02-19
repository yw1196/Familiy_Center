import pandas as pd

'''
예약자ID가 중복되는 것에 따라 일련번호 부여하는 코드

'''

# 엑셀 파일 로드
excel_file_path = "C:\\excel\\lottery_results.xls"
df = pd.read_excel(excel_file_path)

df['일련번호'] = df.groupby(df.iloc[:,4]).cumcount()+1

numbering_path = 'C:\\excel\\numbering.xlsx'
df.to_excel(numbering_path, index=False)

