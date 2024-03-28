import pandas as pd

'''
정기모집 신청 및 추첨이 끝난 뒤
추첨식 예약자 관리에서 해당 기수 엑셀을 다운로드 받아서
처리상태(결제완료, 결제대기, 탈락)에 따른 메시지 발송용 엑셀파일을 만드는 함수

파라미터 path = 엑셀파일 경로, status = 처리상태

파라미터 값 예시
path = D:\\계정\\Desktop\\2024\\2기\\정기모집\\
file_name = 정기모집결과.xlsx
status = '결제완료' '결제대기' '탈락'
'''
 
def draw_result_message(path,file_name,status):
    df = pd.read_excel(path+file_name)

    df_rows = df[df['처리상태'] == str(status)].copy()
    
    df_rows.loc[:, '일련번호'] = df_rows.groupby(df_rows.columns[11]).cumcount()+1
    df_rows.loc[:, '강좌명1'] = df_rows['예약명(강좌명)'].str[0:10]
    df_rows.loc[:, '강좌명2'] = df_rows['예약명(강좌명)'].str[10:20]
    df_rows['empty'] = None
    
    df_grouped = df_rows.groupby(df_rows['일련번호'])
    
    row_threshold = 300

    for group_name, group_df in df_grouped:
        for i, chunk in enumerate(range(0, len(group_df), row_threshold), start=1):
            chunk_df = group_df.iloc[chunk:chunk + row_threshold]
            output_excel_path = f'{path}{status}_{group_name}_{i}.xlsx'
            chunk_df.to_excel(output_excel_path, index=False, header=False, columns=['예약자','휴대전화번호','empty','empty','empty','강좌명1','강좌명2'])
            print(f"그룹 '{group_name}'의 일부를 포함한 엑셀 파일이 {output_excel_path}로 저장되었습니다.")


draw_result_message("C:\\excel\\","test_excel_file.xls","대기")