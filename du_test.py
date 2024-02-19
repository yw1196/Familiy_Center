import pandas as pd

# 엑셀 파일 로드
excel_file_path = "C:\\excel\\lottery_results.xls"
df = pd.read_excel(excel_file_path)

filtered_df = df[df.iloc[:, 6]!='예약취소']

