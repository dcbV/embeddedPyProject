"""
File: mainUnitTest.py
Description: execute all test cases
"""

import os.path
import configuration
import utils
import sys

import unittest
import HtmlTestRunner

sys.path.append('../../embeddedPyProject')
from codeEmbProj.embedded import *


class Test_compare_to_pattern_list(unittest.TestCase):
    test_set = "Test_compare_to_pattern_list"
    data = utils.getFromJson('./testData/' + test_set + '.json')
    results = {}

    @classmethod
    def setUpClass(cls) -> None:
        """
        This method will be executed before the test file

        :param: None
        :return: None
        """

        cls.test_data = utils.getData(cls.data, cls.test_set)

        if not os.path.exists(configuration.report_folder):
            try:
                os.mkdir(configuration.report_folder)
            except OSError:
                print("Creation of the directory %s failed" % configuration.report_folder)
            else:
                print("Successfully created the directory %s " % configuration.report_folder)

    @classmethod
    def tearDownClass(cls) -> None:
        utils.test2XmlReport(configuration.report_folder, cls.test_set, cls.results)

    def test_when_only_one_value_repeated(self) -> None:
        """
        This method test compare_to_pattern_list function with one value repeated

        :param: None
        :return: None
        """

        test_name = 'test_when_only_one_value_repeated'

        test = self.test_data[test_name]
        output = compare_to_pattern_list(test['in']['in1'], test['in']['in2'])
        if test['out']['out1'] == "None":
            test['out']['out1'] = None
        try:
            self.assertEqual(test['out']['out1'], output)
        except:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "fail"))
            raise
        else:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "pass"))

    def test_when_more_than_one_value_repeated(self) -> None:
        """
        This method test compare_to_pattern_list function with more than one value repeated

        :param: None
        :return: None
        """

        test_name = 'test_when_more_than_one_value_repeated'

        test = self.test_data[test_name]
        output = compare_to_pattern_list(test['in']['in1'], test['in']['in2'])
        if test['out']['out1'] == "None":
            test['out']['out1'] = None
        try:
            self.assertEqual(test['out']['out1'], output)
        except:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "fail"))
            raise
        else:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "pass"))

    def test_without_pattern(self) -> None:
        """
        This method test compare_to_pattern_list function with more than one value repeated

        :param: None
        :return: None
        """

        test_name = 'test_without_pattern'

        test = self.test_data[test_name]
        output = compare_to_pattern_list(test['in']['in1'], test['in']['in2'])
        if test['out']['out1'] == "None":
            test['out']['out1'] = None
        try:
            self.assertEqual(test['out']['out1'], output)
        except:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "fail"))
            raise
        else:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "pass"))

    def test_without_repeated_value(self) -> None:
        """
        This method test compare_to_pattern_list function with more than one value repeated

        :param: None
        :return: None
        """

        test_name = 'test_without_repeated_value'

        test = self.test_data[test_name]
        output = compare_to_pattern_list(test['in']['in1'], test['in']['in2'])
        if test['out']['out1'] == "None":
            test['out']['out1'] = None
        try:
            self.assertEqual(test['out']['out1'], output)
        except:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "fail"))
            raise
        else:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "pass"))


