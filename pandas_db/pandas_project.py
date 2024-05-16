from typing import Literal

from sqlalchemy import create_engine
import pandas as pd
from pandas import DataFrame

from sqlalchemy_project.constants import URL


class PandasDB:
    def __init__(self):
        self.engine = create_engine(URL)
        self.data = None
        self.data_file = 'source_data/FINAL_SPINNY_90.xlsx'
        self.data = pd.read_excel(self.data_file)
        self.data.drop_duplicates(inplace=True)

    def get_info_from_table(self):
        print(self.data.head())
        print(self.data.info())

    def send_data_to_db(self,
                        dataframe: DataFrame,
                        table_name: str,
                        if_exists: Literal["fail", "replace", "append"] = 'append'
                        ):
        dataframe.to_sql(name=table_name, con=self.engine, if_exists=if_exists)

    def create_transmission_table(self):
        transmission = self.data[['Transmission', 'Transmission_Type']]
        transmission.drop_duplicates(inplace=True)
        transmission.reset_index(inplace=True)
        transmission = transmission[['Transmission', 'Transmission_Type']]
        self.send_data_to_db(dataframe=transmission, table_name='blabla')

    def read_from_db(self, table_name: str):
        return pd.read_sql(table_name, con=self.engine)

    def create_auto_table(self):
        car_table = self.data[["Car_Name", "Transmission", "Transmission_Type"]]
        transmission = self.read_from_db('transmission')

        new_data = pd.merge(car_table, transmission, how='inner', on=["Transmission", "Transmission_Type"])
        new_data.drop(columns=["Transmission", "Transmission_Type"], inplace=True)
        new_data.drop_duplicates()

        self.send_data_to_db(new_data, 'auto')

"""
id	Car_Name	Transmission	Transmission_Type
1	Volkswagen Ameo [2016-2017] Highline 1.5L AT (D)	7-Speed	Automatic
2	Hyundai i20 Active [2015-2020] 1.2 SX	5-Speed	Manual
4	Honda WR-V VX i-VTEC	5-Speed	Manual
5	Renault Kwid 1.0 RXT AMT	5-Speed	Manual
6	Hyundai Grand i10 [2017-2020] Asta 1.2 Kappa VTVT	5-Speed	Manual
7	Hyundai Elite i20 [2014-2018] Sportz 1.2	5-Speed	Manual
"""