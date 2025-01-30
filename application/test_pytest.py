"""
The pytest module allows a developer to test the application (app_Reddit), namely its functions which render the HTML pages. It contains the following functions:
    *test_index to test rendering of the respective page 
    *test_start to test rendering of the respective page 
"""
import pytest
from app_Reddit import app

def test_index():
    """
    The function to test rendering of the respective page 
    """
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_start():
    """
    The function to test rendering of the respective page 
    """
    response = app.test_client().get('/start')
    assert response.status_code == 200

if __name__ == "__main__":
    pytest.main()
    