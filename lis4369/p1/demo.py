import datetime as dt
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style


def get_requirements():
    print("Data Analysis 1")
    print("\nProgram Requirements:\n"
    + "1. Run demo.py.\n"
    + "2. If errors, more than likely missing installations.\n"
    + "3. Test Python package installer.\n"
    + "4. Research how to do the following installations:\n"
    + "\ta. pandas (only if missing)\n"
    + "\tb. pandas-datareader (only if missing)\n"
    + "\tc. matplotlib (only if missing)\n"
    + "5. Create at least three functions that are called by the program:"
    + "\ta. main(): calls at least two other functions.\n"
    + "\tb. get_requirements(): displays the program requirements.\n"
    + "\tc. data_analysis_1(): displays the following data.\n")

def data_analysis_1():
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime.now()

    df = pdr.DataReader(["DJIA", "SP500"], "fred", start, end)

    print("\nPrint number of records: ")

    print(df.columns)

    print("\nPrint data frame: ")
    print(df)

    print("\nPrint first five lines: ")
    print(df.head(5))

    print("\nPrint last five lines: ")
    print(df.tail(5))

    print("\nPrint first 2 lines: ")
    print(df.head(2))

    print("\nPrint last 2 lines: ")
    print(df.tail(2))

    style.use('ggplot')

    df['DJIA'].plot()
    df['SP500'].plot()
    plt.legend()
    plt.show()
