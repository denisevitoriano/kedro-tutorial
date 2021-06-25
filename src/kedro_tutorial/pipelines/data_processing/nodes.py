"""
This file is a location to add code for the nodes in the data_processing modular pipeline.
"""

# Importing pandas package to wrangling data
import pandas as pd


# Creating functions to wrangling data
def _is_true(x):
    return x == "t"

def _parse_percentage(x):
    x = x.str.replace("%", "")
    x = x.astype(float) / 100
    return x

def _parse_money(x):
    x = x.str.replace("$", "").str.replace(",", "")
    x = x.astype(float)
    return x


# Here there are two functions: `preprocess_companies` and `preprocess_shuttles` 
# Each function inputs a raw dataframe and outputs a dataframe containing pre-processed data
def preprocess_companies(companies: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for companies.

    Args:
        companies: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """
    companies["iata_approved"] = _is_true(companies["iata_approved"])
    companies["company_rating"] = _parse_percentage(companies["company_rating"])
    return companies

def preprocess_shuttles(shuttles: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for shuttles.

    Args:
        shuttles: Raw data.
    Returns:
        Preprocessed data, with `price` converted to a float and `d_check_complete`,
        `moon_clearance_complete` converted to boolean.
    """
    shuttles["d_check_complete"] = _is_true(shuttles["d_check_complete"])
    shuttles["moon_clearance_complete"] = _is_true(shuttles["moon_clearance_complete"])
    shuttles["price"] = _parse_money(shuttles["price"])
    return shuttles