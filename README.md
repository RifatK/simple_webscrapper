
This is simple python code that extracts the html content of a web page and stips out all html tags used 
and print out all tags along with the 5 top most tags used.

This package consits of two files.
1. simple_web_scrapper.py
2. web_scrapper_test_case.py
3. scrapper_tree_data_struct.py (not yet functional)
Instuction to run :

     The core functionality lies in simple_web_scrapper.py. In the main() of this module the first variable is 
 url = 'http://python.org/' which is defaulted to the website assigned. One can simply change this and 
 point to any desired website. Once the url is changed you can simply kick off the script by using the command :
 python simple_web_scrapper.py
 
 
2. web_scrapper_test_case.py - is simple unit test class tat consist of one class TestWebScrapper wich invokes method in 
simple_web_scrapper.py. One can test smaller html docs by providing the html string in the setUp method
and simply running the file.


