import streamlit as st
from tools import load_and_use_tflite

st.title('1元1次方程式')
st.title('Y = 2X - 1')

prompt = st.chat_input("請輸入X的值:")
if prompt:
    input_value = float(prompt)
    tflite_model_path = 'linear_model.tflite'
    tflite_predict_func = load_and_use_tflite(tflite_model_path)
    test_input = [input_value]
    predict_value = tflite_predict_func(test_input)
    round_value = round(float(predict_value[0, 0]))
    st.write(f"X={input_value},Y={round_value}")