"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
import polars as pl
from matplotlib.figure import Figure
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def plot_wordcloud(df:pl.Dataframe)-> Figure:
    problems_gbr = list(
    df.filter(
        (pl.col("country") == "GBR") 
        & (pl.col("repair_status") == "End of life")
    )["problem"]
    .drop_nulls()
    )

    wordcloud = WordCloud(
        background_color = "white",
        stopwords = set(STOPWORDS),
        collocation_threshold=1,
        colormap = plt.cm.Dark2,
        scale = 3,
        random_state = 42,
    ).generate(" ".join(problems_gbr))

    fig, ax = plt.subplots(figsize=(10,8))
    ax.imshow(wordcloud)
    ax.axis("off")

    return fig