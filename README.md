# instagram-posts-analysis

This repository contains tools and scripts to scrape data from Instagram, clean, transform, and analyse it using a Jupyter Notebook, and visualize the results using a Streamlit web application.

With this, you can get information such as: average likes per post, amount of posts per profile, posts per date, day of week with more posts, most used hashtags and more! 

Here I used 10 brazilian book publishers as an example: https://instagram-posts-analysis-sfzwlr3tpel2fupmyzu66e.streamlit.app/

## Features:

    Instagram Scraper:
        
        Python scripts to scrape data from Instagram including user profiles, posts, number of comments, number of likes and hashtags.
        Utilizes Instaloader for data extraction.

    Data Cleaning and Analysis Notebook:
        
        Jupyter Notebook containing step-by-step instructions to clean, transform, and analyze the scraped Instagram data.
        Includes exploratory data analysis (EDA), data preprocessing techniques, and statistical analysis.

    Streamlit Data Visualization App:
        
        Interactive web application built with Streamlit to visualize the cleaned Instagram data.
        Provides intuitive visualization tools for exploring insights derived from the data analysis.

## Repository Structure:

    /scraper:
        
        Contains Python scripts for scraping Instagram data.
        
        You'll need to pip install instaloader in order to use the scraper. 
        You need to input the usernames of the profiles you want to scrape.
        You can change the period to scrape, the default is set to 120 days from your current time.
        I advise you not to use your own instagram account, it may get suspended.
        The data will be saved in a '.csv' file

    /notebook:
        
        Jupyter Notebook for data cleaning, transformation, and analysis.
        
        You'll need to change the file path to point to the '.csv' file created by the scraper in order to read it.
        After that, you can just run the notebook and your data will be ready for the streamlit app.

    /streamlit_app:
        
        Streamlit web application for data visualization.
        
        You'll need to pip install streamlit
        Same as the notebook, you'll need to change the file path to point to the '.csv' files needed to run the app.
        after that, just run 'streamlit run streamlit_app.py' in your terminal.

    /dataframes:
        
        The dataframes I used as an example.
  

## Usage:

    This repository can be used to scrape, clean, analyse and visualize data from specific instagram profiles, which can lead to many insights.

**Requirements:**

    Python 3.x
    Jupyter Notebook
    Instaloader
    Streamlit
    And other libraries listed on requirements.txt
    
    
Contributing:

Contributions to this project are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request.

Disclaimer:

This project is for educational and research purposes only. Please make sure to comply with Instagram's terms of service and data usage policies when using the scraper.

Contact:

For any questions or inquiries, please contact gabrielangelosiq@gmail.com.





