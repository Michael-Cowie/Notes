<div align="center">
    <h1> Relational Databases</h1>
</div>

Relational databases organize data into **tables (relations)** of rows and columns. They follow the Relational Model formalized by E.F. Codd in 1970. Data integrity is enforced via schemas, ACID compliance and referential integrity using primary/foreign keys.

#### Common Implementations

- **PostgreSQL** - Open source, highly standards compliant.
- **MySQL / MariaDB** - Widely deployed, MySQL is Oracle-owned, MariaDB is its fork.
- **Microsoft SQL Server** - Enterprise integration 

##### Table Creation

```SQL
CREATE TABLE Employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department_id INT REFERENCES Departments(id),
    salary NUMERIC(10,2)
);
```

##### Table Appearance

| id | name  | department\_id | salary   |
| -- | ----- | -------------- | -------- |
| 1  | Alice | 10             | 85000.00 |
| 2  | Bob   | 20             | 92000.00 |

##### Example Query

```SQL
SELECT name FROM Employees WHERE salary > 90000;
```

##### Pros

- **Strong Consistency and ACID Transactions** - Guaranteed rollback, commit and isolation levels.
- **Mature Query Language (SQL)** - Set-based logic enables powerful analytics, joins and views.
- **Schema Enforcement** - Reduces application-level data validation logic.

##### Cons

- **Scalability Limitations (Vertical Scaling)** - Sharding and horizontal scaling is complex, e.g. PostgreSQL lacks native sharding.
- **Rigid Schema Evolution** - Requires migrations, which are downtime sensitive.
- **Join Overhead in Complex Queries** - For example, multi-table joins degrade performance with large datasets and lack of indexing.

<div align="center">
    <h1> Document Oriented Databases - NoSQL </h1>
</div>

Document databases store data as **semi-strucutred JSON or BSON documents**, typically nested and schema-flexible. Optimal for hierarchical or polymorphic data. An "id" field is not strictly required in most NoSQL databases, but **if you don't have it and don't create indexes** your searches can become brute-force linear scans `O(n)`, which are very slow in large datasets.

For this reason, MongoDB requires an `_id` field for every document. If you don't provide one, it automatically inserts it using an `ObjectId`. CouchDB requires an `_id` as a document key and finally Firestore also assigns a unique ID if not provided.

Efficient searching in NoSQL databases is not automatic, it requires **careful use of indexes, schema modeling** and sometimes plugins or external tools.

#### Common Implementations

- **MongoDB** - BSON-based, rich querying, indexing.
- **Couchbase** - Distributed with caching layer.
- **Amazon Document DB** - MongoDB compatible, AWS managed.

#### Example Data

```json
{
  "_id": "123",
  "name": "Alice",
  "department": {
    "id": 10,
    "name": "Engineering"
  },
  "skills": ["Python", "React"]
}
```

#### Example Query

```JavaScript
db.employees.find({ "skills": "React", "department.name": "Engineering" })
```

#### Pros

- **Flexible Schema** - Ideal for evolving models, microservices and unstructured data.
- **Nested and Polymorphic Structures** - Embedding avoids joins for performance.
- **Horizontal Scalability** - Easy to shard across nodes, e.g. MongoDBs `shardkey`.

#### Cons

- **Eventual Consistency** - In sharded clusters or replication lag scenarios, strong consistency is not default.
- **Lack of Joins and Normalization** - Relational-style queries require multiple round-trips or data duplication.
- **Indexing Complexity** - Must be explicitly defined and can be hard to optimize for deeply nested fields.

<div align="center">
    <h1> Key-Value Stores </h1>
</div>

These databases store data as **opaque values identified by unique keys**. Think of it as a distributed dictionary or hash map. High throughput and low latency are the goals.

#### Common Implementations

- **Redis** - In-memory, supports complex data types like sets and sorted sets.
- **Riak KV** - Distributed and eventually consistent.
- **Amazon DynamoDB** - Cloud-native, predictable performance.

#### Example Data

```BASH
SET user:123 '{"name": "Alice", "age": 30}'
GET user:123
```

#### Pros

- **Low Latency** - Often sub-millisecond, excellent for caching or session stores.
- **Horizontal Scalability** - Designed for sharding across multiple nodes.
- **Simple Operational Model** - No complex schemas, straightforward key access.

#### Cons

- **Lack of Rich Querying** - Can't perform range scans or filters unless explicitly engineerd.
- **Data Duplication** - Application must manage relationships or data aggregation.
- **Opaque Values** - No partial value updates without retrieving and rewriting the whole blob.

<div align="center">
    <h1> Columnar Databases </h1>
</div>

Optimized for **analytical workloads**, columnar stores store data **by columns instead of rows**, enabling massive compression and scan speeds for aggregates.

#### Common Implementations

- **Apache Cassandra** - Eventual consistency, massive write throughput.
- **ClickHouse** - OLAP, highly efficient columnar engine.
- **Google Bigtable** - Backbone of BigQuery and Firebase.

#### Example Data - Conceptual Column Oriented.

| name  | age | country |
| ----- | --- | ------- |
| Alice | 30  | NZ      |
| Bob   | 35  | US      |

Will be stored internally as,

- Column `name` - `["Alice", "Bob"]`
- Column `age` - `[30, 35]`
- Column `country` - `["NZ, "US"]`

#### Example Query - ClickHouse SQL

```SQL
SELECT country, avg(age) FROM users GROUP BY country;
```

#### Pros

- **Excellent Compression** - Column homogeneity allows run-length encoding, delta compression.

- **Fast Analytical Queries** - Skips irrelevant columns in `SELECT` for performance.

- **Distributed Ingestion** - Suited for time-series, logging and telemetry ingestion.

#### Cons

- **Poor for OLTP** - Updates and deletes are expensive (e.g., must rewrite column segments)
- **Complex Write Paths** - Writes are batched in MemTables/SSTables before merging (In Cassandra).
- **Schema Design is Non-Trivial** - Requires tuning partition keys, clustering keys, TTLS.

<div align="center">
    <h1> Graph Databases </h1>
</div>

Data is stored in **nodes and edges**, with edges representing relationships. Queries traverse graph structures efficiently. Ideal for networked data.

#### Common Implementations

- **Neo4j** - Rich Cypher query language.
- **ArangoDB** - Multi-model with graph capabilities
- **Amazon Neptune** - RDF and property graph support.

#### Example Data

```SCSS
(Alice)-[:FRIEND]->(Bob)
```

#### Example Query - Cypher

```Cypher
MATCH (a:Person)-[:FRIEND]->(b:Person)
WHERE a.name = "Alice"
RETURN b.name
```

#### Pros

- **Efficient Relationship Traversals** - Depth-first or breadth-first pathfinding is built-in.

- **Flexible Schemas** - Easily handles hierarchical or interconnected datasets.

- **Powerful Query Expressiveness** - Graph pattern matching is more intuitive than joins.

#### Cons

- **Not Ideal for Aggregates** - Poor performance on OLAP-style queries unless augmented.

- **Complex Transaction** - Traversal-based locks can complicate concurrency control./

- **Specialized Tooling** - Less ubiquitous than SQL. Developer ramp-up time is longer.