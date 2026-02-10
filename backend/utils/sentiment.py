from textblob import TextBlob


def analyze_sentiment(text: str):
    """
    Returns sentiment label and polarity score.
    """
    if not text:
        return "Neutral", 0.0

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.1:
        return "Positive", polarity
    elif polarity < -0.1:
        return "Negative", polarity
    else:
        return "Neutral", polarity