class Test_search_file_meet(unittest.TestCase):
    test_set = "Test_search_file_meet"
    data = utils.getFromJson('./testData/' + test_set + '.json')
    test_samples = './testData/Test_search_file_meet_samples/'
    results = {}

    @classmethod
    def setUpClass(cls) -> None:
        """
        This method will be executed before the test file

        :param: None
        :return: None
        """

        cls.test_data = utils.getData(cls.data, cls.test_set)

        if not os.path.exists(configuration.report_folder):
            try:
                os.mkdir(configuration.report_folder)
            except OSError:
                print("Creation of the directory %s failed" % configuration.report_folder)
            else:
                print("Successfully created the directory %s " % configuration.report_folder)

    @classmethod
    def tearDownClass(cls) -> None:
        utils.test2XmlReport(configuration.report_folder, cls.test_set, cls.results)

    def setUp(self) -> None:
        if not os.path.exists(self.test_samples):
            try:
                os.mkdir(self.test_samples)
            except OSError:
                print("Creation of the directory %s failed" % self.test_samples)
            else:
                print("Successfully created the directory %s " % self.test_samples)

    def test_with_not_files(self) -> None:
        """
        This method test search_file_meet function without files

        :param: None
        :return: None
        """

        test_name = 'test_with_not_files'

        utils.createFiles(self.test_samples, None)

        test = self.test_data[test_name]
        output = search_file_meet(test['in']['in1'])
        if test['out']['out1'] == "None":
            test['out']['out1'] = None
        try:
            self.assertEqual(test['out']['out1'], output)
        except:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "fail"))
            raise
        else:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "pass"))

        utils.deleteFolder(self.test_samples, None)

    def test_with_on_file_executable_meet(self) -> None:
        """
        This method test search_file_meet function with one file that meets the conditions

        :param: None
        :return: None
        """

        test_name = 'test_with_on_file_executable_meet'

        newfiles = {"file1.txt": 'dummy', "file2.exe": 'dummy'}

        utils.createFiles(self.test_samples, newfiles)

        test = self.test_data[test_name]
        output = search_file_meet(test['in']['in1'])
        if test['out']['out1'] == "None":
            test['out']['out1'] = None
        try:
            self.assertEqual(test['out']['out1'], output)
        except:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "fail"))
            raise
        else:
            self.results.update(utils.savelastresults(self.test_data, test_name, output, "pass"))

        utils.deleteFolder(self.test_samples, newfiles)


class Test_coin_permutations(unittest.TestCase):
    test_set = "Test_coin_permutations"
    data = utils.getFromJson('./testData/' + test_set + '.json')
    results = {}

    @classmethod
    def setUpClass(cls) -> None:
        """
        This method will be executed before the test file

        :param: None
        :return: None
        """

        cls.test_data = utils.getData(cls.data, cls.test_set)

        if not os.path.exists(configuration.report_folder):
            try:
                os.mkdir(configuration.report_folder)
            except OSError:
                print("Creation of the directory %s failed" % configuration.report_folder)
            else:
                print("Successfully created the directory %s " % configuration.report_folder)

    @classmethod
    def tearDownClass(cls) -> None:
        utils.test2XmlReport(configuration.report_folder, cls.test_set, cls.results)

    def test_sequence_empty(self) -> None:
        """
        This method test coin_permutations function with a empty sequence

        :param: None
        :return: None
        """

        test_name = 'test_sequence_empty'

        test = self.test_data[test_name]
        _, permutations = coin_permutations(test['in']['in1'])
        if test['out']['out1'] == "None":
            test['out']['out1'] = None
        try:
            self.assertEqual(test['out']['out1'], permutations)
        except:
            self.results.update(utils.savelastresults(self.test_data, test_name, permutations, "fail"))
            raise
        else:
            self.results.update(utils.savelastresults(self.test_data, test_name, permutations, "pass"))

    def test_sequence_with_permutations(self) -> None:
        """
        This method test coin_permutations function with a sequence where it is necessary to make permutations (2)

        :param: None
        :return: None
        """

        test_name = 'test_sequence_with_permutations'

        test = self.test_data[test_name]
        _, permutations = coin_permutations(test['in']['in1'])
        if test['out']['out1'] == "None":
            test['out']['out1'] = None
        try:
            self.assertEqual(test['out']['out1'], permutations)
        except:
            self.results.update(utils.savelastresults(self.test_data, test_name, permutations, "fail"))
            raise
        else:
            self.results.update(utils.savelastresults(self.test_data, test_name, permutations, "pass"))

    def test_sequence_with_all_ones(self) -> None:
        """
        This method test coin_permutations function with a sequence where all the values are ones

        :param: None
        :return: None
        """

        test_name = 'test_sequence_with_all_ones'

        test = self.test_data[test_name]
        _, permutations = coin_permutations(test['in']['in1'])
        if test['out']['out1'] == "None":
            test['out']['out1'] = None
        try:
            self.assertEqual(test['out']['out1'], permutations)
        except:
            self.results.update(utils.savelastresults(self.test_data, test_name, permutations, "fail"))
            raise
        else:
            self.results.update(utils.savelastresults(self.test_data, test_name, permutations, "pass"))

if __name__ == "__main__":
    """
    Main function
    """

    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output=configuration.report_folder),
        failfast=False, buffer=False, catchbreak=False, exit=False)
