'''Contains functions to parse input data for the test script

Funsctions:
    process_the_data(data, regular_expression)
    look_for_re(line, regular_expression)
    find_unique(line, unique_words, non_unique_words)
'''

import re
import logging

SEPARATORS = ",.;:?! \n"
'''Symbols which can separate one word from anothers'''

def process_the_data(data, regular_expression):
    '''Main function to process the input data. All other functions 
    are intend to be called from it.
    
    Arguments:
        data(list): list of lines of input data
        regular_expression(str): string to be used as regular exspression
    Returns:
        unique_words(list): list of unique wordds found in input data
        match_re(list): list of lines that matches give RE
    '''
    
    unique_words = []
    non_unique_words = []
    match_re = []
    if regular_expression:
        logging.info("User set the RE, compiling")
        re_compiled = re.compile(regular_expression)
        logging.info("RE was compiled")
    else:
        logging.info("There was no RE set by user")
        re_compiled = None
    for line in data:
        logging.debug("Processing line <{}>".format(line))
        if re_compiled:
            logging.info(
                "Going to find out if RE matches at least part of line")
            match = look_for_re(line, re_compiled)
            if match:
                logging.info("We've got a match")
                match_re.append(line)

        logging.info("Looking for the unique words in current line")
        unique_words, non_unique_words = find_unique(line,
                                                     unique_words,
                                                     non_unique_words)

    return unique_words, match_re

def look_for_re(line, regular_expression):
    '''Check if string (or its part) matches the RE given by user.
    
    Arguments:
        line(str): line to check
        regular_expression(re object): compiled regular expression
    Returns:
        None: of nothing was found
        match object: if there was at least one match
    '''
    return regular_expression.search(line)

def find_unique(line, unique_words, non_unique_words):
    '''Find unique words in given lines. If current word found in 
    unique_words then it will be moved to non_unique_words.

    Arguments:
        line(str): line to be processed
        unique_words(list): list of unique words found before
        non_unique_words(list): list of words that is definitely
        not unique
    Returns:
        unique_words(list): updated state of unique words list
        non_unique_words(list): updated state of non unique list
    '''
    
    words = []
    word = ''
    for symbol in line:
        logging.debug("Next symbol in line is {}")
        if symbol not in SEPARATORS:
            logging.debug(
                "This is not a separator add to the current word")
            word += symbol
            logging.debug("Current word now looks like: {}".format(word))
        else:
            logging.debug("This is definitely a separator")
            if len(word):
                words.append(word)
                logging.debug(
                    "We have the {} word. Appended to the words list"
                    .format(word))
            word = ''
            logging.debug("Last word variable was cleared")

    if len(word):
        logging.debug(
            "There is the {} word left unsaved. Appended to the list"
            .format(word))
        words.append(word)

    logging.debug(
        "Checking if some words of current line looks like unique")
    for word in words:
        logging.debug("Next word is {}".format(word))
        if word not in unique_words:
            logging.debug("{} is not in the list of unique words"
                          .format(word))
            if word not in non_unique_words:
                logging.debug("".join(("The word is not listed amog ",
                                       "non-unique words. Adding to ",
                                       "the unique list")))
                unique_words.append(word)
        else:
            logging.debug("".join(("Already listed as unique. Moving ",
                                  "to list of non-unique words")))
            unique_words.remove(word)
            non_unique_words.append(word)

    return unique_words, non_unique_words
