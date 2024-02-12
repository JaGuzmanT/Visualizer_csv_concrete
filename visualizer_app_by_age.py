import streamlit as st
import pandas as pd
import altair as alt

# App interface
st.set_page_config(layout="wide")
st.title("Concrete Dataset Analizer")
st.write("This application is an interactive app for analyzing a custom dataset")
st.write(
    """---""")

# Charging the dataset
concrete_df = pd.read_csv("datos.csv")
st.write(concrete_df,)
st.write(
    """---""")

# Dynamic selections
st.subheader("Graphic visualization")
selected_age_variable = st.selectbox(label="Select the age that you want to monitor",
                                    options=["14 days","28 days","60 days","90 days"])
selected_x_variable = st.selectbox(label="Select the variable that you want to see in the x-axis",
                                   options=["Cs", "UPV", "Er"], placeholder="Cs")
selected_y_variable = st.selectbox(label="Select the variable that you want to see in the y-axis",
                                   options=["Cs", "UPV", "Er"], placeholder="UPV")

concrete_df = concrete_df[concrete_df["Age"]==selected_age_variable]

# Building the chart interface
st.subheader("")
alt_chart = (alt.Chart(data=concrete_df, title=f"Scatter plot of {selected_x_variable} and {selected_y_variable}")
             .mark_circle()
             .encode(
                 x=selected_x_variable,
                 y=selected_y_variable
             )
             .interactive()
             )

# Showing the chart interface
st.altair_chart(alt_chart,use_container_width=True)






