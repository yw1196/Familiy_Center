import pandas as pd

'''
winning.py 코드를 사용하려면 OK관리자페이지에서 파일을 내려받는 작업 외에
당첨자를 수작업으로 분류하고 당첨자 시트를 만들어야하는 단점이 있어
OK관리자페이지에서 파일을 내려받은 상태에서
코드를 실행시키면 당첨자 시트와 문자 발송용 파일을 생성하는 코드를 만들고자 함

2023-12-26 코드 완성
'''

base_path ="D:\\계정\\Desktop\\2024\\1기\\추가모집\\" 
win_dates ="12. 26."

cp = pd.read_excel(f"{base_path}☆추가모집총괄표.xlsx", sheet_name="결제완료")
waiting = pd.read_excel(f"{base_path}☆추가모집총괄표.xlsx", sheet_name="대기자")
enroll = pd.read_excel(f"{base_path}☆추가모집총괄표.xlsx", sheet_name="등록현황", skiprows=2)

filtered_courses = enroll[(enroll['잔여석'] >=1) & (enroll['대기자']>=1)]
winners_series = filtered_courses.apply(lambda row: row['잔여석'] if row['잔여석'] <= row['대기자'] else row['대기자'], axis=1)
filtered_courses = filtered_courses.assign(당첨자=winners_series)

# 결제완료 시트에서 중복된 예약자ID 리스트 생성
duple = cp[cp.duplicated(subset='예약자ID', keep=False)]['예약자ID'].tolist()

winner = pd.DataFrame()

for _, row in filtered_courses.iterrows():

    win_num = int(row['당첨자'])
    count = 0
    course_name = row['강좌명']
    for _, waiting_row in waiting[waiting['예약명'] == course_name].iterrows():

        if waiting_row['ID'] not in duple:
            winner = pd.concat([winner, waiting_row.to_frame().T], ignore_index=True)
            count += 1

        if count >= win_num:
            break

with pd.ExcelWriter(f"{base_path}☆추가모집총괄표.xlsx", engine='openpyxl', mode='a') as writer:
    winner.to_excel(writer, sheet_name=f'{win_dates} 당첨자', index=False, header=True)
    print(f"{win_dates} 당첨자 시트가 ☆추가모집총괄표.xlsx에 저장됐습니다.")

winner['강좌명1'] = winner['예약명'].str[0:10]
winner['강좌명2'] = winner['예약명'].str[10:20]

winner['empty'] = None

output_excel_path = f'{base_path}{win_dates}winning.xlsx'

winner.to_excel(output_excel_path, index=False, header=False, columns=['성명','휴대전화','empty','empty','empty','강좌명1','강좌명2'])
print(f"{win_dates} 대기자 당첨 엑셀 파일이 {output_excel_path}로 저장되었습니다.")