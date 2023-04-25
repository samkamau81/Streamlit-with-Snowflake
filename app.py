import streamlit as st

# Set the app title
st.title("Psychological Support App")
st.markdown("*** A simple machine laerning app to predict the the mental state of people and give advice on the way forward ***")

st.markdown("# Questionnaire")
st.markdown("## Answer these few questions to help me understand your situation more")
st.markdown("-------")

que0=st.selectbox("County of Resisdence",options=['Nairobi','Nakuru','Nyeri'])


que1=st.text_input("Can you tell me how you've been feeling lately?")

que2=st.text_input("What's been on your mind lately?")

que3=st.text_input("How have your sleep patterns been?")

que4=st.text_input("How have you been coping with stress lately?")

que5=st.text_input("Can you describe your mood over the past few weeks?")


que6=st.selectbox("Have you been feeling down or depressed most of the day, nearly every day?",options=['Everyday','Sometimes','Never'])

que7=st.selectbox("Have you lost interest or pleasure in activities that you used to enjoy?",options=['Yes,all','Some','None'])

que8=st.selectbox("Have you experienced changes in your appetite or weight lately?",options=['Yes','No'])

que9=st.selectbox("Have you experienced changes in your sleep patterns lately?",options=['Yes','No'])

que10=st.selectbox("Have you been feeling tired or fatigued more than usual?",options=['Everyday','Sometimes','Never'])

st.markdown("-------")

st.markdown("# Results")







