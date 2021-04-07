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

    # Created dataframe
    df = pandas.read_csv( "qiimedata/OTUS.csv")
    # Transposed data so that the first row and columns switched
    df = df.set_index('Sample').transpose()

    # print("\n\n")
    # print( list(df.columns) )
    print("\n\n")
    print("First Data Frame\n df")
    print( df )
    print("\n")

    ab = 0
    descriptions = []
    ddict = {}

    for index, row in df.iterrows():

        # Gets the name of the column
        name = f"{index}".strip()

        # Cleans data and converts to a list
        # With option to take out "NA" values
        value = next( ( list( line.values() ) for line in values if line[headers[0]] == name), None )
        value_without_na = [ i for i in value if i != "NA" and i != name ] 
        value.remove(name) # Removes name from list

        # Removes list properties from the string and replaces the commas for | character
        value = str(value).replace("[", "").replace("]", "").replace("'", "", 100).replace(",", " |", 100)
        value = f"| {value} |"
        ddict[name] = value

        # Appends to an empty list
        descriptions.append(value)
        # a = f"\n\n{value}"
        # print( a )

    # Using DataFrame.insert() to add a column named "Descriptions" to dataframe
    # df.insert(1, "Description", descriptions, True)

    # If you dont want to change the first dataframe this line
    # creates a new dataframe from the old one with reindexing
    df2 = df.reindex(['Description', *df.columns], axis=1).assign(Description=descriptions)

    print("\n\n")
    print("Second Data Frame\n df2\n\n")
    print( df2 )
    print("\n\n")

    




def test():
    # otus_csv_data = get_otus_csv()
    # print(otus_csv_data)

    test_pandas()





def main():

    test()


if __name__ == "__main__":
    main()