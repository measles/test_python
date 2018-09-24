#!/usr/bin/python3

import argparse
import logging

import lib.parse as parse
import lib.file_io as file_io


if __name__ == "__main__":
    # Parse the CLI arguments
    parser = argparse.ArgumentParser(description = ''.join(
        ('Script to perform unique words search in given file.',
         '\nIf regular expression provided, than there search for ',
         'suitable lines will be performed also')))
    parser.add_argument("-l","--log-level", type=str, help=""
                        .join(("Log level. Dafault is ERROR. Should",
                              "be one of the following:\n",
                              "DEBUG\n",
                              "INFO\n",
                              "WARNING\n",
                              "ERROR\n",
                              "CRITICAL\n")))
    parser.add_argument("-r","--re", type=str,
                        help="".join(
                            ('Regular expression to search in input fi',
                             'le for. Search will be perfomed only if ',
                             'this option is set')))
    parser.add_argument("input_file", type=str,
                        help="Input file. Mandatory parameter.")
    
    options = parser.parse_args()

    # Check loglevel settings
    log_level = options.log_level

    if log_level == None:
        log_level = ERROR
    else:
        log_level = getattr(logging, log_level.upper(), None)
        if not isinstance(log_level, int):
            raise ValueError('Invalid log level: {}'.format(options.log_level))

    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                        level=log_level,
                        filename='logs/script.log',
                        filemode="w+")
        
    logging.info("Going to get input data from file {}".format(
        options.input_file
    ))
    data = file_io.data_input(options.input_file)

    logging.info("Going to parse input data")
    unique_words, match_re = parse.process_the_data(data,
                                                    options.re)

    logging.info("Going to save results to files")
    file_io.results_output(unique_words, match_re)
