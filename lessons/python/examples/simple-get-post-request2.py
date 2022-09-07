## python3 -m pip install urllib3

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import urllib3


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
http = urllib3.PoolManager()

### Get vs Post
# "Get" is less secure than "Post"
# "Get" sends data as part of the "URL"
# "Post" sends data within the "request body"

### Rest
# Rest is a WebAPI
# API is sets of protcols and defenitions

### Rest Rules
# Communications -> Http
# Stateless connection -> Each request is separate from each other
# Self-Descriptive Responces
# ...

### Alternative to REST
# SOAP
# ...

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get Request
for i in range(10, 20):
    resp = http.request("GET", "http://127.0.0.1:3000/profile/" + str(i))
    print(resp.data)

"""
Output:
b'<h1>PROFILE: 10</h1>'
b'<h1>PROFILE: 11</h1>'
b'<h1>PROFILE: 12</h1>'
b'<h1>PROFILE: 13</h1>'
b'<h1>PROFILE: 14</h1>'
b'<h1>PROFILE: 15</h1>'
b'<h1>PROFILE: 16</h1>'
b'<h1>PROFILE: 17</h1>'
b'<h1>PROFILE: 18</h1>'
b'<h1>PROFILE: 19</h1>'
"""