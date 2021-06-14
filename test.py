# this is test code
import pytest
from pypair import pypair

parameters = [ [ "Brand X", "Brand Y","Brand A" ]
             , [ "NT", "2000", "XP"]
             , [ "Internal", "Modem" ]
             , ['This', 'That']
             ]

filter = {"Brand X" : ["XP"], "Brand Y" : ["NT","Modem"]}

def test_twoway():
    assert pypair(parameters,2) == [('Brand X', 'NT', 'Internal', 'This')
                                    , ('Brand X', '2000', 'Modem', 'That')
                                    , ('Brand Y', 'XP', 'Internal', 'That')
                                    , ('Brand A', 'XP', 'Modem', 'This')
                                    , ('Brand Y', 'NT', 'Modem', 'This')
                                    , ('Brand A', 'NT', 'Internal', 'That')
                                    , ('Brand Y', '2000', 'Internal', 'This')
                                    , ('Brand X', 'XP', 'Internal', 'This')
                                    , ('Brand A', '2000', 'Internal', 'This')]

def test_threeway():
    assert pypair(parameters,3) == [('Brand X', 'NT', 'Internal', 'This')
                                    , ('Brand X', 'NT', 'Modem', 'That')
                                    , ('Brand X', '2000', 'Internal', 'That')
                                    , ('Brand X', '2000', 'Modem', 'This')
                                    , ('Brand Y', 'NT', 'Internal', 'That')
                                    , ('Brand Y', 'NT', 'Modem', 'This')
                                    , ('Brand Y', '2000', 'Internal', 'This')
                                    , ('Brand Y', '2000', 'Modem', 'That')
                                    , ('Brand A', 'XP', 'Internal', 'This')
                                    , ('Brand A', 'XP', 'Modem', 'That')
                                    , ('Brand X', 'XP', 'Internal', 'That')
                                    , ('Brand X', 'XP', 'Modem', 'This')
                                    , ('Brand A', 'NT', 'Internal', 'That')
                                    , ('Brand A', 'NT', 'Modem', 'This')
                                    , ('Brand Y', 'XP', 'Internal', 'This')
                                    , ('Brand Y', 'XP', 'Modem', 'That')
                                    , ('Brand A', '2000', 'Internal', 'This')
                                    , ('Brand A', '2000', 'Modem', 'That')]

def test_filtered_twoway():
    assert pypair(parameters,2,filter) == [('Brand X', 'NT', 'Internal', 'This')
                                    ,('Brand X', '2000', 'Modem', 'That')
                                    ,('Brand Y', 'XP', 'Internal', 'That')
                                    ,('Brand A', 'XP', 'Modem', 'This')
                                    ,('Brand Y', '2000', 'Internal', 'This')
                                    ,('Brand A', 'NT', 'Internal', 'That')
                                    ,('Brand X', 'NT', 'Modem', 'This')
                                    ,('Brand A', '2000', 'Internal', 'This')]


#### TEST FOR NON Dictionary Filter ####

parameters_bool = [[['TRUE,FALSE,TRUE'], ['FALSE,FALSE,FALSE'], ['FALSE,TRUE,TRUE']],
[['TRUE,TRUE'], ['FALSE,FALSE'],['-']],
[['TRUE,TRUE'], ['FALSE,FALSE'],['-']] ]

nonDictFilter = [(['TRUE,FALSE,TRUE'], ['TRUE,TRUE'], ['-']), 
(['TRUE,FALSE,TRUE'], ['FALSE,FALSE'], ['TRUE,TRUE']), 
(['TRUE,FALSE,TRUE'], ['FALSE,FALSE'], ['FALSE,FALSE']),
 (['TRUE,FALSE,TRUE'], ['-'], ['TRUE,TRUE']),
 (['TRUE,FALSE,TRUE'], ['-'], ['TRUE,TRUE']),
 (['TRUE,FALSE,TRUE'], ['-'], ['FALSE,FALSE']),
 (['TRUE,FALSE,TRUE'], ['-'], ['FALSE,FALSE']),
 (['TRUE,FALSE,TRUE'], ['-'], ['-']),
 (['FALSE,FALSE,FALSE'], ['TRUE,TRUE'], ['TRUE,TRUE']),
 (['FALSE,FALSE,FALSE'], ['TRUE,TRUE'], ['FALSE,FALSE']),
 (['FALSE,FALSE,FALSE'], ['TRUE,TRUE'], ['-']),
 (['FALSE,FALSE,FALSE'], ['TRUE,TRUE'], ['-']),
 (['FALSE,FALSE,FALSE'], ['FALSE,FALSE'], ['TRUE,TRUE']),
 (['FALSE,FALSE,FALSE'], ['FALSE,FALSE'], ['TRUE,TRUE']),
 (['FALSE,FALSE,FALSE'], ['FALSE,FALSE'], ['FALSE,FALSE']),
 (['FALSE,FALSE,FALSE'], ['FALSE,FALSE'], ['FALSE,FALSE']),
 (['FALSE,FALSE,FALSE'], ['FALSE,FALSE'], ['-']),
 (['FALSE,FALSE,FALSE'], ['-'], ['TRUE,TRUE']),
 (['FALSE,FALSE,FALSE'], ['-'], ['FALSE,FALSE']),
 (['FALSE,TRUE,TRUE'], ['TRUE,TRUE'], ['-']),
 (['FALSE,TRUE,TRUE'], ['FALSE,FALSE'], ['TRUE,TRUE']),
 (['FALSE,TRUE,TRUE'], ['FALSE,FALSE'], ['FALSE,FALSE']),
 (['FALSE,TRUE,TRUE'], ['-'], ['TRUE,TRUE']),
 (['FALSE,TRUE,TRUE'], ['-'], ['TRUE,TRUE']),
 (['FALSE,TRUE,TRUE'], ['-'], ['FALSE,FALSE']),
 (['FALSE,TRUE,TRUE'], ['-'], ['FALSE,FALSE']),
 (['FALSE,TRUE,TRUE'], ['-'], ['-'])]


def test_nonfilter_twoway():
    assert pypair(parameters_bool,2,nonDictFilter=nonDictFilter) == [(['TRUE,FALSE,TRUE'], ['TRUE,TRUE'], ['TRUE,TRUE']), 
						(['TRUE,FALSE,TRUE'], ['FALSE,FALSE'], ['-']), 
						(['FALSE,FALSE,FALSE'], ['-'], ['-']), 
						(['FALSE,TRUE,TRUE'], ['TRUE,TRUE'], ['FALSE,FALSE']), 
						(['FALSE,TRUE,TRUE'], ['FALSE,FALSE'], ['-'])]
