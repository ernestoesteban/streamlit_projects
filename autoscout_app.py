import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image


# here we define some of the front end elements of the web page like the font and background color,
# the padding and the text to be displayed

html_temp = """
	<div style ="background-color:#3d2fd6; padding:13px">
	<h1 style ="color:#f0f0f5; text-align:center; ">Streamlit Auto Scout predicter </h1>
	</div>
	"""
# this line allows us to display the front end aspects we have defined in the above code
st.markdown(html_temp, unsafe_allow_html = True)

# Logo of Autoscout
image = Image.open("autoscout.png")
st.image(image, use_column_width=True)


# Display Autoscout Dataset
st.header("_Autoscout Dataset_")
df = pd.read_csv('prediction_data.csv')
st.write(df.head())

# Loading the models to make predictions
model = pickle.load(open("final_linear_pipe_model", "rb"))


# User input variables that will be used on predictions
st.sidebar.title("_Please Enter the Features to Predict the Price of your car")
km = st.sidebar.number_input("km", float(round(df.km.mean(), 1)))
prev_owner = st.sidebar.number_input("prev_owner", df.prev_owner.mode()[0])
hp = st.sidebar.number_input("hp", float(round(df.hp.mean(), 1)))
Displacement = st.sidebar.number_input("Displacement", float(round(df.Displacement.mean(), 1)))
Consumption_comb = st.sidebar.number_input("Consumption_comb", float(round(df.Consumption_comb.mean(), 1)))

# Converting user inputs to dataframe 
my_dict = {
    "km": kmh,
    "prev_owner": prev_owner,
    "hp": hp,
    'Displacement':Displacement,
    "Consumption_comb": Consumption_comb
}
df_input = pd.DataFrame.from_dict([my_dict])


# defining the function which will make the prediction using the data
def prediction(input_data):

	prediction = model.predict(input_data)
	return prediction
	
	
# Making prediction and displaying results
if st.button("Predict"):
    result = prediction(df_input)[0]

try:
    st.success(f"The price of your car is **{result}**")
except NameError:
    st.write("Please **Predict** button to display the result!")




    


