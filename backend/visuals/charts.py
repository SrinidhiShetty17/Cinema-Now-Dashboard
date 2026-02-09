import plotly.graph_objects as go


def normalize_rating(source: str, value: str):
    """
    Convert different rating formats to a 0–100 scale.
    """
    try:
        if source == "Internet Movie Database":
            # e.g. "8.8/10"
            return float(value.split("/")[0]) * 10

        if source == "Rotten Tomatoes":
            # e.g. "87%"
            return float(value.replace("%", ""))

        if source == "Metacritic":
            # e.g. "74/100"
            return float(value.split("/")[0])

    except Exception:
        return None

    return None


def ratings_bar_chart(ratings: dict):
    sources = []
    values = []

    for source, value in ratings.items():
        normalized = normalize_rating(source, value)
        if normalized is not None:
            sources.append(source)
            values.append(normalized)

    if not sources:
        return None

    fig = go.Figure(
        data=[
            go.Bar(
                x=sources,
                y=values,
                text=[f"{v}/100" for v in values],
                textposition="auto",
            )
        ]
    )

    fig.update_layout(
        title="Ratings Comparison",
        yaxis=dict(title="Score (out of 100)", range=[0, 100]),
        xaxis=dict(title="Source"),
        height=400,
    )

    return fig
