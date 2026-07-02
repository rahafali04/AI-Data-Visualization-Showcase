import streamlit as st
import pandas as pd
import joblib
import folium 
from streamlit_folium import st_folium 

#Page configration & title 
st.set_page_config(page_title="Smart Parking System",layout="wide")
st.title("Smart Parking Recommendation System")
st.markdown("---")

#Asset Loading (Data & Models):
@st.cache_resource
def load_asset():
    #Load DS
    df = pd.read_csv('final_merged_dataset (1).csv')
    #Load the Trained ML model
    model = joblib.load('parking_model.pkl')
    #load the scaler (for data normalization)
    scaler = joblib.load('parking_scaler.pkl')
    return df,model,scaler
try:
    df,model,scaler = load_asset() 
    st.sidebar.success("Data & Model Loaded Successfuly")
except Exception as e:
    st.sidebar.error(f"Loading Error {e}")
    st.stop()
#UI(Input)    
st.sidebar.header("Search Setting")
#Dropdown for selecting area 
selected_area = st.sidebar.selectbox("Select Area / Resturant :",df['area'].unique())
#Slider for choosing the hour 
hour = st.sidebar.slider("Select Hour |",0,23,12)
#Select the day of the week 
day_of_week = st.sidebar.selectbox("Select Day :" , ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
#Convert day name to numieric for the model 
days_map = {"Monday": 0, "Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
day_num = days_map[day_of_week]

#احداثيات تقريبية للمناطق
area_coords = {
    "brookefield": [12.9625, 77.7126],
    "brigade road": [12.9703, 77.6068],
    "kalyan nagar": [13.0221, 77.6403],
    "bellandur": [12.9304, 77.6784],
    "koramangala 5th block": [12.9352, 77.6245],
    "malleshwaram": [13.0031, 77.5709],
    "banashankari": [12.9254, 77.5468]
}

#Prediction & Recommendation Logic 
def get_recommendation(): 
    #Align input features with model's training schema
    input_data = pd.DataFrame(columns=scaler.feature_names_in_)
    #initialize all feature values to zero
    input_data.loc[0] = 0
    #assign user input to respective features 
    input_data['hour']=hour
    input_data['day_of_week']=day_num
    #Handle One-Hot Encoded categorical data for the selected area 
    area_col =f"area_{selected_area}"
    if area_col in input_data.columns:
        input_data[area_col]=1

    #Data scaling & Prediction 
    X_scaled = scaler.transform(input_data)
    pred = model.predict(X_scaled)[0]
    #Map numerical output to status text 
    status_map = {0: "Available", 1:"Busy",2:"Full"}
    current_status = status_map.get(pred,"Full")
    #Display the prediction Result 
    st.subheader(f"Parking Status in:{selected_area}")
    if current_status == "Available":
        st.success(f"Primary Parking is : {current_status}")
    elif current_status == "Busy":
        st.warning(f"Primary Parking is :{current_status}")
    else:
        st.error(f"Primary Parking is :{current_status}")

    #Filter data based on selected area 
    nearby_parkings = df[df['area'] == selected_area].copy()


    #Recommendation Algorithem based on distance / sorting by lowest occupany rate (emptiest spots)
    best_option = nearby_parkings.sort_values('occupancy_rate').iloc[0]
    st.success(f"System Advice: We suggest:{best_option['restaurant_name']} (Occupancy Rate: {best_option['occupancy_rate']:.2%}) ")
    st.progress(best_option['occupancy_rate'])
#Interactive map visulization 
    #a.creat map centered at the recommended location 
    location = area_coords.get(selected_area.lower(),[12.9716 , 77.5946])
    st.subheader("Parking Location Map")
    m=folium.Map(location = location ,zoom_start=15)
    #b.add a marker to the map 
    folium.Marker(location , popup=f"Recommended: {best_option['restaurant_name']}", icon=folium.Icon(color='green' if current_status == "Available" else 'orange')).add_to(m)

    #Render map in streamlit 
    st_folium(m,width=700,height=450 , key =f"map_{selected_area}_{hour}")
#st.info("Note: Map view is disabled as coordinates are not in the current dataset")

get_recommendation()
          



