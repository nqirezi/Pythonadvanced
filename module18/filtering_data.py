import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon Top selling books from 2009 to 2022")

# Sidebar form to add new book
st.sidebar.header("Add New Book Data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("User Rating", 0.0, 5.0, 0.0, 0.1)
    new_review = st.number_input("Review", min_value=0, step=1)
    new_price = st.number_input("Price", min_value=0.0, step=0.1)
    new_year = st.number_input("Year", min_value=2009, max_value=2022, step=1)
    new_genre = st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add book")

if submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'User Rating': new_user_rating,
        'Review': new_review,
        'Price': new_price,
        'Year': new_year,
        'Genre': new_genre
    }
    books_df = pd.concat([pd.DataFrame([new_data]), books_df], ignore_index=True)
    books_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index=False)
    st.sidebar.success("New book added successfully")

#Sidebar filters
st.sidebar.header("Filter Options")
selected_author = st.sidebar.selectbox("Select Author",["all"] + list(books_sf['Author'].unique()))
selected_year = st.sidebar.selectbox("Select Year",["all"] + list(books_sf['Year'].unique()))
selected_genre = st.sidebar.selectbox("Select Genre",["all"] + list(books_sf['Genre'].unique()))
mix_rating = st.sidebar.slider("Minimum User Rating",0.0,5.0,0.0,0.1)
mix_price = st.sidebar.slider("Minimum Price",0,books_df['Price'].max(),books_df[Price].max())

#Filter the dataset
filtered_books_df = books_df.copy()
if selected_author != "All":
    filtered_books_df = filtered_books_df[filtered_books_df['Author'] == selected_author]
if selected_author != "All":
    filtered_books_df = filtered_books_df[filtered_books_df['Author'] == selected_author]
if selected_author != "All":
    filtered_books_df = filtered_books_df[filtered_books_df['Author'] == selected_author]

filtered_books_df = filtered_books_df[
    (filtered_books_df['User rating'] >= mix_rating) & (filtered_books_df['Price'] <= mix_price)]








# Summary Statistics
st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"${average_price:.2f}")

# Dataset preview
st.subheader("Dataset Preview")
st.write(books_df.head())

# Top 10 Titles and Authors
col1, col2 = st.columns(2)
with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df["Author"].value_counts().head(10)
    st.bar_chart(top_authors)

# Genre Distribution Pie Chart
st.subheader("Genre Distribution")
fig = px.pie(books_df, names="Genre", title="Most Liked Genre (2009-2022)",
             color='Genre', color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

# Fiction vs Non-Fiction over Years
st.subheader("Number of Fiction vs Non-Fiction Books over Years")
size = books_df.groupby(['Year', "Genre"]).size().reset_index(name='Counts')
fig = px.bar(size, x="Year", y="Counts", color='Genre',
             title="Number of Fiction vs Non-Fiction Books 2009-2022")
st.plotly_chart(fig)

# Top 15 Authors by Book Count
st.subheader("Top 15 Authors by Counts of Books Published (2009-2022)")
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author', 'Count']

fig = px.bar(top_authors, x='Count', y='Author', orientation='h',
             title='Top 15 Authors by Counts of Books Published (2009-2022)',
             labels={'Count': 'Count of Books Published', 'Author': 'Author'},
             color='Count', color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig)

# Filter by Genre
st.subheader("Filter Data by Genre")
genre_filter = st.selectbox("Select Genre", books_df['Genre'].unique())
filtered_df = books_df[books_df['Genre'] == genre_filter]
st.write(filtered_df)
