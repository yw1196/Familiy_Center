import pandas as pd
from collections import Counter

base_path ="D:\\계정\\Desktop\\2024\\1기\\추가모집\\" 

cp = pd.read_excel(f"{base_path}☆추가모집총괄표.xlsx", sheet_name="결제완료")

# 결제완료 시트에서 중복된 예약자ID 리스트 생성
duple = cp[cp.duplicated(subset='예약자ID', keep=False)]['예약자ID'].tolist()

id_counts = Counter(duple)

print(f"set으로 변환한 길이: {len(set(duple))}")
print(f"duple 길이: {len(duple)}")