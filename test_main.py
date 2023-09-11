# -*- coding: utf-8 -*-

"""
TESTS goes here
"""
from main import AircraftAnalytics

def test_aircraft_analytics():
    strikes, max_damaged_part = AircraftAnalytics()
    
    # Check if the calculated values meet expectations
    assert isinstance(strikes, dict)
    assert max_damaged_part in strikes
    assert max_damaged_part == max(strikes, key=strikes.get)
