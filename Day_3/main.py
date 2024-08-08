# today we learn graph in streamlit
import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('Salary_predict.csv')

tab1,tab2,tab3 = st.tabs(['line chart','area chart','bar chart'])


#------------------------------------------------------------------------------------------------------
#below is line_chart() constructor from documentation
# st.line_chart()st.line_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, width=None, height=None, use_container_width=True)
with tab1:
    st.line_chart(df,x='age',y='Salary',x_label='Age',y_label='Experience or Salary')
    st.line_chart(df,x='age',y='experience',x_label='age',y_label='experience')

#----------------------------------------------------------------------------------------------------------
# below is area_chart() constructor from streamlit documentation
#st.area_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, stack=None, width=None, height=None, use_container_width=True)
with tab2:
    st.area_chart(df,x='age',y=["experience"],x_label='Age',y_label='Experience',color='interview_score',stack='center')

#-------------------------------------------------------------------------------------------------------
#below is bar_chart() constructor from docementation
# st.bar_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, horizontal=False, stack=None, width=None, height=None, use_container_width=True)
with tab3:
    st.bar_chart(df,x='age',y=['interview_score'],x_label='Age',y_label='Interview score') 






