import requests

def get_tryhackme_ranking(username):
    try:
        response = requests.get(f'https://tryhackme.com/api/user/{username}')
        response.raise_for_status()
        data = response.json()
        if 'rank' in data:
            return data['rank']
        else:
            print(f"Unexpected response structure: {data}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching TryHackMe data: {e}")
        return None

def get_htb_ranking(username):
    try:
        response = requests.get(f'https://some-htb-api.com/user/{username}')
        response.raise_for_status()
        data = response.json()
        if 'rank' in data:
            return data['rank']
        else:
            print(f"Unexpected response structure: {data}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching HackTheBox data: {e}")
        return None

# Replace 'your_username' with your actual usernames
THM_username = 'Leopard65'
HTB_username = 'Leopard65'

THM_rank = get_tryhackme_ranking(THM_username)
HTB_rank = get_htb_ranking(HTB_username)

print(f"TryHackMe Rank: {THM_rank}")
print(f"HackTheBox Rank: {HTB_rank}")

# Update README.md (or any other file) with the fetched ranks
# Example: Writing the rank to a file (this is a placeholder approach)
with open('README.md', 'r') as file:
    content = file.readlines()

# Update the lines corresponding to the ranks
with open('README.md', 'w') as file:
    for line in content:
        if "TryHackMe Rank" in line:
            file.write(f"![TryHackMe Rank](https://img.shields.io/badge/TryHackMe-Rank%20-{THM_rank})\n")
        elif "HackTheBox Rank" in line:
            file.write(f"![HackTheBox Rank](https://img.shields.io/badge/HackTheBox-Rank%20-{HTB_rank})\n")
        else:
            file.write(line)
