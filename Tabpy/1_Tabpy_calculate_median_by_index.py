import pandas as pd
import numpy as np
import tableauhyperapi as tab_api

def calculate_median_by_index(df): #인덱스 기반으로 50개 열의 중앙값을 계산하여 median 필드를 추가
    start_index = 0
    end_index = 1
    df['median'] = df.iloc[:, start_index:end_index].apply(np.nanmedian, axis=1)
    return df[['median']]

def get_output_schema(): #출력 스키마
    schema = {"columns" : [{"name": "median", "type":"DOUBLE"}]}
    # table_definition = tab_api.TableDefinition(tab_api.TableName("Extract", "Extract"))
    return schema

def tabpy_calculate_median_by_index(df): #TabPy 함수 등록을 위한 래퍼 함수
    return calculate_median_by_index(df)