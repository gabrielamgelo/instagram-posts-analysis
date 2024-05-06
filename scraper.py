import instaloader
import pandas as pd
from datetime import datetime, timedelta
import re

def get_posts_info(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)

    posts_info = []
    
    current_date = datetime.now()
    # Choosing the time period to scrape
    until_date = current_date - timedelta(days=30)

    for post in profile.get_posts():
        if post.date >= until_date:
            
            if post.caption is not None and post.caption.strip() != '':
                
                hashtags = re.findall(r'#(\w+)', post.caption)
            else:
                hashtags = []
            post_info = {
                'username': username,
                'likes': post.likes,
                'comments': post.comments,
                'text': post.caption,
                'hashtags': hashtags,
                'date': post.date
            }
            posts_info.append(post_info)
        else:
            break  

    return posts_info

def save_to_csv(posts_info, filename):
    df = pd.DataFrame(posts_info)
    df.to_csv(filename, index=False)
    

# ExemplE of usernames:
usernames = ['username here']  
# it's best to scrape at most 5 profiles at a time
filename = "igposts.csv"


all_posts_info = []
for username in usernames:
    posts_info = get_posts_info(username)
    all_posts_info.extend(posts_info)

save_to_csv(all_posts_info, filename)
