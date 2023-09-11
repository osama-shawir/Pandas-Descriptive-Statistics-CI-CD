# -*- coding: utf-8 -*-

"""
TESTS goes here
"""
from io import StringIO
from unittest.mock import patch
from main import AircraftAnalytics

def test_AircraftAnalytics(capsys):
    # Mock the user input for the file_id
    with patch('builtins.input', return_value="1TAD7Uyc9PjByt_q13uvGXGeubXnujnUi"):
        AircraftAnalytics()
    
    # Capture the printed output
    captured = capsys.readouterr()
    output = captured.out.strip()
    
    # Assert that some expected output is present in the printed output
    assert "Dataframe Information" in output
    assert "Summary Statistics" in output
    # Add more assertions as needed
