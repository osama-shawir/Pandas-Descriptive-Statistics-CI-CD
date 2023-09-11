# -*- coding: utf-8 -*-

"""
TESTS goes here
"""
from aircraft_analytics import AircraftAnalytics  # Import your modified function

def test_aircraft_analytics():
    # Call the function and get the results
    strikes, max_damaged_part = AircraftAnalytics()
    
    # Check if the calculated values meet your expectations
    assert isinstance(strikes, dict)
    assert max_damaged_part in strikes
    assert max_damaged_part == max(strikes, key=strikes.get)
