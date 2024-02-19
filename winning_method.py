import pandas as pd
import sys

'''
OK관리자페이지에서 당첨자(선착순 및 추첨식)파일 및 대기자 파일을 받아서
총괄표 결제완료자 시트 현행화
대기자 파일을 기수 및 날짜에 맞는 파일로 현행화한 뒤에
아래의 메서드에 적절한 파라미터 값을 넣어서 실행하면
win_dates 당첨자 시트와 당첨자 문자보낼 엑셀파일이 생성됨

파라미터 값 예시
base_path = D:\\계정\\Desktop\\2024\\1기\\추가모집\\
win_dates = "12. 26."
'''

def create_winning_excel(base_path, win_dates):
    # 엑셀 파일 읽기
    cp = pd.read_excel(f"{base_path}☆추가모집총괄표.xlsx", sheet_name="결제완료")
    waiting = pd.read_excel(f"{base_path}☆추가모집총괄표.xlsx", sheet_name="대기자")
    enroll = pd.read_excel(f"{base_path}☆추가모집총괄표.xlsx", sheet_name="등록현황", skiprows=2)

    waiting = waiting[(waiting['이용기간'].str.startswith('2024-01')) & (waiting['처리상태'] == '접수대기')]

    # 필터링된 강좌 선택
    filtered_courses = enroll[(enroll['잔여석'] >= 1) & (enroll['대기자'] >= 1)]
    winners_series = filtered_courses.apply(lambda row: row['잔여석'] if row['잔여석'] <= row['대기자'] else row['대기자'], axis=1)
    filtered_courses = filtered_courses.assign(당첨자=winners_series)

    # 결제완료 시트에서 동일한 예약자ID가 두 번 이상 있는 중복 예약자ID 리스트 생성
    duple = cp[cp.duplicated(subset='예약자ID', keep=False)]['예약자ID'].tolist()

    # 당첨자 정보를 저장할 데이터프레임
    winner = pd.DataFrame()

    # 당첨자 선정 로직
    for _, row in filtered_courses.iterrows():
        win_num = int(row['당첨자'])  # 당첨자 수
        count = 0  # 현재까지 선택된 당첨자 수
        course_name = row['강좌명']  # 강좌명

        # 대기자 목록에서 강좌명이 일치하는 행을 선택
        for _, waiting_row in waiting[waiting['예약명'] == course_name].iterrows():
            # 중복된 예약자ID가 아닌 경우에만 당첨자로 선정
            if waiting_row['ID'] not in duple:
                # 선택된 당첨자 정보를 winner에 추가
                winner = pd.concat([winner, waiting_row.to_frame().T], ignore_index=True)
                count += 1

            # 당첨자 수를 채우면 종료
            if count >= win_num:
                break
    
    try:
        # 엑셀 파일에 시트 추가
        with pd.ExcelWriter(f"{base_path}☆추가모집총괄표.xlsx", engine='openpyxl', mode='a') as writer:
            winner.to_excel(writer, sheet_name=f'{win_dates} 당첨자', index=False, header=True)
            print(f"{win_dates} 당첨자 시트가 ☆추가모집총괄표.xlsx에 저장됐습니다.")

        # 추가된 시트에서 필요한 컬럼 추출하여 새로운 엑셀 파일 생성
        winner['강좌명1'] = winner['예약명'].str[0:10]
        winner['강좌명2'] = winner['예약명'].str[10:20]
        winner['empty'] = None

        output_excel_path = f'{base_path}{win_dates}winning.xlsx'
        winner.to_excel(output_excel_path, index=False, header=False, columns=['성명', '휴대전화', 'empty', 'empty', 'empty', '강좌명1', '강좌명2'])
        print(f"{win_dates} 대기자 당첨 엑셀 파일이 {output_excel_path}로 저장되었습니다.")
    except PermissionError as e:
        print("PermissionError: 엑셀 파일을 종료 후 다시 실행해주세요.")
        print("에러 메시지: {e}")
        sys.exit(1)
# 메서드 호출
create_winning_excel("D:\\계정\\Desktop\\2024\\1기\\추가모집\\", "1. 12.")