# Mastodon-links
Script to get urls from my following profile pages.
After setting up an environment and put 
```ACCESS_TOKEN="your-token" API_URL="your-instance"```
in .env file.

Run
```python main.py```

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
