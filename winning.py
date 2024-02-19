import pandas as pd

'''
대기자 당첨 처리 코드
OK관리자 페이지에서 그날 아침에 선착순, 추첨식 결제완료자 파일 및 대기자 파일 내려받은 뒤에 총괄표에 반영 후 그날 당첨자 시트 엑셀에 만들어 둔 후
코드 실행시키면 kt크로샷 그룹주소록 엑셀 양식에 맞는 엑셀파일 나옴
2023-12-20 김용운
'''

# 엑셀 파일 로드
base_path = "D:\\계정\\Desktop\\2024\\1기\\추가모집\\" 
win_dates="12. 26."
sheet_name_to_read=f'{win_dates} 당첨자'

df_rows= pd.read_excel(f"{base_path}☆추가모집총괄표.xlsx", sheet_name=sheet_name_to_read) #엑셀 데이터프레임으로 변환

#강좌명 문자열 자르기
df_rows['강좌명1'] = df_rows['예약명'].str[0:10]
df_rows['강좌명2'] = df_rows['예약명'].str[10:20]


#빈 열 만들기
df_rows['empty'] = None

output_excel_path = f'{base_path}{win_dates}winning.xlsx'


df_rows.to_excel(output_excel_path, index=False, header=False, columns=['성명','휴대전화','empty','empty','empty','강좌명1','강좌명2'])
print(f"{win_dates} 대기자 당첨 엑셀 파일이 {output_excel_path}로 저장되었습니다.")