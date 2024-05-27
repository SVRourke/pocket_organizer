from requests import post

class PocketApi:
    base_url = 'https://getpocket.com/'
    redirect_uri = 'http://localhost:5000/authorize'

    base_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Accept': 'application/json'
    }

    def get_access_token(self, consumer_key):
        response = post(
            self.base_url + 'v3/oauth/request',
            headers = self.base_headers,
            data = {
                'consumer_key': consumer_key,
                'redirect_uri': self.redirect_uri
            })

        return response.json().get('code')

    def get_request_token(self, consumer_key, request_code):
        response = post(
            self.base_url + 'v3/oauth/authorize',
            headers = self.base_headers,
            data={
                'consumer_key': consumer_key,
                'code': request_code
            })

        return response.json().get('access_token')
    
    def construct_redirect_url(self, request_token):
        return self.base_url + f'/auth/authorize?request_token={request_token}&redirect_uri={self.redirect_uri}'

    
    # Stuff for items

    def list_items(self, consumer_key, access_token):
        response = post(
            self.base_url + 'v3/get',
            headers = self.base_headers,
            data = {
                'consumer_key': consumer_key,
                'access_token': access_token,
                "detailType": "complete"
            })

        return response.json().get('list')