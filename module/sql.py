from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
import os
from pandas import DataFrame, read_csv, read_sql_table

Base = declarative_base()
db_path = str(os.getcwd()) + "\\dataset\\"



class SQL:
    # SQL module helps to create an SQL database, tables and load `CSV` file on it.
    def __init__(self, db_name:str, db_path=db_path):
        self.db_name = db_name
        self.db_path = db_path
        db_file = f'{db_path}/{db_name}.sqlite'
        self.engine = create_engine(f'sqlite:///{db_file}')
        self.Session = sessionmaker(bind=self.engine)

    def csv_reader(self, csv_name:str, sep=",", header=0):
       """
       reads an `CSV` file

       Parameters
       ----------
       csv_name: str value only
            write the `CSV` file in the directory. by default, this function reads from `dataset`
            file. if you want to change the path, you need to determine it when connecting to SQL.
            Example:
                SQL(db_name="sql", db_path="your//path")
        sep: str value only -- "," is default
            for more information, refer to read_csv documentation in Pandas
        header: int value only -- 0 is default
            for more information, refer to read_csv documentation in Pandas
        -------------------------------------------------------------------
        return: DataFrame
       """
       try:
        df = read_csv(self.db_path+csv_name, sep=sep, header=header)
        return df
       except Exception as e:
          raise e

    def create_table(
            self, 
            table_name:str=None, 
            columns=None, 
            csv_name:str=None,
            if_exists:str="replace"):
        """
        creates a table in the database.

        Parameters
        ----------
        table_name: str value only -- None
        columns: str or list -- None
        csv_name: str value only -- None
        if_exists: str value only -- "replace"
            for more information, refer to pd.DataFrame.to_sql documentation in Pandas
        """
        if csv_name is None:
            try:
                table_creation_query = "CREATE TABLE {} ({})".format(table_name, ", ".join(columns))
                self.engine.execute(table_creation_query)
            except SQLAlchemyError as e:
                print(e)
        
        else:
            if isinstance(csv_name, DataFrame):
                df.to_sql(table_name, self.engine, if_exists=if_exists)
            
            else:
                df = self.csv_reader(csv_name=csv_name)
                table_name = csv_name.split(".")[0]
                df.to_sql(table_name, self.engine, if_exists=if_exists)

    def read_table(self, table_name:str):
        """
        Reads a SQLite table and returns a Pandas DataFrame.

        Parameters
        ----------
        table_name: str
            table name in SQL database
        
        -------------------------------
        return: DataFrame
        """
        df = read_sql_table(table_name, self.engine)
        return df