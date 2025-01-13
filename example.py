#link to chess.com
#documentation here https://chesscom.readthedocs.io/en/latest/
#and https://pypi.org/project/chess.com/

from chessdotcom import get_player_profile, Client
from chessdotcom import get_leaderboards

Client.request_config["headers"]["User-Agent"] = (
   "My Python Application. "
   "Contact me at email@example.com"
)
response = get_player_profile("fabianocaruana")
print(response)
response = get_leaderboards()
print(response)
#player_name = response.json['player']['name']
#or
#player_name = response.player.name


