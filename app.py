# importing necessary dependancies
import streamlit as st
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from bs4 import BeautifulSoup

#instantiate NLP model
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# Comming up with functions
def causes(text): 
    # determines the major cause of stress an individual is facing
    family=0
    finance=0
    school=0
    relationship=0
    work=0
    text=text.lower()
    text=text.split()

    for i in (text):
        if i == 'school':
            school+=1
        elif i == 'family':
            family+=1
        elif i == 'finance':
            finance+=1
        elif i == 'relationship':
            relationship+=1
        elif i == 'work':
            work+=1
            
    
    return(st.bar_chart([family,finance,school,relationship,work], width=1000, height=1000, use_container_width=True))


def predict_polarity(text):
    #determines the polarity of each answer given by an individual
    tokens = tokenizer.encode(text, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1

def avg_sentiment(lis1,lis2):
    f_val=[]
    #determines the average putting into consideration weight
    for i,j in zip(lis1, lis2):
        val1=predict_polarity(i)*j
        f_val.append(val1)

    avg_f_val=sum(f_val)/len(f_val)
    return avg_f_val

        


# Set the app title
st.title("Psychological Support App")

st.image("https://cdn.pixabay.com/photo/2017/02/13/08/54/brain-2062057__340.jpg")

st.markdown("*** A simple machine laerning app to predict the the mental state of people and give advice on the way forward ***")
st.markdown("-------")
st.markdown("# Questionnaire")

st.markdown("## Answer these few questions to help me understand your situation more , Be very descriptive and fill every field")

st.markdown("-------")
form = st.form(key="my_form")

que0=form.selectbox("County of Resisdence",options=['Nairobi','Nakuru','Nyeri'])

# each question carries its own weight
que1=form.text_input("Can you tell me how you've been feeling lately?") #weight is 20%

que2=form.text_input("What's been on your mind lately?") #weight is 10%

que4=form.text_input("How have you been coping with stress lately?") #weight is 10%

que5=form.text_input("Can you describe your mood over the past few weeks?") #weight is 10%

que7=form.text_input("Have you lost interest or pleasure in activities that you used to enjoy?") #weight is 10%

que8=form.text_input("Have you experienced changes in your appetite or weight lately?") #weight is 10%

que9=form.text_input("Have you experienced changes in your sleep patterns lately?") # weight is 15 %

que10=form.text_input("Have you been feeling tired or fatigued more than usual?") #weight is 15 %

st.markdown("-------")

#list of questions and weights
weights=[20,10,10,10,10,10,15,15]
ques=[que1, que2, que4, que5, que7, que8, que9,que10]

b1=form.form_submit_button('Results')
b2=st.button('Clear')

st.markdown("-------")

st.markdown("# Results")

if b1:
    causes(que2)
    avg_value=avg_sentiment(ques,weights)
    st.write("This is Percentage level of your stress ", (100-avg_value))


elif b2:
    st.session_state['que1'] = ''  
    st.session_state['que2'] = ''  
    st.session_state['que4'] = ''  
    st.session_state['que5'] = ''  
    st.session_state['que7'] = ''  
    st.session_state['que8'] = ''  
    st.session_state['que9'] = ''  
    st.session_state['que10'] = ''  













