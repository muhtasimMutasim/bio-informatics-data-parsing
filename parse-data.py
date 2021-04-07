import pandas
import csv
import sys
import os.path
from os import path

# global variable for printing new line
def pn():
    return print("\n\n")


def get_csv_data():
    """
        Function for retrieving file data
    """
    file = "qiimedata/OTUS.csv"

    with open(file, "r") as f:

        data = f.read()
        return data


def taxtable_dict():
    """
        - Reads Taxatable.csv and returns a dictionary with headers.
    """
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


def create_dataframe():
    """
    - Putting OTUS.csv into dataframe & formatting the data.
    - Taking formatted data and transposing dataframe for ideal structure.
    - Adding a new column with samples bacertia description.
    """

    # For adding new row in dataframe
    values, headers = taxtable_dict()

    # Created dataframe
    df = pandas.read_csv( "qiimedata/OTUS.csv")
    # Transposed data so that the first row and columns switched
    df = df.set_index('Sample').transpose()

    # pn
    # print( list(df.columns) )
    pn()
    print("First Data Frame\n df")
    print( df )
    pn()

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
    # Uncomment if you want to make changes to the original dataframe.
    # df.insert(1, "Description", descriptions, True)

    # If you dont want to change the first dataframe this line
    # creates a new dataframe from the old one with reindexing
    df2 = df.reindex(['Description', *df.columns], axis=1).assign(Description=descriptions)

    # pn()
    print("\nSecond Data Frame\n df2\n\n")
    print( df2 )
    pn()
    
    return df2




def write_csv():
    """
        Writes dataframe to csv.
    """
    
    try:

        if not sys.argv[1] or sys.argv[1] == "":
            error = '\n\nAn argument is required to run this script. The Argument should be the desired file name \n\n'
            error = error + " Example of how to run the script:\npython3 parse-data.py test.csv\n\n"
            sys.exit(error)
    
    except IndexError:

        error = '\n\nAn argument is required to run this script. The Argument should be the desired file name \n\n'
        error = error + " Example of how to run the script:\n\n\t python3 parse-data.py test.csv\n\n"
        sys.exit(error)

    # Checks if the qiimedata folder exists. 
    if path.isdir('qiimedata') == False:
        sys.exit('\n\n"qiimedata" Directory Does not exist. Script cant run without it. \n\n')
    
    # Checks if file with given name already exists
    file_name = "qiimedata/" + sys.argv[1]
    file_exists = path.isfile(file_name)
    print( f"\nGiven Filename {sys.argv[1]} Exists?: {file_exists}\n\n" )

    if file_exists == True:
        sys.exit("File Already exists")
    # Function creates ideal dataframe with pandas.
    df = create_dataframe()
    df.to_csv(file_name, sep=',')

    print("\n\nFile has been created successfully in the qiimedata directory\n\n")




def main():
    write_csv()


if __name__ == "__main__":
    main()