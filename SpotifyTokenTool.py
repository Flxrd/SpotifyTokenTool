import requests
# Put your spotify client ID and secret below, you can get them here;
# https://developer.spotify.com/documentation/web-api/tutorials/getting-started
ClientID = ""  # Spotify Client ID Here
ClientSecret = ""  # Spotify Client Secret Here
TokenTqUrl = "https://accounts.spotify.com/api/token"  # Future-proofing, You can ignore this.
rq = requests


# Makes the terminal output COLORFUL

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Ask spotify for a token by exchanging your Client details.
pretoken = rq.post(TokenTqUrl, data=f'grant_type=client_credentials&client_id={ClientID}&client_secret={ClientSecret}',
                   headers={'Content-Type': 'application/x-www-form-urlencoded'})
webtoken = pretoken.json()
spotifytoken = webtoken.get('access_token')

# Making sure the colors look ok
if pretoken.status_code == 200:
    # Print out the token with a status code
    print("Status code: " + colors.GREEN + str(pretoken.status_code) + " (" + str(pretoken.reason) + ")" + colors.END)
    print("Token Recieved: " + colors.BLUE + spotifytoken + colors.END)
else:
    print("Status code: " + colors.RED + str(pretoken.status_code) + " (" + str(pretoken.reason) + ")" + colors.END)
    print(colors.YELLOW + "Your ClientID/Secret is most likely wrong" + colors.END)
