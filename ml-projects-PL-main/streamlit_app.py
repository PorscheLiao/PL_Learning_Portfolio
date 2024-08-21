# https://docs.streamlit.io/library/cheatsheet
# streamlit run app.py
import streamlit as st
import numpy as np 
import joblib
import base64

def get_image_html(page_name, file_name):
    with open(file_name, "rb") as f:
        contents = f.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    return f'<a href="{page_name}"><img src="data:image/png;base64,{data_url}" style="width:300px"></a>'


data_url_1 = get_image_html("聯立方程式解", "ml-projects-PL-main/equations.png")
data_url_2 = get_image_html("分類", "ml-projects-PL-main/penguin.png")
data_url_3 = get_image_html("迴歸", "ml-projects-PL-main/taxi.png")
data_url_4 = get_image_html("辨識", "ml-projects-PL-main/letter.png")
data_url_5 = get_image_html("BreastCancer_prediction", "ml-projects-PL-main/BreastCancer.png")

# data_url_1 = get_image_html("聯立方程式解", "./equations.png")
# data_url_2 = get_image_html("分類", "./penguin.png")
# data_url_3 = get_image_html("迴歸", "./taxi.png")
# data_url_4 = get_image_html("辨識", "./letter.png")
# data_url_5 = get_image_html("BreastCancer_prediction", "./BreastCancer.png")

st.set_page_config(
    page_title="我的學習歷程",
    page_icon="👋",
)

st.title('Machine Learning 學習歷程')   

col1, col2 = st.columns(2)
with col1:
    # url must be external url instead of local file
    # st.markdown(f"### [![分類]({url})](分類)")
    st.markdown('### [(分類)企鵝品種辨識](分類)')
    st.markdown('''
    ##### 特徵(X):
        - 島嶼
        - 嘴巴長度
        - 嘴巴寬度
        - 翅膀長度
        - 體重
        - 性別
    ##### 預測類別(Class):
        - Adelie
        - Chinstrap
        - Gentoo
        ''')
    # st.image('penguin.png')
    st.markdown(data_url_2, unsafe_allow_html=True)


    st.markdown('### [(BreastCancer_prediction)BreastCancer_prediction](BreastCancer_prediction)')
    st.markdown('''
    ##### 特徵(X):
        - mean radius
        - mean texture
        - mean perimeter             
        - mean area                  
        - mean smoothness            
        - mean compactness           
        - mean concavity             
        - mean concave points        
        - mean symmetry              
        - mean fractal dimension     
        - radius error               
        - texture error              
        - perimeter error            
        - area error                 
        - smoothness error           
        - compactness error          
        - concavity error            
        - concave points error       
        - symmetry error             
        - fractal dimension error    
        - worst radius               
        - worst texture              
        - worst perimeter            
        - worst area                 
        - worst smoothness           
        - worst compactness          
        - worst concavity            
        - worst concave points       
        - worst symmetry             
        - worst fractal dimension    
    ##### 預測類別(Class):
        - malignant
        - benign
        ''')
    # st.image('BreastCancer.png')
    st.markdown(data_url_5, unsafe_allow_html=True)
    
    st.markdown('### [(聯立方程式解)聯立方程式解](聯立方程式解)')
    st.markdown('''
    ##### 方程式1
          方程式2
    ##### 求解
        x=?
        y=?
        ''')
    # st.image('equations.png')
    st.markdown(data_url_1, unsafe_allow_html=True)
with col2:
    st.markdown('### [(迴歸)計程車小費預測](迴歸)')
    st.markdown('''
    ##### 特徵(X):
        - 車費
        - 性別
        - 吸菸
        - 星期
        - 時間
        - 同行人數
    ##### 目標：預測小費金額
        ''')
    # st.image('taxi.png')
    st.markdown(data_url_3, unsafe_allow_html=True)


    # url must be external url instead of local file
    # st.markdown(f"### [![辨識]({url})](辨識)")
    st.markdown('### [(辨識)辨識手寫字母](辨識)')
    st.markdown('''
    ##### 辨識手寫字母
        ''')
    # st.image('letter.png')
    st.markdown(data_url_4, unsafe_allow_html=True)
 