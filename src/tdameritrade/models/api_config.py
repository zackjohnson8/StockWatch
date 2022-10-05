class APIConfig:
    def __init__(self, refresh_token, client_id, redirect_url, access_token=None):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.redirect_url = redirect_url
