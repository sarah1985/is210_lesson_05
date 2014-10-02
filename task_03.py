#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Transforming Data"""


def celsius_to_fahrenheit(temperature):
    """Celsius to Fahrenheit conversion"""

    fahrenheit = (9 * temperature / 5) + 32
    return float(fahrenheit)


def fahrenheit_to_celsius(temperature):
    """Fahrenheit to Celsius conversion"""

    celsius = 5 * (temperature - 32) / 9
    return float(celsius)


def convert_temperature(temperature, output_format='c'):
    """temperature conversion"""

    num_temp = int(temperature[:-1])
    # unit = temperature.lower()[-1]
    output = None

    if output_format == 'c':
        output = fahrenheit_to_celsius(numTemp)

    elif output_format == 'f':
        output = celsius_to_fahrenheit(numTemp)

    return output