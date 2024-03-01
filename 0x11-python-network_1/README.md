Certainly! Let's break down each topic:

### 1. Fetching Internet Resources with urllib:

Python's `urllib` module allows you to make HTTP requests to fetch internet resources. Here's a basic example of how to use `urllib` to fetch a webpage:

```python
import urllib.request

response = urllib.request.urlopen('http://www.example.com')
html = response.read()
print(html)
```

### 2. Decoding urllib Body Response:

The response obtained from `urlopen()` is in bytes format. To decode it into a string, you can use the `.decode()` method with the appropriate encoding. For example:

```python
html_decoded = html.decode('utf-8')
print(html_decoded)
```

### 3. Using the requests Package:

The `requests` package is simpler to use and more powerful than `urllib`. You can install it via pip (`pip install requests`) and use it like this:

```python
import requests

response = requests.get('http://www.example.com')
print(response.text)
```

### 4. Making HTTP GET Request:

With the `requests` package, making a GET request is straightforward:

```python
response = requests.get('http://api.example.com/data')
print(response.json())
```

### 5. Making HTTP POST/PUT/etc. Request:

To make other types of requests like POST or PUT, you can use the respective methods in `requests`:

```python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('http://api.example.com/post', data=payload)
print(response.text)
```

### 6. Fetching JSON Resources:

If the resource you're fetching is in JSON format, you can use the `.json()` method provided by `requests` to parse it directly:

```python
response = requests.get('http://api.example.com/data.json')
data = response.json()
print(data)
```

### 7. Manipulating Data from an External Service:

Once you've fetched data from an external service, you can manipulate it as needed. For example, with JSON data, you can access specific fields and perform operations on them:

```python
for item in data['items']:
    print(item['name'])
```

These are the basic concepts and techniques for networking in Python using `urllib` and the `requests` package. Remember to handle exceptions and errors appropriately, especially when working with network requests.