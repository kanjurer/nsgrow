"""
Purpose of the file is to store all the configurations at one place.
Variables beginning with __ are private and should not be used outside this file.
"""

import os

# root dir
__ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

"""
Configuration begins here...
"""
# Clean up files after notebook run
CLEAN_UP = True
AUTO_OUTPUT_FOLDER = True

# relative folder paths
DATA_PATH = os.path.join(__ROOT_DIR, '../data')
OUTPUT_PATH = os.path.join(__ROOT_DIR, '../output')

# data filenames
__POPULATION_FILENAME = "1710013901-noSymbol.csv"
__LAND_FILENAME = "Land Data.csv"
__FISCAL_FILENAME = "Municipal_Fiscal_Statistics__Operating_Fund_Total_Revenues_and_Expenditures_by_Municipality_20240209.csv"
__HOUSING_FILENAME = "3410013501-eng.csv"
__GDP_FILENAME = "Worldwide Annual GDPs.csv"
__INFLATION_FILENAME = "YOY Percentage Change CPI.csv"
__TAXRATES_FILENAME = "Municipal_Property_Tax_Rates_20240321.csv"
__MINWAGE_FILENAME = "Nova_Scotia_Minimum_Wage_20240402.csv"

# output filenames
__POPULATION_OUTPUT_FILENAME = "0a-population_preprocessing.csv"
__LAND_OUTPUT_FILENAME = "0b-land_preprocessing.csv"
__FISCAL_OUTPUT_FILENAME = "0c-fiscal_preprocessing.csv"
__HOUSING_OUTPUT_FILENAME = "0d-housing_preprocessing.csv"
__GDP_OUTPUT_FILENAME = "0e-gdp_preprocessing.csv"
__INFLATION_OUTPUT_FILENAME = "0f-inflation_preprocessing.csv"
__TAXRATES_OUTPUT_FILENAME = "0g-taxrates_preprocessing.csv"
__MINWAGE_OUTPUT_FILENAME = "0h-minwage_preprocessing.csv"
__MERGE_OUTPUT_FILENAME = "1-merge_processing.csv"
__BINNING_OUTPUT_FILENAME = "2-binning.csv"

"""
Configuration ends here...
"""

# data paths
POPULATION_PATH = os.path.join(DATA_PATH, __POPULATION_FILENAME)
LAND_PATH = os.path.join(DATA_PATH, __LAND_FILENAME)
FISCAL_PATH = os.path.join(DATA_PATH, __FISCAL_FILENAME)
HOUSING_PATH = os.path.join(DATA_PATH, __HOUSING_FILENAME)
GDP_PATH = os.path.join(DATA_PATH, __GDP_FILENAME)
INFLATION_PATH = os.path.join(DATA_PATH, __INFLATION_FILENAME)
MINWAGE_PATH = os.path.join(DATA_PATH, __MINWAGE_FILENAME)
TAXRATES_PATH = os.path.join(DATA_PATH, __TAXRATES_FILENAME)

# output data paths
POPULATION_OUTPUT_PATH = os.path.join(OUTPUT_PATH, __POPULATION_OUTPUT_FILENAME)
LAND_OUTPUT_PATH = os.path.join(OUTPUT_PATH, __LAND_OUTPUT_FILENAME)
FISCAL_OUTPUT_PATH = os.path.join(OUTPUT_PATH, __FISCAL_OUTPUT_FILENAME)
HOUSING_OUTPUT_PATH = os.path.join(OUTPUT_PATH, __HOUSING_OUTPUT_FILENAME)
GDP_OUTPUT_PATH = os.path.join(OUTPUT_PATH, __GDP_OUTPUT_FILENAME)
INFLATION_OUTPUT_PATH = os.path.join(OUTPUT_PATH, __INFLATION_OUTPUT_FILENAME)
TAXRATES_OUTPUT_PATH = os.path.join(OUTPUT_PATH, __TAXRATES_OUTPUT_FILENAME)
MINWAGE_OUTPUT_PATH = os.path.join(OUTPUT_PATH, __MINWAGE_OUTPUT_FILENAME)
MERGE_OUTPUT_PATH = os.path.join(OUTPUT_PATH, __MERGE_OUTPUT_FILENAME)
BINNING_OUTPUT_PATH = os.path.join(OUTPUT_PATH, __BINNING_OUTPUT_FILENAME)
