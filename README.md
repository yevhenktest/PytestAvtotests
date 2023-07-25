<<<<<<< HEAD
## Overview

This project is a test automation framework for testing a website. The tests are written in Python using Selenium and Pytest frameworks. This README file contains instructions on how to run the autotests and generate a report.

## Prerequisites

To run autotests, you need to install the following software:

* **Python**
* **Selenium**
* **Pytest**

## Instructions

Before running autotests, you must execute the browser selection command:
```python
export BROWSER=chrome
```
To run all autotests, run the command:
```python
pytest
```
This will run all existing autotests, which may take a long time.

To run individual tests, use the **-m marker and specify the form on the site**. There are five different **forms** that can be tested:

* **signin:** the login form;
* **reg:** the registration form;
* **medicaltrainer:** the medical trainer form;
* **cardmessage:** the Product feedback - card message form;
* **question:** the Ask your question form.

Additionally, there are five different **localizations** available:

* **en:** the English localization of the COM instance;
* **pl:** the Polish localization of the COM instance;
* **es:** the Spanish localization of the COM instance;
* **ua:** the UA instance;
* **ru:** the Russian localization of the COM instance.

To run a specific test, use the following command format:
```python
pytest -m <form>_<localization>
```
#### For example:
```python
pytest -m signin_en
```
will run a test of filling out a login form on the KOM site in English.

To generate an HTML report in one file, add the following option to the launch command:
```python
--html=report.html --self-contained-html
```
#### For example:
```python
pytest -m signin_en --html=report.html --self-contained-html
```
will launch a test of filling out a login form on the KOM site with the generation of a report in one HTML file. The report will be saved as report.html in the same directory as the autotests.

## Conclusion

With the instructions in this README file, you should be able to run autotests for the website and generate a report. If you have any questions or issues, please contact the project team.
=======
# PytestAvtotests
Autotests for site testing
>>>>>>> 66917d03630bd1379341c2a098f7d7d8f8f5f3a4
