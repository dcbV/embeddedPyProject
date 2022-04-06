# embeddedProject

###About
Code from the embedded project document v1.0 05-04-2022

###Requirements
- Python v3.10(.4)
- unittest
- html-testRunner
- pywin32

###Folder Structure:
*     embeddedPyProject-|
                        |- codeEmbProj -|                             -> Software Development code
                                        |- __init__			-> __init__ file for code
                                        |- embedded.py  	        -> code file
                                        |- main.py			-> main project file

                        |- testEmbProj -|                             -> Software Test code
                                        |- reports  -|		-> folder with test results
                                        |- testData -|		-> folder with one json file for each development function
                                        |- __init__			-> __init__ file for test
                                        |- configuration.py	        -> file with basic configuration
                                        |- mainUnitTest.py	        -> main tests file with test cases
                                        |- utils.py			-> utils for test case code				

###Run Unit Tests Script
1. To be located in the folder embeddedPyProject
2. cd testEmbProj
3. python mainUnitTests.py

###Test Results
After the execution, a json file with a resume of each test case execution is generated and
an associated html file for each development function (./testEmbProj/reports folder)