from flask import *
from flask_accept import accept
import os, requests as c,json


port = int(80)
ip= c.get('https://icanhazip.com').text
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
os.system('cls')
app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["300 per day", "50 per hour"]
)
@app.route('/growtopia/server_data.php', methods=['POST'])
@limiter.limit("15 per minute")
@accept('application/x-www-form-urlencoded')
def web():
    return "server|"+ip+"\nport|"+port+"\ntype|1\n#maint|Maintance message (Not used for now) -- PandaEver\n\n\nbeta_server|"+ip+"\nbeta_port|"+port+"\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001"
@app.errorhandler(404)
def error(e):
	return "Ngapa Lu Liat-Liat, Webserver Setup By PandaEver,WhatsApp: 6282278103764"
@app.errorhandler(406)
def errorx(e):
	return "Awokwokwokwok Masih Ga Keliatan:v, Webserver Setup By PandaEver,WhatsApp: 082278103764"
@app.errorhandler(405)
def errorz(e):
	return "Awokwokwokwok G Keliatan, Webserver Setup By PandaEver,WhatsApp: 6282278103764"
@app.errorhandler(429)
def errors(e):
	return "Hayolo Gak Down Ya:v, Webserver Setup By PandaEver,WhatsApp: 6282278103764"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT','80')),debug=False)
