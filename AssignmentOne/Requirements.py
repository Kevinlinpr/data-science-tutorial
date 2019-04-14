import pandas as pd
from AssignmentOne.houseData import house_data_sql_connect

class Requirements:
        '''
        Requirements a:
        To most accurately reflect the conditions under which the firm will purchase the houses
        you should limit your analysis to houses that are sold under 'normal conditions'
                abstract the normal conditions part from the whole houseData in houseData.py
        '''

        NORMAL_CONDITIONS_SQL = "SELECT * FROM houses WHERE [Sale Condition]='Normal'"

        '''
        the most useful variables in housing.db is 'Gr Live Area', 'Total Bsmt SF', (2010-'Year Built')
    
    
        Requirements b:
        If you find any missing values in the relevant variables, then remove the affected observations.
                remove observation which has NULL variables under 'ground living area' 
        '''
        NOT_NULL_VARIABLES = "SELECT [Gr Liv Area],[Total Bsmt SF],[Year Built],[Sale Condition] FROM houses" \
                             " WHERE [Gr Liv Area] AND [Total Bsmt SF] AND [Year Built] AND [Sale Condition] NOT NULL"

        '''
        Requirements a and b:
        '''
        NORMAL_CONDITIONS_AND_NOT_NULL_VARIABLES_SQL = "SELECT [Gr Liv Area],[Total Bsmt SF],[Year Built],[Sale Condition] FROM houses " \
                                                       "WHERE [Gr Liv Area] AND [Total Bsmt SF] AND [Year Built] AND [Sale Condition] NOT NULL " \
                                                       "AND [Sale Condition]='Normal'"
        '''
        Perform EDA to determine which two of these features are most useful
        '''
        Question_1_SQL = "SELECT " \
                         "[Sale Condition] AS [sale condition]," \
                         "2010-[Year Built] AS [age of the house]," \
                         "[Gr Liv Area] AS [ground living area]," \
                         "[Total Bsmt SF] AS [basement size]," \
                         "[Gr Liv Area]+[Total Bsmt SF] AS [house area]," \
                         "[SalePrice] AS [sale price] " \
                         "FROM houses " \
                         "WHERE " \
                         "[Gr Liv Area] AND [Total Bsmt SF] AND [Year Built] AND [Sale Condition] NOT NULL " \
                         "AND [Sale Condition]='Normal' ORDER BY [Gr Liv Area]+[Total Bsmt SF]"

        Question_1_House_Area_SQL = "SELECT " \
                         "[Sale Condition] AS [sale condition]," \
                         "2010-[Year Built] AS [age of the house]," \
                         "[Gr Liv Area] AS [ground living area]," \
                         "[Total Bsmt SF] AS [basement size]," \
                         "[Gr Liv Area]+[Total Bsmt SF] AS [house area]," \
                         "[SalePrice] AS [sale price] " \
                         "FROM houses " \
                         "WHERE " \
                         "[Gr Liv Area] AND [Total Bsmt SF] AND [Year Built] AND [Sale Condition] NOT NULL " \
                         "AND [Sale Condition]='Normal' ORDER BY [Gr Liv Area]+[Total Bsmt SF]"

        Question_1_Living_Area_SQL = "SELECT " \
                                    "[Sale Condition] AS [sale condition]," \
                                    "2010-[Year Built] AS [age of the house]," \
                                    "[Gr Liv Area] AS [ground living area]," \
                                    "[Total Bsmt SF] AS [basement size]," \
                                    "[Gr Liv Area]+[Total Bsmt SF] AS [house area]," \
                                    "[SalePrice] AS [sale price] " \
                                    "FROM houses " \
                                    "WHERE " \
                                    "[Gr Liv Area] AND [Total Bsmt SF] AND [Year Built] AND [Sale Condition] NOT NULL " \
                                    "AND [Sale Condition]='Normal' ORDER BY [Gr Liv Area]"

        Question_1_Basement_Size_SQL = "SELECT " \
                                     "[Sale Condition] AS [sale condition]," \
                                     "2010-[Year Built] AS [age of the house]," \
                                     "[Gr Liv Area] AS [ground living area]," \
                                     "[Total Bsmt SF] AS [basement size]," \
                                     "[Gr Liv Area]+[Total Bsmt SF] AS [house area]," \
                                     "[SalePrice] AS [sale price] " \
                                     "FROM houses " \
                                     "WHERE " \
                                     "[Gr Liv Area] AND [Total Bsmt SF] AND [Year Built] AND [Sale Condition] NOT NULL " \
                                     "AND [Sale Condition]='Normal' ORDER BY [Total Bsmt SF]"

        Question_1_adv_SQL = "SELECT " \
                         "[Sale Condition] AS [sale condition]," \
                         "[Bldg Type] AS [type of dwelling]," \
                         "[House Style] AS [house style]," \
                         "[Overall Cond] AS [rates overall condition]," \
                         "2010-[Year Built] AS [age of the house]," \
                         "[Gr Liv Area] AS [ground living area]," \
                         "[Total Bsmt SF] AS [basement size]," \
                         "[Gr Liv Area]+[Total Bsmt SF] AS [house area]," \
                         "[SalePrice] AS [sale price] " \
                         "FROM houses " \
                         "WHERE " \
                         "[Gr Liv Area] AND [Total Bsmt SF] AND [Year Built] AND [Sale Condition] NOT NULL " \
                         "AND [Sale Condition]='Normal' ORDER BY [SalePrice]"