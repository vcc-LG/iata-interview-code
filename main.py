#!/usr/local/bin/python

"""
Development initiatives

Code to retrieve GAI scores and calculate average values

"""

import csv


def get_index(file_name, iso_code):
    """
    Function to return a list of GAI scores for requested ISO
    country code, and average values of GAI index for those years
    :param file_name: The path to the CSV file
    :param iso_code: The requested ISO country code
    :return: output_data_list
             average_index
    """
    data_dict = csv.DictReader(open(file_name), delimiter=',')   #create dictionary from csv
    output_data_list = []
    for row in data_dict:
        if row['id'] == iso_code:     #if iso code matches input
            try:
                output_data_list.append([row['year'], float(row['value'])])
            except ValueError:    #typically if entry is blank or NaN
                output_data_list.append([row['year'], None])
    data_vals = [i[1] for i in output_data_list]       #extract numbers from list
    average_index = sum([i for i in data_vals if i != None]) / \
                    len(tuple(filter(lambda x: x is not None, data_vals)))   #calculate average
    return output_data_list, average_index


if __name__ == "__main__":
    input_file = 'climate-vulnerability.csv'
    my_code = 'AE'
    my_data_list, my_average = get_index(input_file, my_code)
    print("The average of all scores for {0} is {1:.2f}".format(my_code,my_average))