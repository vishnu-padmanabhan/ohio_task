import data_layer.data_processing as dp
import pandas as pd

excel_file_name = '20210309_2020_1 - 4 (1).xls'


def load_db():
    result = dp.setup_table()
    if result:
        try:
            df = pd.read_excel(excel_file_name)
            df_agg = df.groupby('API WELL  NUMBER', as_index=False)[
                'OIL', 'GAS', 'BRINE'].sum()
            dp.load_data(df_agg)
        except Exception as e:
            print(e)
    else:
        print("Error : Table or Db is not setup yet!")


def get_data(well_number):
    data = dp.get_data(well_number)
    if data:
        return {'oil': data[1], 'gas': data[1], 'brine': data[2]}
    return data
