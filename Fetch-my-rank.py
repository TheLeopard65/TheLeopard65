import requests

def get_tryhackme_profile(username):
    try:
        response = requests.get(f'https://tryhackme.com/api/user/{username}')
        response.raise_for_status()
        data = response.json()
        return {
            'rank': data.get('rank', 'N/A'),
            'systems_owned': data.get('systems_owned', 'N/A'),
            'users_owned': data.get('users_owned', 'N/A'),
            'final_score': data.get('final_score', 'N/A'),
            'global_ranking': data.get('global_ranking', 'N/A')
        }
    except requests.RequestException as e:
        print(f"Error fetching TryHackMe data: {e}")
        return None

def get_htb_profile(username, api_token):
    try:
        headers = {
            'Authorization': f'Token {api_token}'
        }
        response = requests.get(f'https://www.hackthebox.com/api/v4/profile/{username}', headers=headers)
        response.raise_for_status()
        data = response.json()
        return {
            'rank': data.get('rank', 'N/A'),
            'systems_owned': data.get('systems_owned', 'N/A'),
            'users_owned': data.get('users_owned', 'N/A'),
            'final_score': data.get('final_score', 'N/A'),
            'global_ranking': data.get('global_ranking', 'N/A')
        }
    except requests.RequestException as e:
        print(f"Error fetching HTB data: {e}")
        return None

THM_username = 'Leopard65'
HTB_username = 'Leopard65'
HTB_api_token = 'your_htb_api_token'

THM_profile = get_tryhackme_profile(THM_username)
HTB_profile = get_htb_profile(HTB_username, HTB_api_token)

print(f"TryHackMe Rank: {THM_profile['rank']}")
print(f"Systems Owned: {THM_profile['systems_owned']}")
print(f"Users Owned: {THM_profile['users_owned']}")
print(f"Final Score: {THM_profile['final_score']}")
print(f"Current Global Ranking: {THM_profile['global_ranking']}")
print(f"HackTheBox Rank: {HTB_profile['rank']}")

with open('README.md', 'r') as file:
    content = file.readlines()

with open('README.md', 'w') as file:
    for line in content:
        if "TryHackMe Rank" in line:
            file.write(f"![TryHackMe Rank](https://img.shields.io/badge/TryHackMe-Rank%20-{THM_profile['rank']})\n")
        elif "Systems Owned" in line:
            file.write(f"**Systems Owned:** {THM_profile['systems_owned']}\n")
        elif "Users Owned" in line:
            file.write(f"**Users Owned:** {THM_profile['users_owned']}\n")
        elif "Final Score" in line:
            file.write(f"**Final Score:** {THM_profile['final_score']}\n")
        elif "Current Global Ranking" in line:
            file.write(f"**Current Global Ranking:** {THM_profile['global_ranking']}\n")
        elif "HackTheBox Rank" in line:
            file.write(f"**HackTheBox Rank:** {HTB_profile['rank']}\n")
        else:
            file.write(line)
