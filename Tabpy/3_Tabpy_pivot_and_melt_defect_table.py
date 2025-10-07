import numpy as np
import pandas as pd

def melt_defect(df):
    df_cols = df.columns
    df_filled = df.copy()
    for col in df_cols:
        df_filled[col] = df_filled[col].fillna('KGD')

    df_pivot = df_filled.pivot_table(index=['LOT_ID', 'process_step', 'defect_class', 'defect_subclass', 'inspection_tool', 'failure_mode', 'failure_mechanism', 'defect_code', 'wafer_region', 'scrap_code'], columns='defect_name', values='defect_area', aggfunc='sum', fill_value=0)
    df_pivot.reset_index(inplace=True)

    df_melted = pd.melt(df_pivot,
                        id_vars=['LOT_ID', 'process_step', 'defect_class', 'defect_subclass', 'inspection_tool', 'failure_mode', 'failure_mechanism', 'defect_code', 'wafer_region', 'scrap_code'],
                        var_name='defect_name',
                        value_name='defect_area')

    for index, row in df_melted.iterrows():
        if row['defect_area'] == 0:
            df_melted.loc[index, 'process_step':'scrap_code'] = 'KGD'

    # Remove duplicate rows
    df_no_duplicates = df_melted.drop_duplicates()

    # Sort by 'LOT_ID'
    df_sorted = df_no_duplicates.sort_values(by='LOT_ID')

    # Filter rows where 'LOT_ID' has two 'defect_name' values, keeping only the row with the larger 'defect_area'
    def filter_rows(group):
        if len(group) == 2:
            return group.loc[group['defect_area'].idxmax()]
        else:
            return group

    result = df_sorted.groupby('LOT_ID').apply(filter_rows).reset_index(drop=True)

    return result

def get_output_schema():
    schema = {
        'LOT_ID': prep_string(),
        'process_step' : prep_string(),
        'defect_class': prep_string(),
        'defect_subclass': prep_string(),
        'inspection_tool': prep_string(),
        'failure_mode': prep_string(),
        'failure_mechanism': prep_string(),
        'defect_code': prep_string(),
        'wafer_region': prep_string(),
        'scrap_code': prep_string(),
        'defect_name': prep_string(),
        'defect_area': prep_decimal()
    }

    return pd.DataFrame(schema)

