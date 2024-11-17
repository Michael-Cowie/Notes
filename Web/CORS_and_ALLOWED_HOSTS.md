<div align="center">
  <h1> CORS_ORIGIN_WHITELIST </h1>
</div>

CORS stands for Cross-Origin Resource Sharing, which is a security feature implemented by web browsers to restrict web pages from making requests to a domain other than the one that served the page. `CORS_ORIGIN_WHITELIST` is a Django setting used when you're dealing with AJAX requests (or API requests) coming from a different origin (domain, protocol, or port) than your Django application.

The current example from within my backend server is,

```Python
CORS_ORIGIN_WHITELIST = [
     'http://localhost:3000',  # React
     'http://localhost:5173',  # Vite
     'http://localhost:1337'   # Nginx
]
```

This setting specifies a list of origins that are allowed to make cross-origin requests to the Django API. If a request comes from an origin not listed in this whitelist, it will be blocked by the browser's CORS policy.

#### CORS

To understand CORS better I will break it down and create a simple example from the context of a DRF (Django Rest Framework) application. Imagine you're building a web application using Django Rest Framework for the backend and a separate frontend framework like React.js or Angular.js for the client-side. These two parts might be hosted on different domains (e.g., backend on `api.example.com` and frontend on `app.example.com`).

When your frontend (e.g., JavaScript code running in the browser) tries to make requests to your Django Rest Framework API, the browser blocks these requests by default due to security reasons (CORS policy). To allow these cross-origin requests from your frontend to your Django Rest Framework API, you specify the domains (origins) that are allowed to access your API in the `CORS_ORIGIN_WHITELIST` setting.

When a client, typically a web browser, makes a cross-origin request to your Django application, it includes an Origin header in the HTTP request. This header indicates the domain from which the request originates. For example, if a frontend application hosted at `https://frontend.example.com` makes a request to your Django backend hosted at `https://api.example.com`, the `Origin` header in the request will be set to `https://frontend.example.com`.

Django middleware, specifically the Django CORS middleware when configured with `CORS_ORIGIN_WHITELIST`, checks this `Origin` header against the list of domains specified in `CORS_ORIGIN_WHITELIST`. If the domain specified in the `Origin` header matches any domain listed in `CORS_ORIGIN_WHITELIST`, Django includes the necessary CORS headers in the response to allow the cross-origin request. These headers inform the browser that the request is permitted and specify which methods (e.g., `GET`, `POST`) and headers can be used in the cross-origin request.

When hosting the backend to a server on the web, for example, `wwww.radix.fitness.com`, this will require updating of `CORS_ORIGIN_WHITELIST` to also include `radix.fitness.com`. An origin is a combination of hostname, port, and scheme.

```
https://foo.example.com:8080//
^^^^    ^^^^^^^^^^^^^^^ ^^^^   
 ||           ||         ||
scheme     hostname     port
```

Therefore, the request IP address is irrelevant here as CORS is primarily focusing on the `Origin` HTTP header field which indicates the domain from which the request originates. In summary, `CORS_ORIGIN_WHITELIST` is used to control access to your Django application based on the `Origin` header in cross-origin requests.

# `ALLOWED_HOSTS`

`ALLOWED_HOSTS` is used to ensure that your Django application only responds to requests with a valid `Host` header, preventing potential security vulnerabilities related to HTTP Host header manipulation. Both settings work in conjunction with the corresponding HTTP headers to enforce security policies and protect your application.

Now, suppose your Django Rest Framework API is deployed in a production environment, and you want to ensure that it only responds to requests coming from trusted sources. The `ALLOWED_HOSTS` setting comes into play here. It specifies a list of host/domain names or IP addresses that your Django Rest Framework API is willing to serve.

When a client sends a request to your Django application, it includes a `Host` header indicating the hostname to which it believes it is connecting. When a request is received by your API, Django checks the `Host` header to see if it matches any entry in the `ALLOWED_HOSTS` list. If it doesn't match, Django rejects the request, preventing potential attacks that exploit the mismatch between the request's host and the server's expectations. If the value matches any entry in `ALLOWED_HOSTS`, Django considers the request valid and proceeds with handling it. Otherwise, it raises a `SuspiciousOperation` error.

When a client sends an HTTP request to your Django application, it includes a `Host` header. This header specifies the domain name to which the client believes it is connecting. For example, if a client sends a request to `https://api.example.com`, the `Host` header in the request will be set to `api.example.com`. Django middleware checks this `Host` header against the list of host/domain names specified in the `ALLOWED_HOSTS` setting.