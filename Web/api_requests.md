<div align="center">
    <h1> Fundamental HTTP Architecture </h1>
</div>


HTTP (HyperText Transfer Protocol) operates as a **stateless, application-layer protocol** built on top of TCP/IP. Each HTTP transaction consists of a request-response cycle where the client initiates communication and the server responds with the requested resource or appropriate status information.

<div align="center">
    <h1> HTTP Structure </h1>
</div>

## Request

An HTTP request contains several distinct components organized in a specific hierarchical structure.

```
┌───────────────────────────────────────┐
│ Request Line                          │
├───────────────────────────────────────┤
│ Headers - (Multiple Key-Value Pairs)  │
├───────────────────────────────────────┤
│ Empty Line - (CRLF)                   │
├───────────────────────────────────────┤
│ Message Body - (Optional)             │
└───────────────────────────────────────┘
```

The **request line** contains three critical components.

1. **HTTP Method** - Defines the action be to performed (`GET`, `POST`, `PUT`, ...)
2. **Request URI** - Specifies the target resource path
3. **HTTP Version** - Indicates protocol version (`HTTP/1.1`, `HTTP2`, `HTTP/3`, ...)

Example - `POST /api/v1/users HTTP/1.1`

In an HTTP request, the client already knows the server because it had to resolve it using DNS before making the connection. Hence, the URI only specifies the resource. The host is specified separately in the `Host` header. We distinguish the URI from the URL in the following way,

- **URI (Uniform Resource Identifier)** - Formal **identifier** for a resource, by name, location or both. It is a general identifier.

```ini
search?q=what+is+the+temperature
```

The above URI will identify a resource relative to a server. It does no contain a scheme or hostname.

- **URL (Uniform Resource Locator)** - Formal **locator**. It identifies **and locates** a resource and how to access it. **All URLs are URIs, but not all URIs are URLs**.

```http
https://www.google.com/search?q=what+is+the+temperature
```

The above URL identifies **and locates** the source. It includes the protocol (`https`) and server address (`www.google.com`). This can be used directly to make a request.

Analogies,

- **File Name vs File Path** - The file name `report.pdf` will act as the URI, whereas `https://files.example.com/reports/report.pdf` will act as the URL. `report.pdf` is just the name, a reference. The URL is the full path to **retrieve** the file from the web.

- **Username vs Email Address** - The URI will be `@exampleuser`, whereas the URL would be `mailto:exampleuser@example.com`. A username tells **who**, whereas an email address tells **who and how to contact them**.

- **Function Signature vs API Endpoint** - The URI would be `/users/{id}`, whereas the URL would be `https://api.example.com/users/42`. The URI defines the structure **or resource name**. Whereas, the URL gives the **exact location** for that instance.

## Response

HTTP responses mirror request structure but include status information.

```
┌─────────────────────────────────────┐
│ Status Line                         │
├─────────────────────────────────────┤
│ Response Headers                    │
├─────────────────────────────────────┤
│ Empty Line (CRLF)                   │
├─────────────────────────────────────┤
│ Response Body                       │
└─────────────────────────────────────┘
```

The **status line** in an HTTP response has the following structure,

```
<HTTP-Version> <Status-Code> <Reason-Phrase>
```

- **HTTP-Version** - Protocol version used **by the server** - `HTTP/1.0`, `HTTP/1.1`, ...
- **Status-Code** - A 3-digit number indicating result of request - `200`, `404`, `500`, ...
- **Reason-Phrase** - `OK`, `Not Found` - Human-readable explanation of the status code.

## Header

**Headers are metadata** about the request or response, **formatted as key-value pairs** separated by colons. They provide essential information about the request context, content type, authentication, caching directions and more. Headers are always present in HTTP requests and are transmitted before the body.

Common header categories include,

- **General Headers** - Apply to both requests and response (`Cache-Control`, `Connection`)
- **Request Headers** - Client-specific information (`User-Agent`, `Accept`, `Authorization`)
- **Entity Headers** - Describe message body properties (`Content-Type`, `Content-Length`)

The most critical headers include,

