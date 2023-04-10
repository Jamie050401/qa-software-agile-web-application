#!/bin/python3

#################################################################################################
# Program:  Python / SQLite Web Application                                                     #
# Filename: test_functions.py                                                                   #
# Author:   Jamie Allen                                                                         #
# Course:   BSc Digital Technology and Solutions                                                #
# Module:   Software Engineering and Agile                                                      #
# Version:  1.0                                                                                 #
#################################################################################################

from web import functions

class TestGetUserProfileImage:
    def test_one(self):
        assert functions.get_user_profile_image(3) == "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/baby-yoda-grogu-boba-fett-1643800811.jpg"

class TestGetDifferenceBetweenDates:
    def test_one_seconds(self):
        earlier_date = "2021-01-01 00:00:00"
        later_date = "2021-01-01 00:00:10"
        assert functions.get_difference_between_dates(earlier_date, later_date) == "10s"

    def test_two_minutes(self):
        earlier_date = "2021-01-01 00:00:00"
        later_date = "2021-01-01 00:10:00"
        assert functions.get_difference_between_dates(earlier_date, later_date) == "10m"

    def test_two_hours(self):
        earlier_date = "2021-01-01 00:00:00"
        later_date = "2021-01-01 02:00:00"
        assert functions.get_difference_between_dates(earlier_date, later_date) == "2h"

    def test_three_days(self):
        earlier_date = "2021-01-01 00:00:00"
        later_date = "2021-01-03 00:00:00"
        assert functions.get_difference_between_dates(earlier_date, later_date) == "2d"

    def test_four_weeks(self):
        earlier_date = "2021-01-01 00:00:00"
        later_date = "2021-01-14 00:00:00"
        assert functions.get_difference_between_dates(earlier_date, later_date) == "2w"

    def test_five_months(self):
        earlier_date = "2021-01-01 00:00:00"
        later_date = "2021-02-01 00:00:01"
        assert functions.get_difference_between_dates(earlier_date, later_date) == ">1M"

#################################################################################################
# File: test_functions.py                                                                       #
#                                                                                               #
# Disclaimer: The following source code is the sole work of the author unless otherwise stated. #
#                                                                                               #
# Copyright (c) Jamie Allen. All Rights Reserved.                                               #
#################################################################################################
