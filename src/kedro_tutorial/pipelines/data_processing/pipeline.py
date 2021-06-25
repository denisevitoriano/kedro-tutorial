"""
This file exposes the `create_pipeline` function at the top-level of the module. 
"""

# Creating a node for each function 
from kedro.pipeline import Pipeline, node

# Importing node file and its functions 
from .nodes import preprocess_companies, preprocess_shuttles

"""
Calling create_pipeline with no arguments should return an instance of a Pipeline:
"""

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
                name="preprocess_companies_node",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocess_shuttles_node",
            ),
        ]
    )

"""
`companies` and `shuttles` refer to the datasets defined in conf/base/catalog.yml. 
These are inputs to the `preprocess_companies` and `preprocess_shuttles` functions. 
The named node inputs (and outputs) are used by the pipeline to determine interdependencies between the nodes, and hence, their execution order.
"""