import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv("Dataframes/igposts_treated.csv")


#Posts by profile

color_discrete_map = {
    'editorasextante': '#FFB6C1',  
    'galerarecord': '#87CEEB',     
    'editoraelefante': '#FFD700',   
    'intrinseca': '#98FB98',        
    'plataforma21_': '#FFA07A',     
    'editoraparalela': '#F08080',   
    'veruseditora': '#ADD8E6',      
    'editorarocco': '#9370DB',      
    'editoraeuphoria': '#FF6347',   
    'editoraarqueiro': '#20B2AA',   
    'companhiadasletras': '#FFDAB9',
    'editoraaleph': '#FFA500',      
    'editorasuma': '#AFEEEE',       
    'darksidebooks': '#8FBC8F',     
    'harpercollinsbrasil': '#FF69B4' 
}

post_by_profile = df['username'].value_counts().reset_index()
post_by_profile = post_by_profile.sort_values(by='count', ascending=False)

fig_post = px.bar(post_by_profile, x='count', y='username', color='username', color_discrete_map=color_discrete_map, labels={'count': 'Post Count', 'username': 'Username'})
fig_post.update_xaxes(title_text="Total of posts")
fig_post.update_yaxes(title_text="Profile")

# Likes by profile

total_likes = df.groupby('username')['likes'].sum().reset_index().sort_values(by='likes', ascending=False)
total_likes = total_likes.sort_values(by='likes',ascending=False)

fig_likes = px.bar(total_likes, x='likes', y='username', color='username', color_discrete_map=color_discrete_map, labels={'usernane': 'Username', 'likes': 'Total Likes'})

fig_likes.update_xaxes(title_text='Total Likes')
fig_likes.update_yaxes(title_text='Profile')


# Comments by profile
total_comment = df.groupby('username')['comments'].sum().reset_index().sort_values(by='comments', ascending=False)
total_comment = total_comment.sort_values(by='comments',ascending=False)

fig_comment = px.bar(total_comment, x='comments', y='username', color='username', color_discrete_map=color_discrete_map)

fig_comment.update_xaxes(title_text='Profile')
fig_comment.update_yaxes(title_text='Total Comments')

# Number of posts by date

date_line = df['date'].value_counts().reset_index()
date_line.columns = ['date', 'Number of Posts']
date_line = date_line.sort_values(by='date')


fig_date = px.line(date_line, x='date', y='Number of Posts', color_discrete_sequence=['lightcyan'], labels={'date': 'Date'})

fig_date.update_xaxes(title_text='Date')
fig_date.update_yaxes(title_text='Total Posts')

# Posts by hour

df['hour'] = df['hour'].apply(lambda x: f'{x} h')

hours = df['hour'].value_counts().reset_index()
hours.columns = ['hour', 'Number of Posts']
hours = hours.sort_values(by='Number of Posts', ascending=True)

fig_hour = px.bar(hours, x='Number of Posts', y='hour', color='Number of Posts', color_discrete_sequence= px.colors.sequential.Blues, labels={'hour': 'Hour of Day', 'count': 'Total Posts'})

# Posts by day of week

week = df['day_of_week'].value_counts().reset_index()
week.columns = ['Day of Week', 'Number of Posts']
week = week.sort_values(by='Number of Posts', ascending=True)

fig_week = px.bar(week, x='Day of Week', y='Number of Posts', color='Day of Week', color_discrete_sequence=px.colors.qualitative.Prism)

# Average likes by day of week

like_week = df.groupby('day_of_week')['likes'].mean().round().sort_values(ascending=True)

fig_like_week = px.bar(like_week, x='likes', color='likes', color_discrete_sequence=px.colors.qualitative.Prism, labels={'likes': 'Average Likes', 'day_of_week': 'Day of Week'})

fig_like_week.update_xaxes(title_text='Day of Week')
fig_like_week.update_yaxes(title_text='Average Likes')

# Average likes by hour it was posted

like_hour = df.groupby('hour')['likes'].mean().sort_values(ascending=True).round()

fig_like_hour = px.bar(like_hour, x='likes', color='likes', color_discrete_sequence=px.colors.qualitative.Prism, labels={'likes': 'Average Likes', 'hour': 'Hour it was posted'})

fig_like_hour.update_xaxes(title_text= 'Average Likes')
fig_like_hour.update_yaxes(title_text= 'Hour it was posted')

# Average likes for post

avg_likes = int(df['likes'].mean().round())

# Average of comments for post

avg_comment = int(df['comments'].mean().round())

# Average of hashtags 

avg_hashtag = int(df['hashtag_count'].mean().round())

# Most used hashtags

import collections
import re


hashtags = ' '.join(df['hashtags']).split()
counter_hashtags = collections.Counter(hashtags)
top_200_hashtags = counter_hashtags.most_common(200)

