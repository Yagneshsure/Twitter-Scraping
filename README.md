# Twitter Scraping

This project is a Python-based tool for scraping Twitter data using the snscrape library. It allows you to extract various fields from Twitter, such as date, ID, URL, tweet content, user information, reply count, retweet count, language, source, and like count. The scraped data can be stored in MongoDB and displayed in a user-friendly GUI built with Streamlit.

## Skills Learned

- Python scripting
- Data collection
- MongoDB
- Streamlit
- Social media data scraping

## Problem Statement

Today, data is scattered across various social media platforms. Twitter, in particular, contains a large amount of valuable information. To obtain accurate and relevant data from Twitter, scraping is required. This project aims to scrape Twitter data and extract fields such as date, ID, URL, tweet content, user information, reply count, retweet count, language, source, and like count.

## Approach

The project is implemented in Python and utilizes the following libraries:

- snscrape: For scraping Twitter data.
- pandas: For data manipulation and analysis.
- pymongo: For interacting with MongoDB.
- streamlit: For creating the user interface.

The project follows these steps:

1. Use the snscrape library to scrape Twitter data based on the specified keyword, date range, and tweet count limit.
2. Store the scraped data in a DataFrame, which includes the required fields.
3. Display the scraped data in a table using the Streamlit GUI.
4. Provide buttons to upload the data to MongoDB and download it as CSV or JSON files.
5. If the user clicks the "Upload to MongoDB" button, the data is stored in MongoDB, associating it with the provided keyword.
6. If the user clicks the "Download as CSV" button, the data is downloaded as a CSV file.
7. If the user clicks the "Download as JSON" button, the data is downloaded as a JSON file and saved in the "scraped_data.json" file.

## How to Use

1. Install the necessary dependencies by running `pip install -r requirements.txt`.
2. Ensure you have MongoDB installed and running.
3. Run the script using `python twitter_scrapping.py`.
4. Access the Streamlit app through your web browser.
5. Enter the keyword or hashtag to search, select the date range, and specify the tweet count limit.
6. Click the "Scrape Twitter Data" button to initiate the scraping process.
7. The scraped data will be displayed in a table on the Streamlit app.
8. Click the "Upload to MongoDB" button to store the data in MongoDB.
9. Click the "Download as CSV" button to download the data as a CSV file.
10. Click the "Download as JSON" button to download the data as a JSON file and save it locally.

## Conclusion

This Twitter Scraping project provides a convenient way to extract and store Twitter data based on specific keywords and date ranges. By leveraging the snscrape library, MongoDB for data storage, and Streamlit for the user interface, it offers a streamlined and user-friendly experience for scraping and analyzing Twitter data.

Feel free to contribute, enhance, or customize this project based on your requirements!

