# Mastodon-links
Script to get url from my following profile pages.
After setting up an environment and put 
```ACCESS_TOKEN="your-token" API_URL="your-instance"```
in .env file.

Run
```python main.py```
- If you like to get a csv file instead of a json file, run ```python main.py -f csv```
- How to get your access token [link](https://dev.to/bitsrfr/getting-started-with-the-mastodon-api-41jj) 

# Live page 
Just need a mastodon access token and the instance URL.
https://satoshi-sh-mastodon-links-frontend-2t1ln0.streamlit.app/

## JSON File Format 
```
[{"display_name": "",
    "username": "",
    "account": "",
    "links": [
      { "title": "", "link":"" },
      { "title": "", "link": "" },
      {
        "title": "",
        "link": ""
      },
    ]},....]
```
