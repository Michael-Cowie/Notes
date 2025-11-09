<div align='center'>
    <h1> Introduction </h1>
</div>

Structured Query Languages (SQL) is the standard language for defining, accessing, and managing data in relational databases. Originating at IBM in the 1970s as a practical implementation of Edgar F. Codd's relational model, SQL was designed to let users describe **what data they want** rather than how to retrieve it. This declarative approach became so effective that **SQL was adopted as an ANSI and ISO standard** in the 1980s, leading to its widespread use across many database systems.

Although SQL is a standardized language, there is **no single SQL Engine**. Instead, SQL is implemented by numerous database systems, such as PostgreSQL, MySQL, SQLite and Oracle Database. All of these follow the core SQL standard **but extend it in different ways**. These systems are often referred to as relational database management systems (RDBMS). They share the same fundamental concepts - tables, rows, columns, keys, joins and transactions. They can different in performance charasteristics, feature sets, design philosophies and specific extensions they add to SQL.

- **PostgreSQL** - Emphasizes standards compliance, extensibility and advanced features (window functions, custom data types, strong ACID guarantees). It is often considered the most complete and academically faithful SQL implementation.

- **MySQL** - Prioritizes simplicity and speed, making it popular for web applications. Historically, it relaxed some strict SQL rules to favour performance and scalability.

- **SQLite** - Is a lightweight, file-based SQL engine embedded in applications, ideal for mobile devices and local storage.
- **...**

These differences exist because **SQL defines the language**, while **each RDBMS defines how to implement the language and optimize it** for specific use cases. Thus, SQL remains universal, but database systems vary in capabilities and behaviours.

At the language level, SQL is composed of several core components. The **Data Definition Language (DDL)** specifies database structures through commands such as `CREATE TABLE` and `ALTER TABLE`. The **Data Manipulation Language (DML)** provides tools like `SELECT`, `INSERT`, `UPDATE` and `DELETE` for interacting with data. The **Data Control Langauge (DCL)** manages permissions, while **Transaction Control Language (TCL)** governs reliability through commands such as `COMMIT` and `ROLLBACK`. Together, these sublanguages form a complete toolkit for building structured, consistent and durable data systems.

For instance,

```SQL
SELECT name, salary
FROM employees
WHERE department = 'Engineering';
```

expresses a declarative request for specific records, while

```SQL
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2),
    department VARCHAR(50)
);
```

defines the structure in which those records will be stored.

To fully master SQL, one must understand both the language itself and the principles of relational design, including normalization, indexing, query planning, transactions, and concurrency control. These foundations remain consistent across all SQL-based systems, even as each RDBMS adds its own unique capabilities.

<div align='center'>
    <h1> SQL Implementations </h1>
</div>

The SQL language is defined by a family of ISO standards collectively known as ISO/IEC 9075. Importantly, this standard does not describe one fixed feature set that all database systems must implement. Instead, it consists of a core language and a very large number of **optional features**, grouped into modules. A vendor is free to choose which modules it will support.

For example, recursive queries, temporal blades, JSON, window functions, XML queries and object-relational features are all individually specification modules. There are hundreds of such optional features. Because implementing every component is enormously expensive and because vendors already had decades of legacy behaviour before many modules were standardized, no real SQL database implements 100% of the standard. Full compliance has never occurred in practice.

What the standard does require is that if you declare support for a feature, the feature must behave as defined. But you're allowed to support only a subset.

Even so, all major RDBMS (PostgreSQL, MySQL, ...) implement a common core of SQL syntax and semantics - basic DDL, DML SELECT statements, JOINs, constraints, transactions and so on. This core is the practical intersection of all implementations. Thus, no system implements 100% because the standard is too broad and modular. However, all major systems implement a shared core, because that portion is essential to relational operation and has been stable since SQL-92.

Each SQL implementation evolves historically and architecturally. Their internal storage engines, transaction models and procedural languages drive what parts of the SQL standard they can efficiently support.

- **PostgreSQL** - Is the closest to the standard in spirit. It supports CTEs, window functions, JSON, arrays and more. Often with behaviour aligned with the SQL:1999-SQL:2016 specifications.

- **MySQL** - Historically prioritized speed and implementation simplicity over strict correctness. For years it accepted non-standard `GROUP BY` behaviour and lacked CHECK constraints. Even today, it does not support everything PostgreSQL does (e.g. FULL OUTER JOIN and advanced indexing methods).

- **Oracle** - Uses yet another dialect with PL/SQL and many unique features and also has a distinct syntax (`ROWNUm`, special sequence mechanisms, ...).

- **...**

These differences are not "mistakes". They reflect divergent design goals. SQL is not like C++ where compilers attempt near-perfect compliance. SQL is more like a specification menu from which vendors pick dishes.

<div align='center'>
    <h1> ORMs </h1>
</div>

ORMs attempt to abstract the differences between SQL dialects. Django's ORM defines a high-level query representation that compiles into SQL for each backend. **Each backend** advertises a set of capabilities flags, e.g.

- Supports transactions.
- Supports partial indexes.
- Supports JSON containment operators.
- Supports window functions.

The ORM adapts based on these flags, and if something is impossible to express portably, Django exposes it only for engines that support it. For example.

- **PostgreSQL** gets additional ORM features such as [JSONField](https://docs.djangoproject.com/en/5.2/ref/models/fields/#jsonfield) operators, full-text search, array operators and the `Unaccent` function.

- **SQLite** receives simplified functionality. Django may emulate some features where posible such as storing booleans as integers.

- **MySQL** has a reduced feature set, especially for constraint enforcement and advanced queries.

This means any Django application can remain portable across engines only if you restrict yourself to the subset of behaviour that every chosen engine can support. As soon as you rely on PostgreSQL specific capabilities, whether that's an operator such as `@>` on JSONB, you lose portability. Django cannot magically invent missing engine features. If MySQL does not support `UNNEST` or SQLite does not support deferred constraints, the ORM cannot emulate them faithfully. However, you can use engine-specific features via a engine specific Django API extensions.
