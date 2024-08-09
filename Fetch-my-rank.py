import requests

def get_tryhackme_ranking(username):
    try:
        response = requests.get(f'https://tryhackme.com/api/user/{username}')
        data = response.json()
        return data['rank']  # Adjust according to the actual API response structure
    except Exception as e:
        print(f"Error fetching TryHackMe data: {e}")
        return None

# Function to get HackTheBox ranking (using a community tool)
def get_htb_ranking(username):
    try:
        response = requests.get(f'https://some-htb-api.com/user/{username}')  # Replace with actual URL
        data = response.json()
        return data['rank']  # Adjust according to the actual API response structure
    except Exception as e:
        print(f"Error fetching HackTheBox data: {e}")
        return None

# Replace 'your_username' with your actual usernames
THM_username = 'Leopard65'
HTB_username = 'Leopard65'

THM_rank = get_tryhackme_ranking(THM_username)
HTB_rank = get_htb_ranking(HTB_username)

print(f"TryHackMe Rank: {THM_rank}")
print(f"HackTheBox Rank: {HTB_rank}")
