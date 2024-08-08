import streamlit as st
#title 
st.title("this is your title at the bottom")

#header
st.header("this is your header")

#subheader
st.subheader("this is your sub header")
#markdown
#
st.markdown("this is your markdown\n:**text to be bold**")
st.markdown("# header1")
st.markdown("## header2")
st.markdown("### header3")
#caption
#triple string show that this is multine string and also used for multi line comment
st.caption("this is used for caption")
st.code("""
import numpy as np
import pandas as pd
import sklearn.preprocessing import SimpleImputer
import sklearn.ensemble import RandomForestRegressor
import sklearn.preprocessing import StandardScaler
import sklearn.model_selection import train_test_split
import sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
""")


#this is common text without any specific formated
st.text("this is common text")


#latex this is used for any equation
st.latex("""
    x = x^2 + x ^4
""")


#divider is mark line between up and down
st.text("this is above text from line")
st.divider()
st.text("this is lower text from line")
#write function take lot of arguments like dataframe/images/bunch of things
st.write("this is your write function")

