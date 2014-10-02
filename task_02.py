#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05: Compound Examples"""

from decimal import Decimal


def get_interest_rate(principal, duration, prequalification):
    """get interest rate"""

    rate = None

    if 0 <= principal < 200000:

        if 1 <= duration <= 15:
            if prequalification:
                rate = '0.0363'
            else:
                rate = '0.0465'

        elif 15 < duration <= 20:
            if prequalification:
                rate = '0.0404'
            else:
                rate = '0.0498'

        elif 20 < duration <= 30:
            if prequalification:
                rate = '0.0577'
            else:
                rate = '0.0639'

    if 200000 <= principal < 1000000:

        if 1 <= duration <= 15:
            if prequalification:
                rate = '0.0302'
            else:
                rate = '0.0398'

        elif 15 < duration <= 20:
            if prequalification:
                rate = '0.0327'
            else:
                rate = '0.0408'

        elif 20 < duration <= 30:
            if prequalification:
                rate = '0.0466'

    if principal >= 1000000:

        if 1 <= duration <= 15:
            if prequalification:
                rate = '0.0205'

        elif 15 < duration <= 20:
            if prequalification:
                rate = '0.0262'

    if rate is not None:
        return Decimal(rate)


def compound_interest(principal, duration, rate, interval=12):
    """calculate compound interest"""

    total = None

    if rate is not None:
        total = principal * (1 + (rate/12))**(12 * duration)

    return total


def calculate_total(principal, duration, prequalification):
    """calculate total"""

    total = None
    rate = get_interest_rate(principal, duration, prequalification)

    if rate:
        total = compound_interest(principal, duration, rate)

    return int(round(total))


def calculate_interest(principal, duration, prequalification):
    """calculate interest"""

    total = calculate_total(principal, duration, prequalification)

    if total:
        return total - principal

    else:
        return None