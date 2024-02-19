import pandas as pd

'''
정기모집 후에 처리상태(결제완료, 결제대기, 탈락)에 따라 문자발송 엑셀파일 만드는 코드
2023. 12. 12. 김용운(金容雲)
'''

# 엑셀 파일 로드
excel_file_path = "C:\\excel\\lottery_results.xls"
df = pd.read_excel(excel_file_path) #엑셀 데이터프레임으로 변환

# 처리상태(7번째 열)에 따라 데이터프레임 나누기
df_rows = df[df['처리상태'] == '탈락']

# 예약자ID(5번째 열) 중복여부에 따라 일련번호(8번째 열 생성) 부여 
# 하나의 아이디로 최대 2강좌까지 예약할 수 있으므로 임의의 아이디가 처음 나타나면 일련번호 1 부여, 동일한 아이디가 또 등장하면 일련번호 2부여
df_rows['일련번호'] = df_rows.groupby(df_rows.iloc[:,4]).cumcount()+1

#강좌명 문자열 자르기
df_rows['강좌명1'] = df_rows['예약명(강좌명)'].str[0:10]
df_rows['강좌명2'] = df_rows['예약명(강좌명)'].str[10:20]

#빈 열 만들기
df_rows['empty'] = None


#일련번호 값이 같은 행끼리 묶기
df_grouped = df_rows.groupby('일련번호')

row_threshold = 300
base_path='C:\\excel\\test_file\\'

# group_name은 일련번호 숫자
for group_name, group_df in df_grouped:
    for i, chunk in enumerate(range(0, len(group_df), row_threshold), start=1):
        chunk_df = group_df.iloc[chunk:chunk + row_threshold]
        output_excel_path = f'{base_path}lose{group_name}_{i}.xlsx'
        chunk_df.to_excel(output_excel_path, index=False, header=False, columns=['예약자','휴대전화번호','empty','empty','empty','강좌명1','강좌명2']) #헤더값이 들어가기 원하지 않으면 인덱스 뒤에 header=False 추가
        print(f"그룹 '{group_name}'의 일부를 포함한 엑셀 파일이 {output_excel_path}로 저장되었습니다.")