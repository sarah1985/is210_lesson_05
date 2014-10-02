#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01: Defining a Function"""


def bool_to_str(bvalue, short=False):
    """boolean to string conversion"""

    if bvalue and not short:
        return "Yes"

    elif bvalue and short:
        return "Y"

    elif not bvalue and not short:
        return "No"

    elif not bvalue and short:
        return "N"