import requests
import base64
import datetime


class Auth:

    @staticmethod
    def authentication():
        client_id = "1ae029bf595e43fb92d84232c842b1b5"
        client_secret = "809c6b2273634187843c5444e72f8375"
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        token_url = "https://accounts.spotify.com/api/token"
        method = "POST"
        token_data = {
            "grant_type": "client_credentials"
        }
        token_headers = {
            "Authorization": f"Basic {client_creds_b64.decode()}"  # <base64 encoded client_id:client_secret>
        }
        r = requests.post(token_url, data=token_data, headers=token_headers)
        print(r.json())
        valid_request = r.status_code in range(200, 299)
        token_response_data = r.json()

        if valid_request:
            now = datetime.datetime.now()
            access_token = token_response_data['access_token']
            expires_in = token_response_data['expires_in']  # seconds
            expires = now + datetime.timedelta(secconds=expires_in)
            did_expire = expires < now

