## python3 -m pip install urllib3

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import urllib3


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
http = urllib3.PoolManager()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get Request
resp = http.request("GET", "http://127.0.0.1:3000/")
print(resp.data)
# b'<h1>HOME PAGE</h1>'


# Get Request
resp = http.request("GET", "http://127.0.0.1:3000/profile/HAMID")
print(resp.data)
# b'<h1>PROFILE: HAMID</h1>'


# Get Request
resp = http.request("GET", "http://127.0.0.1:3000/profile/SAEED")
print(resp.data)
# b'<h1>PROFILE: SAEED</h1>'


# Post Request
resp = http.request("POST", "http://127.0.0.1:3000/data", body="Hello World")
print(resp.data)
# b"<h1>DATA: b'Hello World'</h1>"
