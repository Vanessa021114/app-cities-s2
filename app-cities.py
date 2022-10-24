import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('World Cities by Vanessa')

df = pd.read_csv('worldcities.csv')

pop_filter = st.sidebar.slider('select minimal population',0.0,40.0,4.0)



# create a multi select
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options
     df.capital.unique())  # defaults

df = df[df.population >= pop_filter]

# filter by capital
df = df[df.capital.isin(['primary','admin'])]

df[df.capital=='primary']


# show dataframe
st.subheader('City Details:')
st.write(df[['city', 'country', 'population']])

# show the plot
st.subheader('Total Population By Country')
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)


form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL') 
form.form_submit_button("Apply")

# filter by population
df = df[df.population >= pop_filter]

# filter by capital
df = df[df.capital.isin(capital_filter)]

if country_filter!='ALL':
    df = df[df.country == country_filter]

# show on map
st.map(df)
st.write(df)
fig, ax = plt.subplots()
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)