- **Host** - Specifies the target server. - `Host: api.example.com`
- **Content-Type** - Describes the media type of the request body. - `Content-Type: application/json`
- **Authorization** - During login or authentication, a user sends their password to the server in the request body of a `POST` request. After successful authentication, the client gets a token such as JWT or OAuth token. This is the token that is sent in the `Authorization` header. - `Authorization: Bearer <token>`
- **Accept** - Specifies which content types the client can handle. - `Accept: application/json`
- **User-Agent** - Identifies the client application. A Postman request could be `User-Agent: PostmanRuntime/7.32.2`. It follows the format `User-Agent: <product>/<version> <comment>`. This is useful as the server can tailor the response based on the client such as sending mobile-optimized content to phones and HTML for browsers for browers but JSON for API clients.
- **Content-Length** - Indicates the size of the request body in bytes. - `Content-Length: 85`

## Body

**Contains the actual data payload** being sent to the server. Unlike headers, the body can contain binary data, structured text or any format specified by the `Content-Type` header. The body is typically not used for `GET` and `DELETE`, although not a forced requirement. It is typically used for `POST` and `PUT` operations.

#### Example

```HTTP
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
Accept: application/json
User-Agent: Mozilla/5.0 (compatible; API-Client/1.0)
Content-Length: 85

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securePassword123"
}
```

<div align="center">
    <h1> Passing Data in HTTP Requests </h1>
</div>

## Query Parameters

Query parameters are **key-value pairs**. Query parameters are part of the full URL, but not part of the URI path. They come **after the path component**, separated by a `?`. They are used to send small amounts of **non-sensitive** data the server, typically for filtering, sorting, searching and pagination and similar use cases. Though query parameters **can technically** be used in any method, they are standard practice **only for** `GET` **and** `DELETE`.

- **Filtering** - `?category=electronics`
- **Sorting** - `?sort=price_desc`
- **Search** - `?q=table%20tennis%20rubber`
- **Pagination** `?page=2&limit=20`

In the previous example,

```http
https://www.google.com/search?q=what+is+the+temperature
```
- **Scheme** - `https` - Protocol used.
- **Authority** - `www.google.com` - Domain name, which may also include the port.
- **Path** - `/search` - Resource being used.
- **Query** - `q=what+is+the+temperature` - Key-value data, **the query parameters**.
- **Fragment** - None in this example - It's an optional anchor, such as `#section1`.

Query strings are structured as,

```ini
key1=value1&key2=value2&key3=value3
```

- Each pair is separated by `&`
- Keys and values are separated by `=`
- Keys and values are **percent-encoded** (URL encoding)

Certain characters are reserved in URIs and must be percent-encoded if used in value or keys.

- Space - Encoded as `%20` or `+`
- `&` - Encoded as `%26`
- `=` - Encoded as `%3D`
- `?` - Encoded as `%3F`

`URLSearchParams` can be used to easily handle query parameters.

```TypeScript
const params = new URLSearchParams({
  page: '1',
  limit: '10',
  filter: 'active'
});
const url = `https://api.example.com/users?${params.toString()}`;
```

Will give `url.toString()` as,

```http
https://api.example.com/users?page=1&limit=10&filter=active
```

Alternatively, the `URL` could used.

```TypeScript
const url = new URL('/users', 'https://api.example.com');
url.searchParams.set('page', '1');
url.searchParams.set('limit', '10');
url.searchParams.set('filter', 'active');
```

Will give `url.toString()` as,

```http
https://api.example.com/users?page=1&limit=10&filter=active
```

To mimc these requests using Postman, the key value are used in the `Params` tab.

<div align="center">
  <img src="./images/1.png">
</div>

## Request Headers

HTTP request headers are key-value pairs sent by the client to the server in an HTTP request. They provide **metadata** about the request context such as content type, authorization, client info and more.

The header is a line in the format of,

```HTTP
<Header-Name>: <Header-Value>
```

#### Basic `POST` request using `fetch` with headers.

```TypeScript
const url = new URL("https://api.example.com/data");

