#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Transforming Data"""


def celsius_to_fahrenheit(temperature):
    """Celsius to Fahrenheit conversion"""

    Fahrenheit = (9*temperature/5) + 32
    return float(Fahrenheit)


def fahrenheit_to_celsius(temperature):
    """Fahrenheit to Celsius conversion"""

    Celsius = 5*(temperature - 32)/9
    return float(Celsius)


def convert_temperature(temperature, output_format='c'):
    """temperature conversion"""

    numTemp = int(temperature[:-1])
    unit = temperature.lower()[-1]
    output = None

    if output_format == 'c':
        output = fahrenheit_to_celsius(numTemp)

    elif output_format == 'f':
        output = celsius_to_fahrenheit(numTemp)

    return output