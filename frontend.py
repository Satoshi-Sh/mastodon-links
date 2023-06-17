import streamlit as st
from main import getData

def main():
    st.set_page_config(page_title="Get Data")
    st.title("Get Mastodon Followers URL")
    st.write("We just need your access token and the url of your instance to craete a json file with your followings' url")
    
    token = st.text_input("Enter your access Token")
    url = st.text_input("ex. https://mastodon.xyz")

    button_clicked = st.button("Get Data")

    if button_clicked:
        if (token=="" or url==""):
           st.write("Please give me token and the instance url")
        else:
           json_str= getData(token,url.lower(),False)
           if json_str:
              st.download_button("Download JSON",data=json_str,file_name="following_url.json")
           else:
               st.write("Please check your token and the instance url. Something wrong...")
               
if __name__ == "__main__":
    main()