import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("C:\\Users\\gabri\\Desktop\\Workspace\\Projetos\\Book Data\\igposts_dataset_treated.csv")

# Criando coluna com contagem de hashtags

df['hashtag_count'] = df['hashtags'].apply(lambda x: len(x.split()))


#Postagens por editora

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

post_por_editora = df['username'].value_counts().reset_index()
post_por_editora = post_por_editora.sort_values(by='count', ascending=False)

fig_post = px.bar(post_por_editora, x='count', y='username', color='username', color_discrete_map=color_discrete_map, labels={'count': 'Total de Postagens', 'username': 'Editora'})
fig_post.update_xaxes(title_text="Número de Postagens")
fig_post.update_yaxes(title_text="Editora")

# Número de likes por editora

total_de_likes = df.groupby('username')['likes'].sum().reset_index().sort_values(by='likes', ascending=False)
total_de_likes = total_de_likes.sort_values(by='likes',ascending=False)

fig_likes = px.bar(total_de_likes, x='likes', y='username', color='username', color_discrete_map=color_discrete_map, labels={'usernane': 'Editora', 'likes': 'Total de Likes'})

fig_likes.update_xaxes(title_text='Total de Likes')
fig_likes.update_yaxes(title_text='Editora')


# Total de comentários por editora

total_comment = df.groupby('username')['comments'].sum().reset_index().sort_values(by='comments', ascending=False)
total_comment = total_comment.sort_values(by='comments',ascending=False)

fig_comment = px.bar(total_comment, x='comments', y='username', color='username', color_discrete_map=color_discrete_map)

fig_comment.update_xaxes(title_text='Editora')
fig_comment.update_yaxes(title_text='Total de Comentários')

# gráfico de linha com datas

date_line = df['date'].value_counts().reset_index()
date_line.columns = ['date', 'Quantidade de Posts']
date_line = date_line.sort_values(by='date')


fig_date = px.line(date_line, x='date', y='Quantidade de Posts', color_discrete_sequence=['lightcyan'], labels={'date': 'Data'})

fig_date.update_xaxes(title_text='Data')
fig_date.update_yaxes(title_text='Total de Posts')

# Horários com mais postagens

df['hour'] = df['hour'].apply(lambda x: f'{x} horas')

hours = df['hour'].value_counts().reset_index()
hours.columns = ['hour', 'Quantidade de Posts']
hours = hours.sort_values(by='Quantidade de Posts', ascending=True)

fig_hour = px.bar(hours, x='Quantidade de Posts', y='hour', color='Quantidade de Posts', color_discrete_sequence= px.colors.sequential.Blues, labels={'hour': 'Hora do Dia', 'count': 'Total de Posts'})

# Dias da semana

week = df['day_of_week'].value_counts().reset_index()
week.columns = ['Dia da Semana', 'Quantidade de Posts']
week = week.sort_values(by='Quantidade de Posts', ascending=True)

fig_week = px.bar(week, x='Dia da Semana', y='Quantidade de Posts', color='Dia da Semana', color_discrete_sequence=px.colors.qualitative.Prism)

# Média de likes por dia da semana

like_week = df.groupby('day_of_week')['likes'].mean().round().sort_values(ascending=True)

fig_like_week = px.bar(like_week, x='likes', color='likes', color_discrete_sequence=px.colors.qualitative.Prism, labels={'likes': 'Média de Likes', 'day_of_week': 'Dia da Semana'})

fig_like_week.update_xaxes(title_text='Dia da Semana')
fig_like_week.update_yaxes(title_text='Média de Likes')

# Média de likes por hora da postagem

like_hour = df.groupby('hour')['likes'].mean().sort_values(ascending=True).round()

fig_like_hour = px.bar(like_hour, x='likes', color='likes', color_discrete_sequence=px.colors.qualitative.Prism, labels={'likes': 'Média de Likes', 'hour': 'Hora da Postagem'})

fig_like_hour.update_xaxes(title_text= 'Média de Likes')
fig_like_hour.update_yaxes(title_text= 'Horário da Postagem')

# Média de likes por postagem

med_likes = df['likes'].mean().round()

# Média de comentários por postagem

med_comment = df['comments'].mean().round()

# Média de hashtags 

med_hash = df['hashtag_count'].mean().round()

# Hashtags mais usadas

import collections
import re

dft = pd.read_csv("C:\\Users\\gabri\\Desktop\\Workspace\\Projetos\\Book Data\\df_text_tratado.csv")

hashtags = ' '.join(df['hashtags']).split()
counter_hashtags = collections.Counter(hashtags)
top_200_hashtags = counter_hashtags.most_common(200)

df_top_200 = pd.DataFrame(top_200_hashtags, columns=['Hashtag', 'Vezes que foi usada'])

def remove_special_characters(text):
    return re.sub(r'[^\w\sáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕàÀçÇ]', '', text)

