import re

def convert_date(date_range_str):
    # 날짜 부분을 추출 (시작 날짜만 고려)
    start_date_str = date_range_str.split(' ')[0]
    
    # 월, 일, 요일 추출
    month = int(start_date_str.split('-')[1])
    day = int(start_date_str.split('-')[2])
    day_of_week = date_range_str.split('(')[1].split(')')[0]

    # 새로운 형식으로 조합
    formatted_date = f'{month}월 {day}일({day_of_week})'

    return formatted_date

def extract_text_inside_parentheses(input_string):
    # 정규 표현식을 사용하여 괄호 안의 문자열 추출
    matches = re.findall(r'\((.*?)\)', input_string)
    
    result_string=''.join(matches)
    # 추출된 문자열 반환
    return result_string

print(extract_text_inside_parentheses('00:00 ~ 00:00(시청각실)'))