"""
This file makes Python treat the code in the data_processing folder as a module. 
In hence, ensures that the data_processing folder is a Python package.
"""

# Lauching the pipeline by importing its function
from .pipeline import create_pipeline  # NOQA (NO Quality Assurance)