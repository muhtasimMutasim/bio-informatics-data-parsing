import pandas
import csv


# Gets the OTUS csv file data
def get_otus_csv():

    file = "qiimedata/OTUS.csv"

    with open(file, "r") as f:

        data = f.read()
        return data


# Reads Taxatable.csv and returns a dictionary
def taxtable_dict():

    file = "qiimedata/Taxatable.csv"

    ttable = []

    with open(file, "r") as f:

        # converts reader to list
        reader = [ i for i in csv.reader( f ) ]
        # makes variable with variable equal to first row of file
        headers = reader[0]

        values = []

        # iterates through reader objects and stores them to new list
        for num in range( 1, len(reader) ):
            line = reader[ num ]
            # print( f"{num}, { line }" )
            # one line loop that adds data with appropriate data with headers
            value = { headers[i] : line[i] for i in range(0, len(headers) ) }
            values.append( value )
        
        return values, headers


# Putting OTUS.csv into dataframe
def test_pandas():

    # For adding new row in dataframe
    values, headers = taxtable_dict()

    df = pandas.read_csv( "qiimedata/OTUS.csv")
    print( df )
    print("\n\n\n")
    # new_column_names = df[ 'Sample' ]

    # cnames = [ i for i in new_column_names ]
    # cnames.insert(0, "Samples")

    # print( cnames )
    # df2 = pandas.DataFrame( df, names=cnames )
    # print( df2 )
    

    # print( values )
    # df.loc[ -1 ] = [ str(i.values()) for i in values ]
    # df.loc[ -1 ] = values
    # df.index = df.index + 1  # shifting index
    # print( df )
    # for i in df:
    #     print(i)



def test():
    # otus_csv_data = get_otus_csv()
    # print(otus_csv_data)

    test_pandas()





def main():

    test()


if __name__ == "__main__":
    main()
