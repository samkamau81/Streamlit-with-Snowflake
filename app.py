# importing necessary dependancies
import streamlit as st
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from bs4 import BeautifulSoup
from snowflake.snowpark import Session

#instantiate NLP model
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# Establish Snowflake session
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets.snowflake).create()

session = create_session()
st.success("Connected to Snowflake!")

# Load data table
@st.cache_data
def load_data(table_name):
    ## Read in data table
    table = session.table(table_name)
    ## Do some computation on it
    table = table.limit(100)    
    ## Collect the results. This will run the query and download the data
    table = table.collect()
    return table

# Comming up with functions
@st.cache_data
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

    sum=family+finance+school+relationship+work
    df0=pd.DataFrame([[family,finance,school,relationship,work]], columns=['Family','Finance','School','Relationship','Work'])      

    if sum!=0:
        st.markdown("<h3 style='text-align:center;'>Environment that contributes the most to your issue is as shown; </h3>",unsafe_allow_html=True)
        st.bar_chart(df0, width=200, height=200, use_container_width=True)
        
@st.cache_data   
def predict_polarity(text):
    #determines the polarity of each answer given by an individual
    tokens = tokenizer.encode(text, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1

@st.cache_data
def avg_sentiment(lis1,lis2):
    f_val=[]
    #determines the average putting into consideration weight
    for i,j in zip(lis1, lis2):
        val1=predict_polarity(i)*j
        f_val.append(val1)

    avg_f_val=sum(f_val)/len(f_val)
    return avg_f_val


#Defining Tables in the Snowflake Database
psych_info = "PSYCHOLOGY_DATABASE.PUBLIC.LOCATION_REVIEW"
psych_advise="PSYCHOLOGY_DATABASE.PUBLIC.SOLUTION"

#Putting Tables in DataFrames
df1 = load_data(psych_info)
Loc_Info=pd.DataFrame(df1)
df2 = load_data(psych_advise)
Advise_info=pd.DataFrame(df2)

# Set the app title
st.image("https://raw.githubusercontent.com/samkamau81/Streamlit-with-Snowflake/main/mentalmuse.JPG?token=GHSAT0AAAAAAB3OTCLFHYQGUQEO47ZJV3PAZCQYPZA")
#st.markdown("<h1 style='text-align:center;'>Big Headline</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;'> AI FOR MENTAL HEALTH </h1>",unsafe_allow_html=True)

st.markdown("-------")
st.markdown("<h2 style='text-align:center;'> Questionnaire </h2>",unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center;'> Answer these few questions to help me understand your situation more</h3>",unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'> Be very descriptive and fill every field if possible</h4>",unsafe_allow_html=True)

st.markdown("-------")
form = st.form(key="my_form", clear_on_submit=True)

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

st.markdown("<h2 style='text-align:center;'>Your Results from my analysis are; </h2>",unsafe_allow_html=True)

if b1:
    
    avg_value=100-(avg_sentiment(ques,weights))
    if avg_value!=50:
        st.metric(label="### Stress Level", value=avg_value, delta=(avg_value-50) ,delta_color="inverse")
        #stress level and actions to be taken
        for i in range(len(Advise_info)):
            if avg_value >= (Advise_info.iloc[i, 0]):
                st.write("### Advice: ", Advise_info.iloc[i, 1])
                break    

            #Location to seek more medical attention
 
        for j in range(len(Loc_Info)):
            if que0 == Loc_Info.iloc[j,1]:
                st.write("### Visit : "+" "+str(Loc_Info.iloc[j, 0])+" "+"whose reviews are "+" "+str(Loc_Info.iloc[j, 2])+"/5"+" "+"within"+" "+str(Loc_Info.iloc[j, 1])+" "+"at"+" "+str(Loc_Info.iloc[j, 3]))


        causes(que2)
        
    else:
        st.write("<h3 style='text-align:center;'>PLEASE FILL IN THE FIELDS!</h3>",unsafe_allow_html=True)

 



st.markdown("-------")
st.markdown("<h1 style='text-align:center;'> Did You Know ?</h1>",unsafe_allow_html=True)
st.image("https://www.intecbusinesscolleges.co.uk/Uploaded/1/Image/1in4people.jpg")
st.markdown("<em style='text-align:center;'> according to the World Health Organization </em>",unsafe_allow_html=True)
st.markdown("-------")
st.markdown("<h1 style='text-align:center;'>Practice self-care, and always stay connected. </h1>",unsafe_allow_html=True)


st.markdown("<h4 style='text-align:center;'> Want to contribute to the Project</h4>",unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'> github: https://github.com/samkamau81/Streamlit-with-Snowflake/tree/main </h4>",unsafe_allow_html=True)










