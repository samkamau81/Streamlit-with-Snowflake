# Streamlit-with-Snowflake
## MentalMuse : AI FOR MENTAL HEALTH
### *By Samuel Waweru*
### Link: https://mentalmuse.streamlit.app/ 
-----------------
### TABLE OF CONTENT
- About the Project
- Technology Used
- Importance
- Prerequisites
- License
- How to Contribute to the Project


-----------------------
## About the Project
![github1](https://user-images.githubusercontent.com/63351043/235633634-3a0c43a6-0066-420f-8618-a851d9e27703.JPG)

This is an AI powered app that uses NLP to assess the mental state of a user an then uses data stored in Snowflake database i.e Location of Psychologists and Psychiatrists within their *county*. it utilizes Snowflake python connector 2 ,to connect the streamlit app with the database and nlp-bert-base-multilingual-uncased-sentiment algorithm to determine the polarity of the user.

### How does it work ;
Once the user has accessed the MentalMuse app , he/she answers questions in a questionnaire. Each question carries its own weight, depending on the relevance of the question in determining the mental state of the individual. Once the polarity of the answer they have given is predicted , it is then multiplied by the weight. This technique improves the accuracy of the prediction i.e. degree of their mental state. 

![image](https://user-images.githubusercontent.com/63351043/235637185-b3548151-4278-484d-8b9d-787b9a6c406a.png) ![image](https://user-images.githubusercontent.com/63351043/235637369-529d82cb-50b1-4fe7-9a48-f6d8ea5459e3.png)

The percentage stress level is output and then queried into the database and the solution based on it is given. Awesome , Right 😉!
The app also asks the location of the user and then from the database gets the address location of a psychaitrist/psychologists near them.

![image](https://user-images.githubusercontent.com/63351043/235637561-d7cd3e30-c253-4079-b714-2de9c5c0c256.png)

--------------------
## Technology Used
- STREAMLIT

I have utilized this framework to run MentalMuse. It was fun using it 😄
It is very easy to use.

![image](https://miro.medium.com/v2/resize:fit:828/format:webp/1*WG_wkTeaK3FdevXHNLxSTA.jpeg)

- Snowflake 

I have utilized this cloud platform to create my database and tables containing the Psychologist Office Location , Reviews and the advise
they offer dapending on the level of depression and stress generated.

![image](https://user-images.githubusercontent.com/63351043/235639933-39aad61c-fd57-479f-8682-5b8cdaff885d.png) ![image](https://user-images.githubusercontent.com/63351043/235640053-6faf76da-9d54-45b8-b7f7-1ea87746b222.png)


- Natural Language Processing

For this part , I have utilzed the bert-base-multilingual-uncased-sentiment to carry out the classification of the users input.
It is finetuned for sentiment analysis on feedback in six languages: English, Dutch, German, French, Spanish and Italian. It predicts the sentiment of the the input as a number of stars (between 1 and 5).

1 - Very Negative

5- very Positive

----------------------
## Importance

### The importance of MentalMuse is to help people get advice on how to tackle their mental health issues which are on the rise because of many reasons. According to the World health Organization , one in every 4 people suffer from Mental Health illness. Prevention and early intervention are key to promoting mental health and preventing the development of mental health conditions.


----------------------
## Prerequisites

From the requirement.txt;

- streamlit
- transformers==4.12.5
- torch==1.10.0
- bs4==0.0.1
- snowflake-snowpark-python
- Python 3.8

-------------------
## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


------------------




