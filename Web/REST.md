<div align="center">
    <h1> REST </h1>
</div>

REST (**RE**presentational **S**tate **T**ransfer) is an **architectural style** rather than a protocol. It governs the structure of networked applications using **stateless communication** and **uniform interfaces**. It was formally introduced by Roy Fielding in his doctoral dissertation in 2000 as a set of architectural principles for designing scalable and maintainable web systems.

REST is based on the concept of **resources**, which are entities identified by **URIs (Uniform Resource Identifiers)**. These resources can be retrieved, created, modified, or deleted using standard HTTP methods, and their **state is conveyed via representations**, most commonly using JSON in modern APIs.

Each HTTP method defines a contract between the client and the server, describing the **intended effect** of the request. These methods, while syntactically similar, vary significantly in purpose, behaviour and appropriate usage contexts.  HTTP methods are not merely verbs but are semantically significant operations that form the backbone of RESTful design. Mastery of their charasteristics including idempotency, safety, expected status codes and body semantics is essential to building APIs that are reliable, predictable and aligned with web standards.

Each method serves a precise purpose,

- `GET` - Retrieves
- `POST` - Creates
- `PUT` - Replaces
- `PATCH` - Updates
- `DELETE` - Removes

Misusing these verbs leads to semantic ambiguity, caching failures, idempotency bugs and security flaws.

#### Representation - `RE`ST

A **representation** is a server-generated, serialized form of a resource's state, sent to the client in a specific media type (JSON, XML, HTML, ...), which the client uses to understand or manipulate the resource.

Clients never interact with a resource directly. Instead, they interact with a **representation of the resource**, which is transferred over HTTP. This abstraction allows clients and servers to remain loosely coupled.

Representations are the only way clients interact with resources, they never directly access the data or internal models.

A resource `/users/42` may be represented as,

```JSON
{
  "id": 42,
  "name": "Alice",
  "email": "alice@example.com"
}
```

This JSON is a **representation** of the server-side resource.

This decouples **resources identity** (URI) from the representation format. Clients can specify which representation they want via the `Accept` header, e.g. `Accept: application/json`.

#### State - RE`S`T

State in REST refers to **application state**, not resource state. Application state is the context and transition held by the client as it interacts with the resources.

In REST,

- The **server holds the resource state** in the database as data.
- The **client holds the application state**, such as what page the user is on and what links are available.

The client **transfers application state** by selecting links and making HTTP requests that transition the state of the application. Suppose you're building a SPA and visiting `/user/123`. The actual data stored on the server is,

```JSON
{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com"
}
```

This is the server-side resource state and the JSON representation of that state. Within the application state,

1. The user is **currently viewing** this profile.
2. The client knows what came before, maybe they clicked on Alice from a user list.
3. The page includes a link, `GET /user/123/edit` or a form that lets them update it.

4. If the user clicks `edit` they'll navigate to another representation.

That **navigation between representations** and the context the client holds (Browsing, editing and confirming) is what REST means by **application state**.

RESTs "State Transfer" refer to how the **client transfers between states of the application** such as going from `user list → profile → edit form` by following links in representations. While client and server state matter, REST is named for the fact that **clients change application state by transferring representations** of resource state.

#### Transfer - RES`T`

Transfer refers to the **transmission of the resource representations** between client and server over HTTP.

In REST every interaction between client and server involves the transfer of representations, usually in JSON/XML. These transfers include not only data but also hypermedia controls (links, form, etc) that guide the client to the next valid action.

This is the "engine" of REST. The client drives the application forward by transferring representations and using embedded links or forms to trigger state changes.

#### Idempotency

Idempotency is a crucial criteria for `GET` and `PUT` requests. A request is idempotent if **sending it once or sending it 100 times, results in the exact same outcome on the server**. This side effects don't multiply.

- If an operation is idempotent, **retrying it is safe**. This is **very important in unreliable networks**.

- If it's not idempotent, repeating may lead to undesired effects such as duplicate transaction or multiple users being created.

There are **six fundamental REST constraints**, each of which directly impacts the design and expected behaviour of RESTful APIs and their use of HTTP methods.

#### Client-Server Architecture

REST mandates a clear separation between the client, which is responsible for the user interface and user experience and the server which handles business logic and data storage.

HTTP methods invoked by the client should operate solely on resource representations served by the server. This decoupling allows clients and servers to evolve independently, as long as the interface (URIs, method semantics and media types) is respected.

#### Statelessness

Each request from client to server must contain all necessary context. **The server must not store any session state between requests**.

Every HTTP method must carry sufficient information through headers, path parameters and body content to the server to fulfill the request. For example, a `PUT` request must contain the entire updated resource since the server cannot "remember" the previous states. This is why authentication tokens are sent **with every request**, because no client session is retained server-side.

#### Cacheability

Server responses must explicitly indicate whether they are cacheable. Proper caching improves performance and scalability.

`GET` requests should return cacheable responses where appropriate, using headers such as `ETag`, `Last-Modified` or `Cache-Control`. `POST`, `PUT`, `PATCH` and `DELETE` are generally considered **non-cacheable** unless explicitly stated otherwise.

```
GET /products/42
Cache-Control: public, max-age=86400
ETag: "v1-product-42"
```

#### Uniform Interface

The REST interface must be consistent across the system. This constraint is the most central to REST and it underpins the semantic usage of HTTP methods. It includes four sub-constraints,

