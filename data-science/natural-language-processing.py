from textblob import TextBlob

# Load dataset
df = pd.read_csv("data/reviews.csv")

# Sentiment analysis
df["polarity"] = df["review"].apply(lambda x: TextBlob(x).sentiment.polarity)
df["sentiment"] = df["polarity"].apply(lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Neutral")

print(df.head())