df_top_200 = pd.DataFrame(top_200_hashtags, columns=['Hashtag', 'Times Used'])

def remove_special_characters(text):
    return re.sub(r'[^\w\sáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕàÀçÇ]', '', text)

df_top_200['Hashtag'] = df_top_200['Hashtag'].apply(remove_special_characters)

# Most liked hashtags

dfh = pd.read_csv("Dataframes/hashtags_likes.csv")


# Sidebar

st.sidebar.header("Instagram Posts Analysis")



# Select Box


option = st.sidebar.selectbox('Select subject to visualize:',
                              ['📸 Posts', '❤️ Likes', '💬 Comments', '#️⃣ Hashtags'])

## Posts

if option == '📸 Posts':
    selected_option = st.selectbox('Filter by:',
                                   ['🧑‍💼 Profile', 'Date 📈', 'Day of Week 📅', 'Hour 🕒'],
                                   key='posts_selectbox')
    if selected_option == '🧑‍💼 Profile':
        st.markdown("# Total Posts by Profile")
        st.plotly_chart(fig_post, use_container_width=True)

    elif selected_option == 'Date 📈':
        st.markdown("# Posts Posting Day")
        st.plotly_chart(fig_date, use_container_width=True)

    elif selected_option == 'Day of Week 📅':
        st.markdown("# Posts by Day of Week")
        st.plotly_chart(fig_week, use_container_width=True)

    elif selected_option == 'Hour 🕒':
        st.markdown("# Posts by Posting Hour")
        st.plotly_chart(fig_hour, use_container_width=True)

## Likes

elif option == '❤️ Likes':
    selected_option = st.selectbox('Filter by:',
                                   ['🧑‍💼 Profile', 'Day of Week 📅', 'Hour 🕒'],
                                   key='likes_selectbox')
    if selected_option == '🧑‍💼 Profile':
        st.markdown("# Total Likes by Profile")
        st.markdown("#### ***Each post received an average of {} likes.***".format(avg_likes))
        st.plotly_chart(fig_likes, use_container_width=True)
        
    elif selected_option == 'Day of Week 📅':
        st.markdown("# Average Likes by Day of Week")
        st.plotly_chart(fig_like_week, use_container_width=True)

    elif selected_option == 'Hour 🕒':
        st.markdown("# Average Likes by Posting Hour")
        st.plotly_chart(fig_like_hour, use_container_width=True)


## Comments

elif option == '💬 Comments':
    selected_option = st.selectbox('Filter by:',
                                   ['🧑‍💼 Profile'],
                                   key='comments_selectbox')
    if selected_option == '🧑‍💼 Profile':
        st.markdown("# Total Comments by Profile")
        st.markdown("### ***Each post received an average of {} comments.***".format(avg_comment))
        st.plotly_chart(fig_likes, use_container_width=True)


## Hashtags

elif option == '#️⃣ Hashtags':
    selected_option = st.selectbox('Filter by:',
                                   ['Most Used', 'Most Liked'],
                                   key='hashtags_selectbox')
    if selected_option == 'Most Used':
        st.markdown("# Most Used Hashtags:")
        st.markdown(" ### ***Each post used, in average, {} hashtags***".format(avg_hashtag))
        selected_hashtags = st.multiselect("Search by #️⃣hashtag:", df_top_200['Hashtag'])
        if selected_hashtags:
            st.write("Selected hashtags:")
            for hashtag in selected_hashtags:
                row = df_top_200[df_top_200['Hashtag'] == hashtag].iloc[0]
                st.markdown(f"- **#️⃣ Hashtag:** {row['Hashtag']}   |   **🔄 Times Used:** {row['Times Used']}")
        st.markdown("# All hashtags:")
        st.table(df_top_200[['Hashtag', 'Times Used']])


    
    elif selected_option == 'Most Liked':
        st.markdown("# Hashtags and Number of likes:")
        all_hashtags = dfh['hashtag'].tolist()
        selected_hashtags = st.multiselect("Pesquise by #️⃣hashtag:", all_hashtags)
        if selected_hashtags:
            selected_df = dfh[dfh['hashtag'].isin(selected_hashtags)]
            st.write("Selected hashtags:")
            for index, row in selected_df.iterrows():
                st.markdown(f"- **#️⃣ Hashtag:** {row['hashtag']}   |   **❤️ Likes:** {row['likes']}")
        st.markdown("# All hashtags:")
        st.table(dfh[['hashtag', 'likes']])
            
            
            
st.sidebar.markdown("Created by: Gabriel Angelo de Siqueira")

st.sidebar.markdown("[My Linkedin](https://www.linkedin.com/in/gabriel-angelo-de-siqueira/)")

st.sidebar.markdown("[My Github](https://github.com/Aqualungie)")





















































