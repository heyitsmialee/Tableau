import numpy as np
import pandas as pd

# 특정 공정을 진행할 때, 여러 대의 설비에 제품이 나누어 투입되는 경우가 있다.
# 이때 LOT, 공정명, 설비명을 1:1:1로 유지하기 위해 설비명을 한줄로 표현하는 방법

def pivot(df):
    result = df.groupby(['LOT', '공정명'])['설비명'].agg(lambda x: ','.join(x)).reset_index()
    return result

def get_output_schema():
    return pd.DataFrame({
        'LOT': prep_string(),
        '공정명': prep_string(),
        '설비명': prep_string()
    })