df_top_200['Hashtag'] = df_top_200['Hashtag'].apply(remove_special_characters)

# Hashtags com mais likes

dfh = pd.read_csv("C:\\Users\\gabri\\Desktop\\Workspace\\Projetos\\Book Data\\hashtags_likes.csv")


# Sidebar

st.sidebar.header("Análise das Postagens no Instagram de 15 Editoras de Livros Nacionais 📖")



# Select Box


option = st.sidebar.selectbox('Selecione o que visualizar:',
                              ['Postagens 📸', 'Likes ❤️', 'Comentários 💬', 'Hashtags #️⃣'])

# Postagens

if option == 'Postagens 📸':
    selected_option = st.selectbox('Postagem por:',
                                   ['Editora 📖', 'Data 📈', 'Dia da Semana 📅', 'Hora 🕒'],
                                   key='postagens_selectbox')
    if selected_option == 'Editora 📖':
        st.markdown("# Total de Postagens por Editora")
        st.plotly_chart(fig_post, use_container_width=True)

    elif selected_option == 'Data 📈':
        st.markdown("# Postagens por Data")
        st.plotly_chart(fig_date, use_container_width=True)

    elif selected_option == 'Dia da Semana 📅':
        st.markdown("# Postagens por Dia da Semana")
        st.plotly_chart(fig_week, use_container_width=True)

    elif selected_option == 'Hora 🕒':
        st.markdown("# Postagens por Hora")
        st.plotly_chart(fig_hour, use_container_width=True)

#Likes

elif option == 'Likes ❤️':
    selected_option = st.selectbox('Likes por:',
                                   ['Editora 📖', 'Dia da Semana 📅', 'Hora 🕒'],
                                   key='likes_selectbox')
    if selected_option == 'Editora 📖':
        st.markdown("# Total de Likes por Editora")
        st.markdown("#### ***Cada postagem recebeu, em média, 2384 likes.***")
        st.plotly_chart(fig_likes, use_container_width=True)
        
    elif selected_option == 'Dia da Semana 📅':
        st.markdown("# Média de likes por Dia da Semana")
        st.plotly_chart(fig_like_week, use_container_width=True)

    elif selected_option == 'Hora 🕒':
        st.markdown("# Média de Likes por Hora da Postagem")
        st.plotly_chart(fig_like_hour, use_container_width=True)


# Comentários

elif option == 'Comentários 💬':
    selected_option = st.selectbox('Comentários por:',
                                   ['Editora 📖'],
                                   key='comentarios_selectbox')
    if selected_option == 'Editora 📖':
        st.markdown("# Total de Comentários por Editora")
        st.markdown("### ***Cada postagem recebeu, em média, 113 comentários.***")
        st.plotly_chart(fig_likes, use_container_width=True)


# Hashtags

elif option == 'Hashtags #️⃣':
    selected_option = st.selectbox('Hashtags que:',
                                   ['Foram mais usadas', 'Tiveram mais likes'],
                                   key='hashtags_selectbox')
    if selected_option == 'Foram mais usadas':
        st.markdown("# Hashtags Mais Usadas:")
        st.markdown(" ### ***Cada postagem usou uma média de 7 hashtags***")
        selected_hashtags = st.multiselect("Pesquise por #️⃣hashtag:", df_top_200['Hashtag'])
        if selected_hashtags:
            st.write("Hashtags selecionadas:")
            for hashtag in selected_hashtags:
                row = df_top_200[df_top_200['Hashtag'] == hashtag].iloc[0]
                st.markdown(f"- **#️⃣ Hashtag:** {row['Hashtag']}   |   **🔄 Vezes que foi Usada:** {row['Vezes que foi usada']}")
        st.markdown("# Tabela:")
        st.table(df_top_200[['Hashtag', 'Vezes que foi usada']])


    
    elif selected_option == 'Tiveram mais likes':
        st.markdown("# Hashtags e Quantidade de likes:")
        all_hashtags = dfh['hashtag'].tolist()
        selected_hashtags = st.multiselect("Pesquise por #️⃣hashtag:", all_hashtags)
        if selected_hashtags:
            selected_df = dfh[dfh['hashtag'].isin(selected_hashtags)]
            st.write("Hashtags selecionadas:")
            for index, row in selected_df.iterrows():
                st.markdown(f"- **#️⃣ Hashtag:** {row['hashtag']}   |   **❤️ Likes:** {row['likes']}")
        st.markdown("# Tabela:")
        st.table(dfh[['hashtag', 'likes']])
            
            
            
st.sidebar.markdown("Autor: Gabriel Angelo de Siqueira")

st.sidebar.markdown("[Meu Linkedin](https://www.linkedin.com/in/gabriel-angelo-de-siqueira/)")

st.sidebar.markdown("[Meu Github](https://github.com/Aqualungie)")





















































