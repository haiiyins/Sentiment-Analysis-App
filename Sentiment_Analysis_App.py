import streamlit as st
# import subprocess
# cmd = ['python3', '-m', 'textblob.download_corpora']
# subprocess.run(cmd)
# print("Working")
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def convert_to_df(sentiment):
    sentiment_dict = {'polarity': sentiment.polarity, 'subjectivity': sentiment.subjectivity}
    sentiment_df = pd.DataFrame(sentiment_dict.items(), columns=['metric', 'value'])
    return sentiment_df

def analyze_token_sentiment(docx):
    analyzer = SentimentIntensityAnalyzer()
    pos_list = []
    neg_list = []
    neu_list = []
    for i in docx.split():
        res = analyzer.polarity_scores(i)['compound']
        if res > 0.1:
            pos_list.append(i)
            pos_list.append(res)
        elif res <= -0.1:
            neg_list.append(i)
            neg_list.append(res)
        else:
            neu_list.append(i)

    result = {'positives': pos_list, 'negatives': neg_list, 'neutral': neu_list}
    return result

def main():
    st.title("Sentiment Analysis using Natural Language Processing")
    st.subheader("ISTE-782 Visual Analytics")

    menu = ["About", "Home"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        with st.form(key='nlpForm'):
            raw_text = st.text_area("Enter the text you want to analyze here: ")
            submit_button = st.form_submit_button(label='Analyze')

        # layout
        col1, col2 = st.columns(2)
        if submit_button:
            with col1:
                st.info("Results")
                sentiment = TextBlob(raw_text).sentiment
                st.write(sentiment)

                # Sentiment
                if sentiment.polarity > 0.05:
                    st.markdown("Sentiment:: Positive :smiley: ")
                elif sentiment.polarity < 0.05:
                    st.markdown("Sentiment:: Negative :angry: ")
                else:
                    st.markdown("Sentiment:: Neutral 😐 ")

                # Dataframe
                result_df = convert_to_df(sentiment)
                st.dataframe(result_df)

                # Visualization
                c = alt.Chart(result_df).mark_bar().encode(
                    x='metric',
                    y='value',
                    color='metric')
                st.altair_chart(c, use_container_width=True)

            with col2:
                st.info("Token Sentiment")
                token_sentiments = analyze_token_sentiment(raw_text)
                st.write(token_sentiments)

    else:
        st.subheader("About")
        st.write("This website was built by a group of 4 RIT graduate students as a part of lecture presentation for the course ISTE 782 - Visual Analytics by Prof. Erik Golen")
        st.write("Got some cool feature suggestions, documentation improvements or bugs to report?")
        st.write("You may use the menu on the top right corner and click on 'Report a bug', we would be happy to address them.")
        st.write("You can find the code used to build this web app [here](https://github.com/ritvik-chebolu/Sentiment-Analysis-App).")

if __name__ == '__main__':
    main()