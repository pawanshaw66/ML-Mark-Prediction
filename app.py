import  streamlit as st
import joblib

def main():
    html_temp = """
    <div style = "background-color:lightblue;padding:16px">
    <h2 style = "color:black";text-align:center> Student Mark  Prediction Using ML</h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('students_mark_predictor_model')
    
    p1 = st.number_input("Enter study hour")
    
    if st.button('Predict'):
       pred =   model.predict([[p1]]) 
       st.success("Mark is  {}".format(pred[0]))
        
    
    
    
    
    
    
    
    
if __name__== '__main__':
    main()      