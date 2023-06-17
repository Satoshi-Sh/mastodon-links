import json
import csv
from mastodon import Mastodon;
from dotenv import dotenv_values;
env_vars = dotenv_values('.env')
import argparse
import requests 

def generate_csv(data):
    csv_data = ''
    for row in data:
        csv_data += ','.join(row) + '\n'
    return csv_data


def getFollowings(token,url,isJSON,isFile):
    following = []
    mastodon = Mastodon(
        access_token=token,
        api_base_url=url,
    )

    account_id = mastodon.account_verify_credentials()['id']
    # Initial API request
    url = f"{url}/api/v1/accounts/{account_id}/following"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"limit": 40}
    response = requests.get(url, headers=headers, params=params)

    while response.status_code == 200:
        data = response.json()
        following.extend(data)
        
        link_header = response.headers.get("Link")
        if not link_header:
           break

        links = requests.utils.parse_header_links(link_header)
        # Check if there is a next URL in the response
        if len(links)>0 and links[0]['rel']=='next':
            next_url = links[0]['url']
            print(next_url)
            response = requests.get(next_url, headers=headers)
        else:
            print("Went through all the pages...")
            break

    if isJSON:
        return makeJSON(isFile,following)
    else:
        return makeCSV(isFile,following)

def process_arguments():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Example script with flags.')

    # Add flags or arguments
    parser.add_argument('-f', '--file', type=str, help='Choose File Format json or csv')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the flag and argument
    if args.file:
       print(f"Creating a {args.file} file...")
       if args.file.lower()=='csv':
           return False
    print(f"Creating a JSON file...")
    return True

def makeJSON(isFile,following):
    data = []
    for account in following:
        info = {}
        info['display_name'] =  account['display_name']
        info['username'] =  account['username']
        info['account_url'] =  account['url']
        links= []
        for field in account['fields']:
            if "value" in field and "http" in field["value"]:
                links.append({"title":field["name"],"link":field["value"].split('"')[1]})
        info['links']=links
        data.append(info)
        
    if isFile:
        filename = "data/following_url.json"

        # Open the file in write mode
        with open(filename, "w") as file:
            # Write the dictionary data to the file as JSON
            json.dump(data, file)

        print("JSON file created: ", filename)
    else:
        # get json string 
        print("File is ready to download!!")
        return json.dumps(data)
def makeCSV(isFile,following):
    data = [['username',"account","account_url","title","url"]]
    for account in following:
        for field in account['fields']:
            if  'value' in field  and "http" in field['value']:
                info=[account['username'],account['acct'],account['url'],field['name'],field['value'].split('"')[1]]
                data.append(info)
    if isFile:
        filename = "data/following_url.csv"

        # Open the file in write mode
        with open(filename, "w",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("CSV file created: ", filename)
    else:
        print("File is ready to download!!")
        return generate_csv(data)


def main():
    isJSON= process_arguments()
    getFollowings(env_vars['ACCESS_TOKEN'],env_vars['API_URL'],isJSON,isFile=True)
    

if __name__== '__main__':
    main()
