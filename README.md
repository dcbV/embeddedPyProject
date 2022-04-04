# embeddedProject

Project belonging to the embedded project document

Python v3.10

###Packages:
- unittest
- HtmlTestRunner: pip install html-testRunner -U
- win32file: pip install pywin32

###Folder structure:
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

###Execute unittest file
1. cd testEmbProj
2. python mainUnitTests.py

###Test Results
After the execution a json file with a resume of each test case execution is generated and
an associated html file for each development function