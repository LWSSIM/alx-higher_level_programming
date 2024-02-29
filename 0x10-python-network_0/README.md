## README: Understanding Web Concepts

### What is a URL?
A Uniform Resource Locator (URL) is a reference to a web resource that specifies its location and how to retrieve it. It typically consists of several components, including the protocol scheme, domain name, path, query parameters, and fragment identifier.

### What is HTTP?
Hypertext Transfer Protocol (HTTP) is an application protocol used for transmitting hypermedia documents, such as HTML. It defines how messages are formatted and transmitted between web servers and clients, enabling the retrieval and display of web content.

### How to Read a URL
A URL is composed of several parts:
- **Scheme**: Indicates the protocol used (e.g., `http`, `https`).
- **Domain**: Specifies the network location of the resource.
- **Port**: Optional port number if different from the default (e.g., `:8080`).
- **Path**: The specific resource within the domain.
- **Query String**: Optional parameters passed to the resource.
- **Fragment Identifier**: A specific portion of the resource (e.g., anchor tags in HTML).

### The Scheme for a HTTP URL
HTTP URLs typically have the scheme `http://` or `https://` for secure connections.

Example:
```
http://www.example.com/page.html
```

### What is a Domain Name?
A domain name is a human-readable label that represents the numerical IP address of a web server. It allows users to access websites without needing to remember complex numeric addresses.

### What is a Sub-domain?
A sub-domain is a subset of a larger domain, often used to organize and categorize website content. It precedes the main domain name and is separated by a period.

Example:
```
blog.example.com
```

### How to Define a Port Number in a URL
To specify a port number in a URL, append it after the domain name with a colon.

Example:
```
http://example.com:8080/page.html
```

### What is a Query String?
A query string is a part of a URL that contains parameters used to pass data to the server. It begins with a question mark `?` and consists of key-value pairs separated by ampersands `&`.

Example:
```
http://example.com/search?q=query&page=2
```

### What is an HTTP Request?
An HTTP request is a message sent by a client to request a specific action from a web server. It consists of a request line, headers, and optionally a message body.

Example:
```
GET /index.html HTTP/1.1
Host: example.com
```

### What is an HTTP Response?
An HTTP response is a message sent by a server to fulfill a client's request. It includes a status line, headers, and optionally a message body containing the requested resource.

Example:
```
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
...
</html>
```

### What are HTTP Headers?
HTTP headers are additional metadata sent in both requests and responses to provide information about the message or to control various aspects of communication.

Example:
```
Content-Type: application/json
Authorization: Bearer token123
```

### What is the HTTP Message Body?
The HTTP message body contains the actual content being transmitted, such as HTML, JSON, or binary data. It follows the headers and is separated by a blank line.

### What is an HTTP Request Method?
An HTTP request method indicates the desired action to be performed for a given resource. Common methods include GET, POST, PUT, DELETE, etc.

Example:
```
GET /index.html HTTP/1.1
```

### What is an HTTP Response Status Code?
An HTTP response status code indicates the outcome of the server's attempt to fulfill the client's request. It provides information about whether the request was successful, failed, or requires further action.

Example:
```
HTTP/1.1 404 Not Found
```

### What is an HTTP Cookie?
An HTTP cookie is a small piece of data sent from a web server and stored in the user's web browser. It is used to track user activity, maintain session state, and personalize web content.

### How to Make a Request with cURL
cURL is a command-line tool for transferring data with URL syntax. You can use it to make HTTP requests and retrieve web content easily.

Example:
```bash
curl http://example.com/page.html
```

### What Happens When You Type google.com in Your Browser (Application Level)
1. The browser initiates a DNS lookup to translate the domain name (`google.com`) into an IP address.
2. Once the IP address is obtained, the browser establishes a TCP connection to the web server hosting Google.
3. The browser sends an HTTP GET request for the default resource (e.g., homepage) to the server.
4. Google's server processes the request, generates an appropriate HTTP response, and sends it back to the browser.
5. The browser receives the response, renders the HTML content, and displays the Google homepage to the user.
