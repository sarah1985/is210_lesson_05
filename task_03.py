#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Transforming Data"""

def celsius_to_fahrenheit(temperature):

    Fahrenheit = (9*temperature/5) + 32
    return float(Fahrenheit)

def fahrenheit_to_celsius(temperature):

    Celsius = 5*(temperature - 32)/9
    return float(Celsius)

def convert_temperature(temperature, output_format = 'c'):

    if output_format == 'c':
        Celsius = fahrenheit_to_celsius(temperature)
        return Celsius

    elif output_format == 'f':
        Fahrenheit = celsius_to_fahrenheit(temperature)
        return Fahrenheit

    else:
        return None