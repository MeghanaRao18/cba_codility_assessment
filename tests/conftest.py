# conftest.py
import pytest_html
import pytest
BASE_URL = 'https://petstore.swagger.io/'

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.append(pytest_html.extras.text("Custom Summary Section"))
