import streamlit as st
import numpy as np
import pandas as pd


st.title('Today we learn about widget')
st.caption("how to take input from user in multiple ways")


#1
st.header("Button")
#below is constructor from offical website
# st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False) 
primary_button = st.button(label="My_Button",type='primary',key=1,help="press in a good style",use_container_width=True)
if primary_button:
    st.write("I am primary button an aho")
st.write(primary_button)
secondary_button = st.button(label='My Secondary button',type='secondary',key=2)
if secondary_button:
    st.write("I am secondary button an aho")
st.write(secondary_button)

#2
st.header("Checkbox")
# below is constructor from offical documentation
# st.checkbox(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
def after_on_change():
    st.write("you say i agree with you")

checkbox = st.checkbox("i agree with",value=False,key=3,help="please press me")
st.write(checkbox)
#3
st.header("Radio")
#st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False, captions=None, label_visibility="visible")
radio_button = st.radio("this is my radio button",options=['one','two','three','four','five','six'],key=4,help='this is my radio button')
st.write(radio_button)



#4
st.header("multi select")
#st.multiselect(label, options, default=None, format_func=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
multi_select = st.multiselect("this is my multi select",options=['one','two','three','four','five','six'],key=5,help='this is my multi select button')
st.write(multi_select)



#5
st.header("slider")
#st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
my_silder = st.slider("this is ny slider",min_value=0,max_value=100,step=10,key=6,help="this is my slider",value=50)
st.write(my_silder)

#6
st.header("Number Input")
#st.number_input(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
my_number = st.number_input("this is my number input",min_value=0,max_value=100,step=10,key=7,help="this is my number input",value=50)
st.write(my_number)



#7
st.header("text input")
#st.text_input(label, value=None, key=None, help=None, type="default", on_change=None, args=None, kwargs=None, *, max_chars=None, label_visibility="visible", autocomplete=None)
my_text = st.text_input("this is my text input",key=8,help="this is my text input",value="ahmed")
st.write(my_text)

#8
st.header("Text input")
#st.text_area(label, value="", height=None, max_chars=None, key=None, help=None
my_text_area = st.text_area("this is my text area",key=9,help="this is my text area",value="ahmed")
st.write(my_text_area)
















