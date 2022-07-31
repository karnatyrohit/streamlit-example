from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

# give a title to our app
st.title('Welcome to BMI Calculator')
 
# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")
 
# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))
 
# compare status value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
     
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
         
elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')
     
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
         
else:
    # take height input in feet
    height = st.number_input('Feet')
     
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
 
# check if the button is pressed or not
if(st.button('Calculate BMI')):
     
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
     
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")       
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")
