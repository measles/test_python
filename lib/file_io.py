import sys

def data_input(file_name):
    data = []
    try:
        with open(file_name, "r") as input_file:
            data = input_file.readlines()
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        exit(2)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        exit(2)

    return data

def results_output(unique_words, match_re):
    if len(unique_words) > 0:
        output_to_file(unique_words, "unique_words.txt")
        print("Found {} unique words. "
              .format(len(unique_words)),
              "Results saved to file unique_words.txt")

    if len(match_re) > 0:
        output_to_file(match_re, "match_re.txt")
        print("Found {} lines that holds text matched "
              .format(len(match_re)),
              "to the regular expression. Results saved",
              " to file match_re.txt")

def output_to_file(data, file_name):
    try:
        with open(file_name, "w+") as output_file:
            for line in data:
                output_file.write("{}\n".format(line))
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        exit(2)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        exit(2)
    
