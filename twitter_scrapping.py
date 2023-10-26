import streamlit as st
from PIL import Image
import snscrape.modules.twitter as sntwitter
import pandas as pd


# Function to scrape Twitter data
def scrape_twitter_data(keyword, start_date, end_date, tweet_limit):
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(keyword + ' since:' + start_date + ' until:' + end_date).get_items():
        tweets.append({
            'date': tweet.date.strftime('%Y-%m-%d %H:%M:%S'),  # Format date as string
            'id': tweet.id,
            'url': tweet.url,
            'content': tweet.content,
            'user': tweet.user.username,
            'reply_count': tweet.replyCount,
            'retweet_count': tweet.retweetCount,
            'language': tweet.lang,
            'source': tweet.source,
            'like_count': tweet.likeCount
        })
        if len(tweets) >= tweet_limit:
            break
    return tweets

# Function to store data in MongoDB
def store_data_in_mongodb(data, keyword):
    client = MongoClient()
    db = client['twitter_data']
    collection = db[keyword]
    collection.insert_one({'keyword': keyword, 'data': data})
    client.close()

# Streamlit app
def main():
    st.title("Twitter Scraping")
    img = Image.open("Twitter-Logo-2010.png")
    st.image(img, width=450)
    
    keyword = st.text_input("Enter keyword or hashtag:")
    start_date = st.text_input("Enter start date (YYYY-MM-DD):")
    end_date = st.text_input("Enter end date (YYYY-MM-DD):")
    tweet_limit = st.number_input("Enter tweet limit:", min_value=1, step=1)

    if st.button("Scrape Twitter Data"):
        scraped_data = scrape_twitter_data(keyword, start_date, end_date, tweet_limit)
        df = pd.DataFrame(scraped_data)
        st.dataframe(df)

        if st.button("Upload to MongoDB"):
            store_data_in_mongodb(scraped_data, keyword)
            st.success("Data uploaded to MongoDB!")

        if st.button("Download as CSV"):
            csv_data = df.to_csv(index=False)
            b64 = base64.b64encode(csv_data.encode()).decode()  # Convert to base64
            href = f'<a href="data:file/csv;base64,{b64}" download="scraped_data.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("Data downloaded as CSV!")

        if st.button("Download as JSON"):
            json_data = df.to_json(orient='records')
            b64 = base64.b64encode(json_data.encode()).decode()  # Convert to base64
            href = f'<a href="data:application/json;base64,{b64}" download="scraped_data.json">Download JSON File</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("Data downloaded as JSON!")

if __name__ == '__main__':
    main()