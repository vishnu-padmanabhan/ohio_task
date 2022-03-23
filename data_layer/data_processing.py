import sqlite3


def setup_table():
    result = False
    try:
        con = sqlite3.connect('ohio.db')
        cur = con.cursor()
        query = '''
                CREATE TABLE IF NOT EXISTS anual_data_tb(
                    well_number TEXT NOT NULL,
                    oil INTEGER,
                    gas INTEGER,
                    brine INTEGER
                )
            '''
        cur.execute(query)
        result = True
    except Exception as e:
        print(e)

    con.close()
    return result


def load_data(df):
    df.rename(columns={'API WELL  NUMBER': 'well_number',
                       'OIL': 'oil', 'GAS': 'gas', 'BRINE': 'brine'}, inplace=True)

    con = sqlite3.connect('ohio.db')
    df.to_sql(name='anual_data_tb', con=con, if_exists='replace', index=False)
    con.close()


def get_data(well_number):
    results = False
    try:
        con = sqlite3.connect('ohio.db')
        query = f'''select * from anual_data_tb where well_number = {well_number}'''
        cur = con.cursor()
        results = cur.execute(query).fetchall()[0]
    except Exception as e:
        print('no data')
    return results
