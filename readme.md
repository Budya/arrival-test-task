Environment:  
- Project created with Python 3.10  

For start tests:
    
    python -m pytest

For start test with allure reporter:

    python -m pytest --alluredir={param}

    allure serve {param}

        @param - paste path to allure directory

For changing default base_url use additional parameter:

    python -m pytest --base_url={Url}

Full example:

    python -m pytest --alluredir={param} --base_url={Url}

    allure serve {param}

        @param - paste path to allure directory

Test cases and results descriptions provided in Test_Cases.xlsx
file in the root folder of project
        