import streamlit as st
from main import getFollowings

def main():
    st.set_page_config(page_title="Get Data")
    st.title("Get Mastodon Followers URL")
    st.write("We just need your access token and the url of your instance to craete a json file with your followings' url")
    st.markdown("How to get an access token [guide](https://dev.to/bitsrfr/getting-started-with-the-mastodon-api-41jj#:~:text=Find%20your%20access%20token)")
    token = st.text_input("Enter your access Token.")
    url = st.text_input("Enter your instance url. ex. https://mastodon.xyz")

    options = ['json', 'csv']
    selected_option = st.radio('Select a file format', options)

    button_clicked = st.button("Get Data")

    if button_clicked:
        if (token=="" or url==""):
           st.write("Please give me token and the instance url")
        else:
           isJson = selected_option=='json'
           if isJson:
               json_str= getFollowings(token,url.lower(),isJson,False)
               if json_str:
                  st.download_button("Download JSON",data=json_str,file_name="following_url.json")
               else:
                  st.write("Please check your token and the instance url. Something wrong...")
           else:
               csv_data = getFollowings(token,url.lower(),isJson,False)
               if csv_data:
                  st.download_button(label='Download CSV', data=csv_data, file_name='following.csv', mime='text/csv')
               else:
                  st.write("Please check your token and the instance url. Something wrong...")
if __name__ == "__main__":
    main()