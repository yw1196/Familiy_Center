import pandas as pd
from my_functions import convert_date
from my_functions import extract_text_inside_parentheses

'''
개강 문자발송 엑셀파일 만드는 코드
2023. 12. 12. 김용운(金容雲)
'''

# 엑셀 파일 로드
excel_file_path = "C:\\excel\\start.xls"
df = pd.read_excel(excel_file_path) #엑셀 데이터프레임으로 변환


# 처리상태가 결제완료인 행만 데이터프레임으로 만들기
df_rows = df[df['처리상태'] == '결제완료']

# 12번째 열(예약자ID)값에 일련번호를 부여
df_rows['일련번호'] = df_rows.groupby(df_rows.columns[11]).cumcount()+1

#강좌명 문자열 자르기
df_rows['강좌명1'] = df_rows['예약명(강좌명)'].str[0:10]
df_rows['강좌명2'] = df_rows['예약명(강좌명)'].str[10:20]
df_rows['개강날짜'] = df['예약이용일정'].apply(convert_date)
df_rows['강의실'] = df['이용시간(장소)'].apply(extract_text_inside_parentheses)

#빈 열 만들기
df_rows['empty'] = None

#일련번호 기준으로 그룹화
df_grouped = df_rows.groupby(df_rows['일련번호'])

row_threshold = 300
base_path='C:\\excel\\test_file\\'

for group_name, group_df in df_grouped:
    for i, chunk in enumerate(range(0, len(group_df), row_threshold), start=1):
        chunk_df = group_df.iloc[chunk:chunk + row_threshold]
        output_excel_path = f'{base_path}startOfSemester_{group_name}_{i}.xlsx'
        chunk_df.to_excel(output_excel_path, index=False, header=False, columns=['예약자','휴대전화번호','empty','empty','empty','강좌명1','강좌명2','개강날짜','강의실'])
        print(f"그룹 '{group_name}'의 일부를 포함한 엑셀 파일이 {output_excel_path}로 저장되었습니다.")