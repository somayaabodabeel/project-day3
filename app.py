"""
@author: somayaabodabeel
"""
import streamlit as st
import joblib
import numpy as np
import os

if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system(f"dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")
def main():
    html_temp = """
    <style>
div {
  background-image: url('Forcasting the future cost.jpg');
}
</style>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('model_joblib_gr')
    
    p1 = st.slider('Enter Your Age',18,100)
    
    s1 = st.selectbox('Sex',('Male','Female'))
    
    if s1=='Male':
        p2=1
    else:
        p2=0
        
    p3 = st.number_input("Enter Your BMI Value")
    
    
    
    p4 = st.slider("Enter Number of Children",0,15)
    
    
    s2 = st.selectbox("Smoker",("Yes","No"))
    
    
    if s2=='Yes':
        p5=1
    else:
        p5=0
        
        
    p6 = st.slider("Enter Your Region",("southwest", "southeast", "northwest", "northeast")
    
    if st.button('Predict'):
        pred= model.predict([[p1,p2,p3,p4,p5,p6]])
        
        st.balloons()
        st.success('Your Insurance Cost is {}'.format(round(pred[0],2)))
        
    
    
        
    
    
    
if __name__ == '__main__':
    main()
