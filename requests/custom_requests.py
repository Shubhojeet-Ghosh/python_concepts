import requests

class APIClient:
    def __init__(self, base_url, headers=None, timeout=30):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.timeout = timeout

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e), "response": getattr(e, 'response', None)}

    def get(self, endpoint, params=None, **kwargs):
        
        return self.request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        
        return self.request("POST", endpoint, data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        return self.request("PUT", endpoint, data=data, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)

    def set_header(self, key, value):
        self.session.headers[key] = value


# Usage 

client = APIClient(
    base_url="https://api.example.com",
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)

# GET request
response = client.get("/users")

# POST request with JSON
response = client.post("/users", json={"name": "Alice"})

# Update header
client.set_header("X-Custom-Header", "value123")
