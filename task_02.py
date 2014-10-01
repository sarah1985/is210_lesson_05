#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05: Compound Examples"""

from decimal import Decimal
import locale
locale.setlocale(locale.LC_ALL, '')

def get_interest_rate(principal, duration, prequalification):

    rate = None

    if 0 <= principal < 200000:

        if 1 <= duration <= 15:
            if prequalification:
                rate = Decimal('0.0363')
            else:
                rate = Decimal('0.0465')

        elif 15 < duration <= 20:
            if prequalification:
                rate = Decimal('0.0404')
            else:
                rate = Decimal('0.0498')

        elif 20 < duration <= 30:
            if prequalification:
                rate = Decimal('0.0577')
            else:
                rate = Decimal('0.0639')

    if 200000 <= principal < 1000000:

        if 1 <= duration <= 15:
            if prequalification:
                rate = Decimal('0.0302')
            else:
                rate = Decimal('0.0398')

        elif 15 < duration <= 20:
            if prequalification:
                rate = Decimal('0.0327')
            else:
                rate = Decimal('0.0408')

        elif 20 < duration <= 30:
            if prequalification:
                rate = Decimal('0.0466')
            else:
                rate = None

    if principal >= 1000000:

        if 1 <= duration <= 15:
            if prequalification:
                rate = Decimal('0.0205')
            else:
                rate = None

        elif 15 < duration <= 20:
            if prequalification:
                rate = Decimal('0.0262')
            else:
                rate = None

    return rate

def compound_interest(principal, duration, rate, interval = 12):

    if rate is None:
        return 'None'

    else:
        total = principal * (1 + (rate/12))**(12 * duration)
        return total

def calculate_total(principal, duration, prequalification):

    rate = get_interest_rate(principal, duration, prequalification)
    total = compound_interest(principal, duration, rate)

    if rate is None:
        return None

    else:
        return int(round(total))

def calculate_interest(principal, duration, prequalification):

    rate = get_interest_rate(principal, duration, prequalification)
    total = compound_interest(principal, duration, rate)
    interest = total - principal

    if rate is None:
        return 'None'

    else:
        return int(interest)