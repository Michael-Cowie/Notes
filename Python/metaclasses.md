<div align="Center">
    <h1> Metaclass </h1>
</div>

Metaclasses in Python are a powerful feature of the language that allows you to control the **creation and behaviour of classes**. They are often described as "classes of classes" - just like classes define how instances are created, **metaclasses define how classes themselves are created**.

In Python,

- **Objects are instances of classes**
- **Classes are instances of metaclasses**

By default, Python uses a built-in metaclass called `type`. This means when you created a class, Python actually does.

```python
MyClass = type("MyClass", (BaseClass,), attributes_dict)
```

So `type` is itself a metaclass.

<div align="Center">
    <h1> Why Use a Metaclass </h1>
</div>

Metaclasses are used when,

- You want to **automate class creation**, e.g. you want to inject attributes or methods.
- You want to **enforce class-level constraints**.
- You are building frameworks. For example, Django ORM uses metaclasses to define models.
- You want to **track classes**, like registering plugins.

<div align="Center">
    <h1> How to Create a Metaclass </h1>
</div>

A metaclass is a subclass of `type`. In the following example, `MyClass` will have the attribute `added_attr` added to it, caused by the metaclass adding it during the creation of the class. This attribute is **at the class level**.

```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_attr'] = 'I was added by metaclass'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

print(MyClass.added_attr)  # I was added by metaclass
```

The relationship between Class, Object and Type must be understood. Here we demonstrate `f`, that is an instance of `Foo` and additionally checking the type when using it directly on the class `Foo`.

```python
class Foo:
    pass

f = Foo()

print(type(f))      # <class '__main__.Foo'>
print(type(Foo))    # <class 'type'>  <-- Foo is instance of type
```

<div align="Center">
    <h1> Metaclass Lifecycle </h1>
</div>

The three important methods to focus on during creation is `__new__`, `__init__` and `__call__`. 

The `__new__` method is added onto the metaclass declared as `__new__(cls, name, bases, dct)`. This is called **before the class is created**. Use this to **modify the class dictionary**. The `__new__` method is what **actually creates the class object**.  Here,

```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Do stuff (like modifying dct)
        return super().__new__(cls, name, bases, dct)
```

- `cls` - **The metaclass**. A subclass of `type`.
- `name` - Name of the class being defined.
- `bases` - Tuple of the parent class. This is used for inheritance, can be empty.
- `dct` - Dictionary of class attributes and methods.

The `__init__` is called **after the class is created**. `__init__` gets the newly created application-level *class**, `Foo`. By that time, the classes namespace has been populated the attribute `added_attr` has been added to the class object. here,

```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct["added_attr"] = "Added attribute"
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(getattr(cls, "added_attr"))
        super().__init__(name, bases, dct)

class Foo(metaclass=MyMeta):
    pass
```

- `cls` - **The class object**.
- `name` - Name of the class object.
- `bases` - Tuple of the parent class. This is used for inheritance, can be empty.
- `dct` - Dictionary of class attributes and methods.

Finally we have `__call__`, this is called when calling an instance of the class. A usecase of this could be to implement a Singleton pattern. Here, any call to a class inheriting from `MyMeta` will only ever return a single instance.

In a metaclass, `super().__call__()` returns an instance of the class being instantiated because you're invoking the base metaclass’s `__call__` method, which is responsible for creating and initializing instances — just like a constructor.

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Foo(metaclass=SingletonMeta):
    pass

foo = Foo()
foo2 = Foo()
print(foo is foo2) # True
```

<div align="Center">
    <h1> Practical Use </h1>
</div>

#### Validating Class Definitions

```python
class ValidateMeta(type):
    def __new__(cls, name, bases, dct):
        if 'required_attr' not in dct:
            raise TypeError(f"{name} must define 'required_attr'")
        return super().__new__(cls, name, bases, dct)
```

#### Automatic Registration

```python
registry = {}

class AutoRegisterMeta(type):
    def __init__(cls, name, bases, dct):
        registry[name] = cls
        super().__init__(name, bases, dct)
```

I will give a practical example of the adaption pattern using metaclasses. This means, it will produce an object of one type given one object type. Here, I will create a Tree Factory. In the context of a GUI application, the Tree will be a class that interfaces with an application object. The Tree object will contain information responsible for how it is displayed in the user interface. The adapation will map the application object which contains information of the context of the application into a Tree object which holds information for displaying it in the tree.

Below is a file called `tree.py`. Here, the metaclass `RegisterTreeMetaClass` is responsible for populating the dictionary `treeAdapters` where the key will be the class name of any class inheriting from the metaclass and sets the value to the class. This dictionary mapping is designed to map anything inheriting from `AppObject` to its associated `TreeObject`. This mapping only works if the classes have identical names.

`tree.py`

```python
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app_object import AppObject

treeAdapters: dict[str, type(TreeObject)] = {}

class RegisterTreeMetaClass(type):

    def __new__(cls, name, bases, dct):
        cls = super().__new__(cls, name, bases, dct)
        treeAdapters[cls.__name__] = cls
        return cls

class TreeObject(metaclass=RegisterTreeMetaClass):
    def __init__(
        self,
        app_object,
        adapter_factory,
    ):
        self._app_object = app_object
        self._adapter_factory = adapter_factory

    @property
    def object_type(self):
        return "An instance of TreeObject"

class MyExample(TreeObject):
    pass

class TreeAdapterFactory:

    def adapt(self, app_object: AppObject) -> TreeObject:
        adapter_class = treeAdapters.get(type(app_object).__name__)
        return adapter_class(app_object, self)
```

In the following example we define the `AppObject` class. Here, we create an instance of `TreeAdapterFactory` which allows us acccess to the previously populated dictionary using the metaclass. Given that we defined our `Example` class that is inheriting from `AppObject` with the same name as the associated `Example` inheriting from `TreeObject`, when we call `adapt`, the `__name__` of our `AppObject` will match the key that previously populated the dictionary, allowing us to find the associated `TreeObject`. Therefore, `adapt` will return an instance of `MyExample` that inherits from `TreeObject` which is created by passing the instance of the `AppObject` and the factory when creating the `TreeObject`.

`app_object.py`

```python
from tree import TreeAdapterFactory

class AppObject:

    @property
    def object_type(self):
        return "An instance of AppObject"

class MyExample(AppObject):
    pass

app_object = MyExample()

tree_adapter_factory = TreeAdapterFactory()
tree_object = tree_adapter_factory.adapt(app_object)

print(app_object.object_type)  # An instance of AppObject
print(tree_object.object_type) # An instance of TreeObject
```

#### Singleton Pattern

The singleton pattern is a little different where instead of `__new__` and `__init__`, it will use `__call__`. The general format of a Singleton appears as,

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
```

A more complete example will be,

```python
class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"[Logger] {message}")

    def get_logs(self):
        return self.logs

# First __call__ call will create the instance
logger1 = Logger()
logger1.log("System started")

# Second __call__ will fetch the instance
logger2 = Logger()
logger2.log("User logged in")

print(f"logger1 is logger2: {logger1 is logger2}")
```

This will output the following,

```
[Logger] System started
[Logger] User logged in
logger1 is logger2: True
```

#### ORM Style Classes

In Django, metaclasses can map class attributes to database columns.