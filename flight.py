import streamlit as st
import pandas as pd
import datetime as dt
from PIL import Image





def run_app():

    st.image(Image.open('aeroplane.JPG'),use_column_width=True)
    st.sidebar.image(Image.open('indigo.jpg'), use_column_width=True)

    st.title("Indian Domestic Flight Price Predictor")

    ##Departure Date
    journey_date = st.sidebar.date_input('Departure date', min_value=dt.date(2019, 1, 1), max_value=dt.date(2035, 3, 1))
    Journey_day = int(pd.to_datetime(journey_date, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(journey_date, format="%Y-%m-%dT%H:%M").month)

    #Departure Time
    dep_time=st.sidebar.time_input("Departure time")
    dep_hr=int(dep_time.hour)
    dep_min=int(dep_time.minute)


    #Arrival Date
    #arrival_date = st.sidebar.date_input('Arrival date', min_value=dt.date(2019, 1, 1), max_value=dt.date(2035, 3, 1))
    #arrival_day = int(pd.to_datetime(arrival_date, format="%Y-%m-%dT%H:%M").day)
    #arrival_month = int(pd.to_datetime(journey_date, format="%Y-%m-%dT%H:%M").month)

    #Arrival Time
    arrival_time=st.sidebar.time_input("Arrival time")
    arrival_hr=int(arrival_time.hour)
    arrival_min=int(arrival_time.minute)


    ##Duration (Arrival -Departure)

    duration_hr=abs(arrival_hr-dep_hr)
    duration_min=abs(arrival_min-dep_min)

    st.sidebar.info("This Application is developed by Siddhesh D. Munagekar to predict flight fare")

    #Source
    source=st.selectbox("Source",("Delhi","Kolkata","Mumbai","Chennai"))
    if (source == 'Delhi'):
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    elif (source == 'Kolkata'):
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0
        s_Chennai = 0

    elif (source == 'Mumbai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1
        s_Chennai = 0

    elif (source == 'Chennai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 1

    else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0



    #Destination

    destination = st.selectbox("Destination", ("Cochin","Delhi", "Hyderabad", "Kolkata", "New_Delhi"))

    if (destination == 'Cochin'):
        d_Cochin = 1
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (destination == 'Delhi'):
        d_Cochin = 0
        d_Delhi = 1
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (destination == 'New_Delhi'):

        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (destination == 'Hyderabad'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0

    elif (destination == 'Kolkata'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1

    else:
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0


    stops=st.selectbox("Total Stops",("Non-Stop",1,2,3,4))

    if stops=="Non-Stop":
        total_stop=0
    else:
        total_stop=int(stops)


    ####Select Airline##

    airline=st.selectbox("Which Air line would you like to travel ?",("Jet Airways","IndiGo","Air India","Multiple carriers","SpiceJet","Vistara",
                                                                      "GoAir","Multiple carriers Premium economy","Jet Airways Business",
                                                                      "Vistara Premium economy","Trujet"))

    if (airline == 'Jet Airways'):
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'IndiGo'):
        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Air India'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Multiple carriers'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'SpiceJet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Vistara'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 1
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'GoAir'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 1
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Multiple carriers Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Jet Airways Business'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 1
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Vistara Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 1
        Trujet = 0

    elif (airline == 'Trujet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 1

    else:
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0


    #Upload  model
    #random_forest = open('flight_rf_model.pkl', 'rb')
    #model=pickle.load(random_forest)
    url = "https://drive.google.com/file/d/1WH6VASQXlXOkMQgOCbDeIE-POIfBT3YG/view?usp=sharing"
    path = 'https://drive.google.com/uc?export=download&id=' + url.split('/')[-2]
    model = pd.read_pickle(path)


    prediction = model.predict([[
        total_stop,
        Journey_day,
        Journey_month,
        dep_hr,
        dep_min,
        arrival_hr,
        arrival_min,
        duration_hr,
        duration_min,
        Air_India,
        GoAir,
        IndiGo,
        Jet_Airways,
        Jet_Airways_Business,
        Multiple_carriers,
        Multiple_carriers_Premium_economy,
        SpiceJet,
        Trujet,
        Vistara,
        Vistara_Premium_economy,
        s_Chennai,
        s_Delhi,
        s_Kolkata,
        s_Mumbai,
        d_Cochin,
        d_Delhi,
        d_Hyderabad,
        d_Kolkata,
        d_New_Delhi
    ]])

    output=round(prediction[0],2)

    if st.button("Check flight price !"):

        st.write("Your flight fare is :Rs.",output)


    return 0





if __name__=='__main__':


    run_app()
