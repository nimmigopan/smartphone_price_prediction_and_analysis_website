import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="viz Demo")

st.title('Price Prediction')

with open('df.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)

#st.dataframe(df)

st.header('Enter the specifications for phone')

#brand_name
brand_name = st.selectbox('Phone Brand',sorted(df['brand_name'].unique().tolist()))
#has_dual_sim
dual_sim = int(st.selectbox('Need Dual Sim?',[True,False]))
#has_5G
fiveG = int(st.selectbox('5G',[True,False]))
#has_NFC
nfc = int(st.selectbox('NFC',[True,False]))
#has_IR_Blaster
IRblaster = int(st.selectbox('IR Blaster',[True,False]))
#processor_brand
processor_brand = st.selectbox('Processor Brand',sorted(df['processor_brand'].unique().tolist()))
#no_of_cores
no_of_cores = int(st.selectbox('No of Cores',sorted(df['no_of_cores'].unique().tolist())))
#processor_speed
processor_speed = float(st.selectbox('Speed of Processor(Hz)',sorted(df['processor_speed'].unique().tolist(),reverse=True)))
#ram
ram = int(st.selectbox('RAM in GB',sorted(df['ram'].unique().tolist(),reverse=True)))
#rom
rom = int(st.selectbox('ROM in GB',sorted(df['rom'].unique().tolist(),reverse=True)))
#fast_charging_available
fast_charging_available = int(st.selectbox('Fast Charging',[True,False]))
#battery_capacity
battery_capacity = int(st.selectbox('Battery Capacity(mAh)',sorted(df['battery_capacity'].unique().tolist(),reverse=True)))
#screen_size
screen_size = float(st.selectbox('Screen Size in inches',sorted(df['screen_size'].unique().tolist(),reverse=True)))
#resolution
resolution = st.selectbox('Screen Resolution',df['resolution'].unique().tolist())
#refresh_rate
refresh_rate = int(st.selectbox('Refresh Rate(Hz)',sorted(df['refresh_rate'].unique().tolist())))
#no_of_rear_cameras
no_of_rear_cameras = int(st.selectbox('No. of rear cameras',sorted(df['no_of_rear_cameras'].unique().tolist(), reverse=True)))
#no_of_front_cameras
no_of_front_cameras = int(st.selectbox('No. of front cameras',sorted(df['no_of_front_cameras'].unique().tolist(), reverse=True)))
#primary_front_camera
primary_front_camera = int(st.selectbox('Primary Front Camera Pixel',sorted(df['primary_front_camera'].unique().tolist(), reverse=True)))
#primary_rear_camera
primary_rear_camera = int(st.selectbox('Primary Rear Camera Pixel',sorted(df['primary_rear_camera'].unique().tolist(), reverse=True)))
#memory_extended_upto
memory_extended_upto = int(st.selectbox('Extended Memory in GB',sorted(df['memory_extended_upto'].unique().tolist(), reverse=True)))
#operating_system
operating_system = st.selectbox('Operating System', ['Android', 'iOS'])

if st.button('predict'):

    #form a df
    data = [[brand_name, dual_sim, fiveG, nfc, IRblaster, processor_brand, no_of_cores, processor_speed, ram, rom, fast_charging_available,
             battery_capacity, screen_size, resolution, refresh_rate, no_of_rear_cameras, no_of_front_cameras, primary_front_camera,
             primary_rear_camera, memory_extended_upto, operating_system]]
    columns = ['brand_name', 'has_dual_sim', 'has_5G', 'has_NFC', 'has_IR_Blaster','processor_brand', 'no_of_cores', 'processor_speed',
               'ram', 'rom', 'fast_charging_available','battery_capacity', 'screen_size', 'resolution', 'refresh_rate', 'no_of_rear_cameras',
               'no_of_front_cameras', 'primary_front_camera','primary_rear_camera', 'memory_extended_upto','operating_system']

    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)

    #predict
    base_price = st.text(np.expm1(pipeline.predict(one_df)))
    #low = base_price - 2803.261137
    #high = base_price + 2803.261137

    #display
    #st.text("The price of phone is between {} and {}".format((low,high)))