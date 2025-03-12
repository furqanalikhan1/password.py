import re
import streamlit as st

#page  style
st.set_page_config(page_title="Password Strength Checker By Furqan Ali Khan", page_icon="🔑",layout="centered")
#cuctom  css
st.markdown(""" 
<style>
   .main{text-align: center;}
    .stTextInput {width :60% !important; margin:auto; }
    .stButton button {width: 50%; background-color :bule; color:white; font-size:18px;}
    .stButton button {background-color: red; color: white;}
 </styl>       

""",unsafe_allow_html=True)

#oage title and decription
st.title("🔒Password Strength Generator")
st.write("Enter your password below to check its security level.🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback =[]

    if len (password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **atlease 8 character long**.")   

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password): 
         score+= 1
    else: 
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d",password):
        score+= 1 
    else:
        feedback.append  ("❌ Password should include **at least one number (0-9)**.")

     #special chatacters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌include **at least one special character([!@#$%^&*])**.")

    #display password strength results
    if score == 4:
        st.success("✔️ ** Strong Passwor** - Your password is secure.")
    elif score == 3:
         st.info("**Moderste Password** - Consider improving security by adding more feature")                        

    else:
        st.error(" ** Week pasword** - Follow the suggestion brlow to strength it. ")

     # feed back 
    if  feedback:
        with st.expander("** Improve your Password**"):
            for item in feedback:
                st.write(item)  
    password = st.text_input("Enter your password:",  type="password", help="Ensure yuor padssword is strong")        

    #button workin
    if st.button("check strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning(" Please enter a password first!")        
