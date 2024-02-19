str='2024-01-05 (금) ~ 2024-03-22 (금)'

date_str = str[0:13]

# 날짜 부분을 추출
date_part = date_str.split('(')[0].strip()

# 월, 일, 요일 추출
month = int(date_part.split('-')[1])
day = int(date_part.split('-')[2])
day_of_week = date_str.split('(')[1].split(')')[0]

# 새로운 형식으로 조합
formatted_date = f'{month}월 {day}일({day_of_week})'

print(formatted_date)