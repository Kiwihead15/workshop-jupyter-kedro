"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node

from .nodes import plot_wordcloud

def create_pipeline(**kwargs)-> Pipeline:
    return pipeline([
        node(
            func = plot_wordcloud,
            inputs = ["openrepair-0_3"],
            outputs = "wordcloud-plot",
            name = "plot_wordcloud_node",
        ),
    ])