const response = await fetch(url.toString(), {
  method: "POST",
  headers: {
    "Content-Type": "application/json",         // Tells the server we're sending JSON
    "Authorization": "Bearer YOUR_TOKEN_HERE",  // Bearer token for auth
    "Accept": "application/json"                // We expect JSON in response
  },
  body: JSON.stringify({ key: "value" })
});
```

Here we specify the request headers,

- `Content-Type` - Describes the MIME type of body, this is required for JSON payloads.
- `Authorization` - Provides credentials. In this case, a Bearer token used for OAuth2/JWT authentication.
- `Accept` - Indicates that the client wants the response in `application/json` format.

In Postman the `Authorization` is placed into the `Authorization` tab. The type here is set to `Bearer Token`.

<div align="center">
  <img src="./images/2.png">
</div>

The `Authorization` is placed onto the request header. It has its own tab but is visible if we extend the hidden headers section on Postman. Shown below, Postman places the `Authorization` request header onto the HTTP request. Additionally, we can observe extra request headers such as `User-Agent`.

<div align="center">
  <img src="./images/3.png">
</div>

<div align="center">
  <img src="./images/4.png">
</div>

Under the Body section in Postman, we choose the `raw → JSON`. Postman will implicitly add `Content-Type: application/json` in the request header, therefore this is not required to be manually added.

<div align="center">
  <img src="./images/5.png">
</div>

Finally, Postman has a default `Accept` which is set to `*/*`. This means that it is a wildcard that accepts all forms of data. This means using the default `Accept` in Postman we do not need to set `Accept` like the TypeScript example above.

<div align="center">
  <img src="./images/6.png">
</div>

#### Custom headers with `POST`

```TypeScript
const url = new URL("https://api.example.com/upload");

await fetch(url.toString(), {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-App-Version": "1.0.0",           // Custom header to indicate app version
    "X-Client-ID": "my-client-123"      // Custom header for client identification
  },
  body: JSON.stringify({ filename: "report.pdf" })
});
```

- `X-App-Version` and `X-Client-ID` are **custom headers**, often used to transmit client-specific metadata.
- These can be used by servers for telemetry, versioning or conditional logic.

#### `GET` request using Axios with headers

```TypeScript
import axios from "axios";

const url = new URL("https://api.example.com/user");
url.searchParams.set("id", "42");

const response = await axios.get(url.toString(), {
  headers: {
    Authorization: `Bearer ${token}`,     // Auth header
    Accept: "application/json"            // Specifies the desired response format
  }
});
```

- `Authorization` - JWT or OAuth Bearer token used for verifying the user identity.
- `Accept` - Informs the server the client prefers the response in JSON format.

## Request Body

The HTTP request body is the **payload** sent by the client to the server and is typically used to, 

- Create, update or submit data.
- Transmit structured or binary data.
- Used primarily with `POST`, `PUT`, `PATCH`. It is not intended to be used with `GET`.
  
Unlike headers or query parameters, the body is not visible in the URL or metadata, it's the main data payload. The structure of the body depends on the `Content-Type` header. Sensitive data such as passwords and access tokens should go in the body, not the URL. 

#### JSON Body Example

This is the most common body structure for modern APIs. Data is serialized as JSON.

```TypeScript
const data = {
  username: "example_username",
  email: "example_email@example.com"
};

await fetch("https://api.example.com/users", {
  method: "POST",
  headers: {
    "Content-Type": "application/json", // Tells the server we're sending JSON
    "Accept": "application/json"
  },
  body: JSON.stringify(data)
});
```

#### Form URL-Encoded Body

Traditional web form format, similar to query parameters but in the body. The following will send `'username=username123&password=securepass'` within the request body.


```TypeScript
const params = new URLSearchParams();
params.set("username", "username123");
params.set("password", "securepass");

await fetch("https://api.example.com/login", {
  method: "POST",
  headers: {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  body: params.toString()
});
```

#### Form Data

`FormData` is a built-in Web API that constructs a `multipart/form-data` body. It is a MIME-encoded format used to submit **forms with text fields, files or binary** via HTTP. It is commonly used in `POST` or `PUT` requests when uploading files or submitting complex forms.

The `application/x-www-form-urlencoded` format only supports simple key-value pairs, whereas `application/json` cannot encode file streams. `multipart/form-data` supports Files (binary), Text fields (UTF-8) and mixed parts (Metadata + file).

```HTML
<input type="file" id="fileInput" />
```

```TypeScript
const fileInput = document.getElementById("fileInput") as HTMLInputElement;

if (fileInput.files && fileInput.files.length > 0) {
  const formData = new FormData();
  formData.append("avatar", fileInput.files[0]); // Attach the first file

  await fetch("https://api.example.com/upload", {
    method: "POST",
    body: formData
  });
}
```

#### Raw Text

```TypeScript
await fetch("https://api.example.com/raw", {
  method: "POST",
  headers: {
    "Content-Type": "text/plain"
  },
  body: "This is a raw string payload"
});
```
