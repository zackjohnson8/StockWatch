class StockbrokerCredentialModel:
    def __init__(self, client_id, redirect_url, refresh_token, access_token=None):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.redirect_url = redirect_url
