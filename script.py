#!/usr/bin/python3

import argparse

import lib.parse as parse
import lib.file_io as file_io


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = ''.join(
        ('Script to perform unique words search in given file.',
         '\nIf regular expression provided, than there search for ',
         'suitable lines will be performed also')))
    parser.add_argument("-r","--re", type=str,
                        help="".join(
                            ('Regular expression to search in input fi',
                             'le for. Search will be perfomed only if ',
                             'this option is set')))
    parser.add_argument("input_file", type=str,
                        help="Input file. Mandatory parameter.")
    
    options = parser.parse_args()


    data = file_io.data_input(options.input_file)

    unique_words, match_re = parse.process_the_data(data,
                                                    options.re)

    file_io.results_output(unique_words, match_re)
