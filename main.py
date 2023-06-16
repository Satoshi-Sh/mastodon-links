import json
from mastodon import Mastodon;
from dotenv import dotenv_values;
env_vars = dotenv_values('.env')

def get(token,url):
    mastodon = Mastodon(
        access_token=token,
        api_base_url=url,
    )

    account_id = mastodon.account_verify_credentials()['id']
    following = mastodon.account_following(account_id)
    
    data = []
    for account in following:
        info = {}
        info['display_name'] =  account['display_name']
        info['username'] =  account['username']
        info['account'] =  account['acct']
        links= []
        for field in account['fields']:
            if "http" in field.value:
                links.append({"title":field.name,"link":field.value.split('"')[1]})
        info['links']=links
        data.append(info)
    filename = "sample_data/following_url.json"

    # Open the file in write mode
    with open(filename, "w") as file:
        # Write the dictionary data to the file as JSON
        json.dump(data, file)

    print("JSON file created: ", filename)


def main():
    get(env_vars['ACCESS_TOKEN'],env_vars['API_URL'])

if __name__== '__main__':
    main()
