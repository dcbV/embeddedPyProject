"""
File: utils.py
Description: library of functions used for the execution of test cases
"""

import datetime
import os.path
import json
from datetime import datetime


def getFromJson(path: str = './') -> dict:
    """
    Returns data from json file passed by argument

    :param path: file path
    :return: data from json file
    """

    filedata = json.loads(open(path).read())
    return filedata


def getData(filedata: dict = dict, function: str = '') -> dict:
    """
    Returns data from dictionary belonging to the test cases related to a function

    :param filedata: dictionary with the data of all the test cases related to a component
    :param function: name of test function
    :return: data from dictionary related to function
    """

    rawdata = filedata[function]
    return rawdata

def createFiles(folder: str, files: dict or None) -> None:
    """
    Created files defined in the parameter function
    :param folder: folder where to save the test results xml
    :param files: list of dummy files to create and info
    :return: None
    """

    if files is not None:
        for file in files.keys():
            newfile = open(folder+file, 'a')
            newfile.write(files[file])
            newfile.close()

def deleteFolder(folder: str,  files: dict or None) -> None:
    """
    Remove files defined in the parameter function
    :param folder: folder where to delete the files
    :param files: list of dummy files to delete
    :return: None
    """

    if files is not None:
        for file in files.keys():
            os.remove(folder+file)

def savelastresults(testdata: dict, test: str, output, result: str) -> dict:
    """
    Created or modified dictionary with the data after executing the test case

    :param testdata: dictionary with the data of all the test cases related to a component
    :param test: name of the executed test
    :param output: data received after executing the test case
    :param result: test case result
    :return: None
    """

    results = {
        test:
         {
             'test_data': testdata[test],
             "out received": output,
             "result": result
         }
    }

    return results


def test2XmlReport(report_folder: str, code_file: str, testname: str, results: dict) -> None:
    """
    Created json file with the data after executing all the test cases related to a function

    :param report_folder: folder where to save the test results xml
    :param testname: test function name
    :param results: dictionary with all the test results
    :return: None
    """

    todays = datetime.now()

    date = str(todays.date()) + '_' + str(todays.hour) + '-' + str(todays.minute) + '-' + str(todays.second)

    if not os.path.isdir(report_folder):
        os.mkdir(report_folder)
    file = open(report_folder + code_file + testname + '_' + date + '.json', "a")
    json.dump(results, file, indent=4)
    file.close()