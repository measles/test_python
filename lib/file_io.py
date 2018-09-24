import sys
import logging

def data_input(file_name):
    data = []
    try:
        logging.info("Attempt to access file {}".format(file_name))
        with open(file_name, "r") as input_file:
            data = input_file.readlines()
        logging.info("File was opened and data were read")
    except IOError as e:
        logging.critical("I/O error({0}): {1}".format(e.errno,
                                                      e.strerror))
        exit(2)
    except:
        logging.critical("Unexpected error:", sys.exc_info()[0])
        exit(2)

    return data

def results_output(unique_words, match_re):
    if len(unique_words) > 0:
        logging.info("Found {} unique words. ".format(len(unique_words)))
        logging.info("Going to save these words to file")
        output_to_file(unique_words, "unique_words.txt")
        logging.info("Results saved to file unique_words.txt")

    if len(match_re) > 0:
        logging.info("Found {} lines that holds text matched  to RE"
              .format(len(match_re)))
        logging.info("Saving results to match_re.txt")
        output_to_file(match_re, "match_re.txt")

def output_to_file(data, file_name):
    try:
        logging.info("Attempt to access file {}".format(file_name))
        with open(file_name, "w+") as output_file:
            for line in data:
                output_file.write("{}\n".format(line))
        logging.info("Data were saved to file")
    except IOError as e:
        logging.critical("I/O error({0}): {1}".format(e.errno,
                                                      e.strerror))
        exit(2)
    except:
        logging.critical("Unexpected error:", sys.exc_info()[0])
        exit(2)
    
