<div align="center">
    <h1> ZODB </h1>
</div>

The Zope Object Database (ZODB) is a mature, Python-native, object-oriented database designed for applications requiring persistent storage of complex, interrelated Python objects. Unlike traditional or document-oriented database that require a transform layer (e.g. ORM), ZODB operates directly on Python objects, eliminating impedance mismatch and enabled transparent persistence.

### Database Classification and Design Principles

#### Type of Database

ZODB is a native object-oriented, ACID-compliant, NoSQL embedded database. It is neither relational or key-value in the conventional sense. Instead, it provides presistent object storage within Python applications. Objects are stored directly and the database maintains object identity, references and state across sessions.

#### Primary Design Goals

- **Native Persistence** - Store and retrieve Python objects without translation or schema enforcement.

  * **Translation** refers to transforming objects into rows, documents, or custom serialization formats. For example, converting a Python object into a table row via an ORM (like SQLAlchemy) or into a JSON document for MongoDB.

  * **Schema** enforcement refers to predefined, rigid structures (such as relational table definitions or schema validation in XML/JSON) that require explicit field definitions and constrain changes.

- **Transparent Transactions** - Ensure consistency and durability of object graphs with minimal boilerplate.

- **Efficient Object Graph Management** - Track and serialize complex interrelated structures, including circular references.

#### Core Concepts and Architecture


#### Persistent Objects

Objects to be stored in ZODB must subclass `persistent.Persistent`. This base class enables ZODB's internal change tracking mechanism. When a persistent object is modified, it is automatically flagged as "dirty" and ZODB writes only the changed object to disk during a transaction.

```python
from persistent import Persistent

class Person(Persistent):
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

ZODB supports nested and cyclic structures and objects maintain their identity and reference integrity upon retrieval.

#### Change Tracking and `_p_changed`

ZODB uses a special attribute, `_p_changed` to detect and track object modifications.

- `_p_changed = None` - Object in ghost state (not yet loaded).
- `_p_changed = False` - Object is in memory but unmodified.
- `_p_changed = True` - Object has been modified and will be written during the next commit.

When persistent attributes are updated, ZODB sets `_p_changed = True` automatically. However, mutations to non-persistent containers like regular `list` or `dict` will **not** trigger this mechanism.

```python
book.tags.append("python")
assert book._p_changed is False  # Still not dirty
book._p_changed = True  # Manually mark dirty
```

To avoid manual intervention, use `PersistentList`, `PersistentMapping` or BTrees, which integrate automatic change tracking.

```python
from persistent.list import PersistentList

book.tags = PersistentList()
book.tags.append("python")  # Now ZODB marks it dirty automatically
```

When you inherit from `persistent.Persistent`, the base class overrides Python attributes access and modification mechanisms, especially `__setattr__`. This tracks the modification changes.

```python
class Person:
    def __init__(self, name):
        # Directly use object.__setattr__ to avoid __setattr__ recursion
        object.__setattr__(self, '_p_changed', False)
        object.__setattr__(self, 'name', name)

    def __setattr__(self, key, value):
        if getattr(self, key, None) != value:
            object.__setattr__(self, '_p_changed', True)
        object.__setattr__(self, key, value)


p = Person("Alice")
p.name = "Bob"          # __setattr__ detects a real change
print(p._p_changed)     # True
```

`object.__setattr__` is used to bypass your own `__setattr__` override. This prevents infinite recursion.

#### The Root Object and Object Graph

Every ZODB database maintains a **root object**, typically a dictionary or BTree. This acts as the top-level container for the applications persistent state.

```python
connection = db.open()
root = connection.root()
root['users'] = {}
```

Objects must be accessible from this root to be persisted; otherwise, they are unreachable and may be garbage-collected.

#### Storage Backend and Format

ZODB stores serialized objects in an append-only binary file named `data.fs`. Internally, ZODB uses a version of Pythons `pickle` protocol with optimizations for reference tracking and partial updates. Each object is stored with a unique object identifier (OID), and changes are written as transaction records.

#### Transaction and the `transaction` Module

ZODB provides full transactional integrity via the `transaction` module. **Changes to objects are not persisted until `transaction.commit()` is called**. Conversely, changes can be discarded using `transaction.abort()`.

```python
import transaction

root['users']['alice'] = Person("Alice", 30)
transaction.commit()
```

Transactions span all changes to persistent objects within a connection, ensuring atomicity and isolation.

`transaction` uses **thread-local state** to track an active transaction. When you change a ZODB `Persistent` object, (e.g. `obj.name = "Example"`), its ZODB connection automatically calls `transaction.get().join(self)` to register as a participant. So, when you call `transaction.commit()`, its commits **all participants**, including any and all ZODB connections you've used and dirtied in the current thread.

```python
import transaction

# This is global and thread-local
txn = transaction.get()
```

This object is a **global transaction manager** for your current thread. ZODB does **not require you to pass a reference to it**. Because, when you modify a persistent object the objects ZODB connection does,

```python
transaction.get().join(self._connection)
```

### Practical Use Cases

#### Application State Persistence

```python
from ZODB import FileStorage, DB
import transaction
import persistent

class Config(persistent.Persistent):
    def __init__(self, theme, window_size):
        self.theme = theme
        self.window_size = window_size

storage = FileStorage.FileStorage('app_state.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

root['config'] = Config(theme='dark', window_size=(1280, 720))
transaction.commit()

connection.close()
db.close()
```

#### Custom Domain Models

```python
from ZODB import FileStorage, DB
import transaction
import persistent
from persistent.list import PersistentList

class Project(persistent.Persistent):
    def __init__(self, name):
        self.name = name
        self.datasets = PersistentList()

storage = FileStorage.FileStorage('project.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

project = Project("Survey 1")
project.datasets.append("dataset_001.csv")
root['project'] = project
transaction.commit()

connection.close()
db.close()
```

#### Large Amount of Objects

For projects with a large number of objects, you will need to utilize a `uuid` for serialization as to uniquely identify an object.


`person.py`
```python
import uuid
from persistent import Persistent
from BTrees.OOBTree import OOBTree
from ZODB import DB
import ZODB.FileStorage
import transaction

class Person(Persistent):
    def __init__(self, _person_uuid, name):
        self.uuid = _person_uuid
        self.name = name

def main():
    storage = ZODB.FileStorage.FileStorage('person.fs')
    db = DB(storage)
    conn = db.open()
    try:
        root = conn.root()
        root['people'] = OOBTree()

        for i in range(100):
            person_uuid = str(uuid.uuid4())
            root['people'][person_uuid] = Person(person_uuid, f"Person_{i}")
        transaction.commit()
    finally:
        conn.close()
        db.close()

if __name__ == '__main__':
    main()
```

This execution will create,

```
person.fs        # ZODB data file (main database)
person.fs.index  # index for fast loading
person.fs.lock   # file lock. Contains PID of the last process that opened it. 
person.fs.tmp    # temporary file (may appear during operations)
```

Now, when the application starts up again we need to load these back using the created `person.fs` file. Keep in mind we need to at some stage import the class we're unpickling otherwise ZODB cannot create an instance of the object and cause issues.

`main.py`
```python
from ZODB import DB
import ZODB.FileStorage
from person import Person # Needs to be imported for unpickling

storage = ZODB.FileStorage.FileStorage('person.fs')
db = DB(storage)
conn = db.open()
root = conn.root()

for uuid, person in root['people'].items():
    print(f"{uuid}: {person.name}")

conn.close()
db.close()
```
