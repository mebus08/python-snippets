# -*- coding: utf-8 -*-
'''
    Here you can find some Functions to validate and convert ISBNs.
    It's not perfect, but it work. (I'm beginner)

    Tested under Python 3.6

    Copyright(2017)

    TODO
    # add ean check

    VERSION
    0.1  ->  Project Start

'''


def get_clear_isbn(isbn):
    '''
        Return a clear ISBN (as Str !!!)
        IN:  0-19 -852663 6
        OUT: 0198526636
    '''

    return isbn.lower().replace('-', '').replace(' ', '')


def check_isbn_10(isbn):
    '''
        Function to validate ISBN-10 Numbers
        More info at:
        https://isbn-information.com/the-10-digit-isbn.html
        Return True or False
    '''

    multi = 1
    checksumme = 0
    c_isbn = get_clear_isbn(isbn)
    for number in c_isbn[::-1]:
        if 'x' in number:
            number = number.replace('x', '10')
        summe = int(number) * multi
        checksumme = checksumme + summe
        multi += 1
    valid = checksumme % 11

    if not valid == 0:
        return False
    else:
        return True


def check_isbn_13(isbn):
    '''
        Function to validate ISBN-13 Numbers
        More info at:
        https://isbn-information.com/the-13-digit-isbn.html
        Return True or False
    '''
    summe1 = 0
    summe2 = 0
    c_isbn = get_clear_isbn(isbn)
    for number in c_isbn[0::2]:
        summe1 = summe1 + int(number)
    summe1 = summe1 * 1

    for number in c_isbn[1::2]:
        summe2 = summe2 + int(number)
    summe2 = summe2 * 3

    checksumme = summe1 + summe2
    valid = checksumme % 10

    if not valid == 0:
        return False
    else:
        return True


def convert_isbn_10_to_13(isbn):
    '''
        Convert a ISBN-10 to ISBN-13
        More info at:
        https://isbn-information.com/convert-isbn-10-to-isbn-13.html
        Return  ISBN-13 (as Int) if ISBN-10 is correct
        else
        Return 0 (as Int)
    '''
    summe1 = 0
    summe2 = 0
    if check_isbn_10(isbn):
        c_isbn = get_clear_isbn(isbn)
        isbn10 = c_isbn[0:9]
        isbn13 = '978' + isbn10
        for number in isbn13[0::2]:
            summe1 = summe1 + int(number)
        summe1 = summe1 * 1

        for number in isbn13[1::2]:
            summe2 = summe2 + int(number)
        summe2 = summe2 * 3

        remainder = (summe1 + summe2) % 10

        if remainder == 0:
            isbn13 = isbn13+'0'
        else:
            check_digit = 10 - remainder
            isbn13 = isbn13+str(check_digit)
        if check_isbn_13:
            return int(isbn13)
        else:
            return 0
    else:
        return 0
