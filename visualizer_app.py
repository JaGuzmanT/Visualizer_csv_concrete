import streamlit as st
import pandas as pd
import altair as alt

# App interface
st.set_page_config(layout="wide")
st.title("Visualizer of graphics for a custom dataset")
st.write("""This app allows you to visualize graphics of a given dataset""")
st.write("""---""")

# Charging the dataset
df = pd.read_csv("datos.csv")
st.write(df)
st.write("""---""")

st.subheader("Graphic Visualization")
selected_x_variable = st.selectbox(label="What variable do you want to visualize in the x-axis",
             options=["Age", "Cs", "UPV", "Er"])
selected_y_variable = st.selectbox(label="What variable do you want to visualize in the y-axis",
             options=["Age", "Cs", "UPV", "Er"])

# Building the chart interface
alt_chart = (alt.Chart(df)
                .mark_circle()
                .encode(
                    x=selected_x_variable,
                    y=selected_y_variable
                )
                .interactive()
                )
st.altair_chart(alt_chart, use_container_width=True)