import pandas as pd

def sex_ratio(base_path, file_name):
    cp = pd.read_excel(f"{base_path}{file_name}", sheet_name="결제완료")
    