1. **Resource Identification in URIs** - e.g. `/users/42`.

2. **Manipulation of Resources Through Representations** - e.g. JSON payloads modifying server-side state via `POST`, `PUT` or `PATCH`.

3. **Self-descriptive Messages** - Every message contains enough information to describe how to process, e.g. `Content-Type` and `Accept`.

4. **Hypermedia as the Engine of Application State (HATEOAS)** - Clients navigate the system via hyperlinks provided dynamically in responses.eeee

#### Layered System

A client cannot tell whether it is connected directly to the server or an intermediary such as a proxy, load balancer or cache layer. REST APIs must be designed to that intermediaries can operate transparently. For instance, `GET` responses should be cacheable headers to that proxies can cache them correctly.

This constraint also permits scaling out the API infrastructure without altering client behaviour.

<div align="center">
    <h1> GET Method </h1>
</div>

The `GET` method is used exclusively for **retrieving resource representations**. It is defined as **safe and idempotent**, meaning that it does not change any server-side state and may be repeated any number of times with identical effect.

The characteristics of the `GET` request include,

- **Request Body** - This is ignored by servers, not intended to carry a body. Having a request using GET ignores the body to maintain predictable, cacheable and idempotent behaviour. Caches (e.g. CDNs and proxies) key off the URL, not the body so different bodies with the same URL would be cached identically, leading to incorrect responses.

- **Cacheable** - Highly cacheable with appropriate headers (`Cache-Control`, `ETag`, `Last-Modified`).

- **Response** - `200 OK` with resource data, `304 Not Modified` with conditional headers or `404 Not Found`.

A simple example would be,

```
GET /api/users/42
```

<div align="center">
    <h1> POST Method </h1>
</div>

The `POST` method **submits an arbitrary payload** to a resource, typically resulting in the **creation of a new resource** or the execution of a processing operation. It is **neither safe or idempotent** as multiple identical requests may yield distinct results (e.g. duplicate records). `POST` means to **create a new subordinate resource** or **process an action**, where the server often does something new every time. If we attempt to create a new user,

```
POST /users
{
  "name": "Alice"
}
```

Each time this is called, the server might create a new user **with a new ID**.

```
POST #1 → creates /users/101
POST #2 → creates /users/102
```

So even though the body is the same, multiple `POST` requests **create multiple resources**. Repeating a `POST` may result in multiple **new resources** or actions such as charging a credit card twice.

Suppose we have an analogy of using `POST` to "Make me a coffee" Everytime you say it, you get another coffee. Therefore, saying it twice will request two coffees. This **is not idempotent**.

The characteristics of `POST` are,

- **Request Body** - This is required as it carries the new entity data.
- **Response** - `201 Created` if new resource is created, `200 OK` for action responses, `400 Bad Request` for invalid and `409 Conflict` for duplicate data.

A simply example to create create a new user would be,

```
POST /api/users
Body: { "username": "alice", "email": "alice@example.com" }
```

<div align="center">
    <h1> PUT Method </h1>
</div>

The `PUT` method is used to **fully replace an existing resource** with the representation provided in the request body. **It is idempotent**, meaning the same request repeated will produce the same result.

`PUT` fully replaces or updates a resource **at a known URI**. Each time you `PUT` the same data to the same URI, the result is the same.

```
PUT /users/123
{
  "name": "Alice"
}
```

In the above `PUT`, the first request will **create or update user `123` to `Alice`**. However, any consecutive `PUT` requests will **change nothing**, in other words the user with id `123` will still have the name `Alice`. You can repeat this `PUT` 100 times and the **server state stays the same**.

Suppose we use the same coffee analogy as `POST`. If we say "Make sure my coffee order at table #5 is a flat white". Saying it twice doesn't add more coffee.

The characteristics of `PUT` are,

- **Request Body** - Required. Any omitted fields may be reset or deleted.

- **Behaviour** - If the resource exists, it is updated. If it does not exist, **it may be created**. **Therefore, a `PUT` request maybe upsert**. It gives the possibility to create a resource too.

- **Response** - `200 OK` or `204 No Content` for successful replacement or `201 Created` if created.

The following example can be used to replace a users entire profile,

```
PUT /api/users/42
Body: { "id": 42, "username": "alice", "email": "new@example.com" }
```

<div align="center">
    <h1> PATCH Method </h1>
</div>

The `PATCH` method allows for **partial modification** of a resource. It is often, but not always idempotent. It depends on how the server interprets the patch.

The `PUT` method is defined to overwrite the entire resource with the request payload. Using `PUT` for partial updates is inconsistent with its definition.

The charasteristics of `PATCH` are,

- **Request Body** - Contains a subset of fields or a patch document.
- **Response** - `200 OK` or `204 No Content` upon succes, `409 Conflict` for constraint violations.

The following `PATCH` will update only the users email,

```
PATCH /api/users/42
Body: { "email": "patched@example.com" }
```

<div align="center">
    <h1> DELETE Method </h1>
</div>

The `DELETE` method instructs the server to **remove the resource** identified by the request URI. It is **idempotent**, as repeated requests yield the same result, that is that the resource is gone.

- **Request Body** - Generally disallowed or ignored.
- **Response** - `204 No Content` is standard, `404 Not Found` if the resource is already deleted.

The following will delete a user,

```
DELETE /api/users/42
```