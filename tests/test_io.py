import unittest
import os
import lib.file_io as file_io
'''
Tests for IO lib
'''

class IO(unittest.TestCase):
    def tearDown(self):
        '''Remove temporary output file'''
        if os.path.isfile("test.out"):
            os.remove("test.out")
        
    def test_that_output_is_equal_to_input(self):
        '''Test to ensure that saved to file is save what was saved'''
        
        test_data = ["tef sdfs sdfsdf sdfsf",
                     "dqoinf n2f892f32f",
                     "3209fj2309j 2 3 jfsjf s",
                     "jf23c923 23 3j0,s s, .s s"]
        file_io.output_to_file(test_data, "test.out")
        saved_data = file_io.data_input("test.out")
        self.assertEqual( saved_data, test_data,
                         "Saved data differs from the one we want to save!")
