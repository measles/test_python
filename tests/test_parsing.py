import unittest
import lib.parse as parse
'''
Tests for parse lib
'''

class FindUniqueWords(unittest.TestCase):
    def test_find_uniques(self):
        '''Test to ensure that few unique words will be found '''
        results, non_unique = parse.find_unique("test,a1ph@;. d0n6",
                                               [], [])
        self.assertEqual(results,
                         ["test", "a1ph@", "d0n6"],
                         "Wrong findings!")
        self.assertEqual(non_unique,
                         [],
                         "Wrong non-unique value!")

    def test_two_occurance_of_non_unique(self):
        ''' Test to ensure that not unoque word will be found in case
        of two appearances
        '''
        results, non_unique = parse.find_unique("test,a1ph@;. d0n6! test",
                                               [], [])
        self.assertEqual(results,
                         ["a1ph@", "d0n6"],
                         "Wrong findings on double occurance!")
        self.assertEqual(non_unique,
                         ["test"],
                         "Wrong non-unique value!")

    def test_three_occurance_of_non_unique(self):
        ''' Test to ensure that not unoque word will be found in case
        of three appearances
        '''
        results, non_unique = parse.find_unique(
            'test,a1ph@;. d0n6! test.test', [], [])
        self.assertEqual(results,
                         ["a1ph@", "d0n6"],
                         "Wrong findings on triple occurance!")
        self.assertEqual(non_unique,
                         ["test"],
                         "Wrong non-unique value!")

    def test_listed_non_uniques_will_be_treat_as_so(self):
        ''' Test to ensure that word from non_unique list will be 
        treat as non unique
        '''
        results, non_unique = parse.find_unique(
            'test,a1ph@;. d0n6! \n', [], ["test"])
        self.assertEqual(results,
                         ["a1ph@", "d0n6"],
                         "Wrong findings!")
        self.assertEqual(non_unique,
                         ["test"],
                         "Wrong non-unique value!")

    def test_reoccured_unique_word_treat_as_non_unique(self):
        ''' Test to ensure that word from unique list on re-appearance 
        will be treat as non unique
        '''
        results, non_unique = parse.find_unique(
            'test,a1ph@;. d0n6! \n', ["test"], [])
        self.assertEqual(results,
                         ["a1ph@", "d0n6"],
                         "Wrong findings!")
        self.assertEqual(non_unique,
                         ["test"],
                         "Wrong non-unique value!")
        
class CommonProcessing(unittest.TestCase):
    def test_data_parsing_without_re(self):
        ''' Test data parsing in when Regular Expression is not set'''
        results, match_re = parse.process_the_data(["test-case test",
                                                    "test:set,let.get?pet",
                                                    "test!test"], None)
        self.assertEqual(results,
                         ["test-case",
                          "set",
                          "let",
                          "get",
                          "pet"], "Wrong processing results!")
        self.assertEqual(match_re,
                         [],
                         "Wrong RE matching results!")
        
    def test_data_parsing_with_re(self):
        ''' Test data parsing in when Regular Expression is set'''
        results, match_re = parse.process_the_data(["test-case test",
                                                    "test:set,let.get?pet",
                                                    "test!test"], '[dst][:!?][stm]')
        self.assertEqual(results,
                         ["test-case",
                          "set",
                          "let",
                          "get",
                          "pet"], "Wrong processing results!")
        self.assertEqual(match_re,
                         ["test:set,let.get?pet",
                          "test!test"],
                         "Wrong RE matching results!")
        
if __name__ == "__main__":
    unittest.main()
