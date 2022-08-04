import streamlit as st
import pickle
import numpy as np
#import joblib 


def load_model():
    with open('Modified1_AA_LLC.pkl', "rb") as file:
        data = pickle.load(file)
    return data


data = load_model()
model = data["model"]
le = data["le"]


def show_predict_page():
    st.title("Terrorism Attack Prediction")

    st.write("""### We need some information to predict the attack""")

    countries = (
                    "Somalia",                            
                    "Nigeria",                            
                    "South Africa",                        
                    "Sudan",                                
                    "Democratic Republic of the Congo",   
                    "Kenya",                                
                    "Burundi",                              
                    'Mali',                                 
                    "Angola",                               
                    "Uganda",                               
                    "Mozambique",                                                          
                    "Cameroon",                             
                    "Central African Republic",             
                    "South Sudan",                          
                    "Ethiopia",                            
                    "Rwanda",                              
                    "Namibia",                              
                    "Niger",                               
                    "Senegal",                              
                    "Zimbabwe",                             
                    "Sierra Leone",                        
                    "Chad",                                  
                    "Rhodesia",                              
                    "Ivory Coast",                           
                    "Zambia",                                
                    "Tanzania",                             
                    "Burkina Faso",                         
                    "Zaire", 
    )

    state = (
                    'Banaadir',            
                    'Borno',             
                    'Gauteng',             
                    'Lower Shebelle',       
                    'Unknown',              
                    'KwaZulu-Natal',        
                    'North Kivu',           
                    'Lower Juba',          
                    'Bay',                  
                    'North Darfur',         
                    'Bujumbura Mairie',    
                    'Hiiraan',              
                    'Extreme-North',        
                    'Yobe',                 
                    'Gedo',                 
                    'Benue',                
                    'Northern',             
                    'Adamawa',              
                    'South Darfur'         
                    'Western Cape',        
                    'Plateau',              
                    'Rivers',               
                    'Kaduna',               
                    'Delta',                
                    'Kano',                 
                    'Bari',                
                    'Mudug',                
                    'Middle Shebelle',      
                    'Orientale',            
                    'Eastern Cape'         
                    'Kidal',               
                    'Central',              
                    'Gao',                 
                    'Timbuktu',            
                    'Galguduud',            
                    'Bayelsa',              
                    'North Eastern',       
                    'Bakool',              
                    'Mandera',
        
    )
    attackType = (
                    'Hostage Taking (Kidnapping)', 'Hijacking',
       'Assassination', 'Bombing/Explosion', 'Armed Assault',
       'Facility/Infrastructure Attack',
       'Hostage Taking (Barricade Incident)', 'Unarmed Assault'
        
    )
        
    targetType = (
                    'Military', 'Journalists & Media', 'Government (Diplomatic)',
       'Government (General)', 'Airports & Aircraft', 'Business',
       'Private Citizens & Property', 'Transportation',
       'Violent Political Party', 'Educational Institution', 'Police',
       'Utilities', 'Religious Figures/Institutions', 'Tourists',
       'NGO', 'Telecommunication', 'Food or Water Supply',
       'Maritime', 'Terrorists/Non-State Militia',
    )
    
    groupName = (
                    "South-West Africa People's Organization (SWAPO)",
       'African National Congress (South Africa)',
       'National Union for the Total Independence of Angola (UNITA)',
       'Mozambique National Resistance Movement (MNR)',
       'Inkatha Freedom Party (IFP)',
       'Movement of Democratic Forces of Casamance', 'Hutu extremists',
       'Revolutionary United Front (RUF)', "Lord's Resistance Army (LRA)",
       'Allied Democratic Forces (ADF)', 'Mayi Mayi', 'Fulani extremists',
       'Janjaweed',
       'Movement for the Emancipation of the Niger Delta (MEND)',
       'Democratic Front for the Liberation of Rwanda (FDLR)',
       'Muslim extremists', 'Al-Shabaab',
       'Al-Qaida in the Islamic Maghreb (AQIM)', 'Boko Haram',
       "Sudan People's Liberation Movement - North",
       'Movement for Oneness and Jihad in West Africa (MUJAO)',
       'Ansar al-Dine (Mali)', 'Anti-Balaka Militia',
       "Sudan People's Liberation Movement in Opposition (SPLM-IO)",
       'Niger Delta Avengers (NDA)',
       'Jamaat Nusrat al-Islam wal Muslimin (JNIM)', 
    )
        
        
    weapon = ('Explosives', 'Firearms', 'Incendiary', 'Melee',
       
    )
    
        
        
        
    country = st.selectbox("Country", countries)
    state = st.selectbox("State", state)
    attackType = st.selectbox("AttackType", attackType)
    targetType = st.selectbox("TaretType", targetType)
    groupName = st.selectbox("Group", groupName)
    weapon = st.selectbox("Weapon", weapon)
    

    ok = st.button("Predict Attack")
    if ok:
        X = [country ,state, attackType, targetType,groupName, weapon]
        X_n = le.fit_transform(X)
        X_n = np.array(X_n).reshape(1, -1)
        prediction = model.predict(X_n)
        #st.write(X_n)
        if prediction[0] == 1:
            st.subheader('The Attack is Successful')
        else:
            st.subheader('The Attack is not Successful')
        
        #print(prediction)
        
        #if (prediction[0] == 0):
           # print('The attack is not successful')
        #else:
            #print('The attack is successful')'''