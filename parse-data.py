import pandas



def get_otus_csv():

    file = "qiimedata/OTUS.csv"

    with open(file, "r") as f:

        data = f.read()
        return data


def test_pandas():

    df = pandas.read_csv( "qiimedata/OTUS.csv" )
    print( df )


def test():
    # otus_csv_data = get_otus_csv()
    # print(otus_csv_data)

    test_pandas()




def main():

    test()


if __name__ == "__main__":
    main()
