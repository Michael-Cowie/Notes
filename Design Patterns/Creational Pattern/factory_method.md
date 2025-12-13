<div align='center'>
    <h1> Factory Method </h1>
</div>

The Factory Method is a **pattern for creating objects** when you,

1. Know you need a **family of related objects**, but
2. Don't want the **client code** to know which concrete class is beung used.

Instead of having the client code do,

```python
if backend == "png":
    exporter = PngExporter()
elif backend == "svg":
    exporter = SvgExporter()
```

you **encapsulate the creation in a creator object**. Now, the client only interacts with the creator.

```python
creator = PngCreator()
creator.export(image, options)
```

The `if` still exists somewhere, such as choosing `PngCreator` or `SvgCreator`, but it is **moved outside the workflow**, leaving the algorithm itself branch-free.

## Motiviation

Consider exporting images. Different formats require,

- Different preprocessing (`prepare_data`)
- Different options (`dpi`, `page_size`, etc...)

Without the Factory Method,

- Workflow logic is mixed with creation and backend selection.
- Adding a new backend requires requires **modifying the workflow** - breaking the Open/Closed Principle.
- Client code must know internal details of every backend.

With the Factory Method,

- Workflow (`export`) is **stable**.
- Backend selection and preparation are **isolated** in a concrete creator.
- Adding a new format only requires a new creator and product class.

## Architecture

<div align='center'>
    <img src='./images/1.png'>
</div>

The pattern consists of,

1. A **Product** interface. The products define **the backend implementation**.
2. A **Creator** class that defines a factory method **and a workflow**.
3. **Concrete Creators** that override the factory method to produce specific products.

- **Client code** that selects the appropriate creator once, then invokes the workflow.

| Role                 | Responsibility                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Product**          | Interface for objects being created (`ImageExporter`, `Serializer`)                                                 |
| **Concrete Product** | Actual backend implementation (`PngExporter`, `JsonSerializer`)                                                     |
| **Creator**          | Declares a factory method (`create_exporter()`, `create_serializer()`) and a stable workflow (`export()`, `dump()`) |
| **Concrete Creator** | Overrides the factory method and optionally prepares backend-specific data or options (`PngCreator`, `JsonCreator`) |

You can identify the factory method by,

1. A base class has a `create_*()` method.
2. Subclasses override it to **instantiate different products**.
3. Workflow logic in the base class uses the product but **does not branch**.

## Example 1 - Different Serializer

Different serializers (JSON, XML, YAML) share a uniform interface, but the system chooses which one to use at runtime.

#### Products

```python
from abc import ABC, abstractmethod

import json

class Serializer(ABC):
    @abstractmethod
    def serialize(self, data):
        pass

class JsonSerializer(Serializer):
    def serialize(self, data):
        return json.dumps(data)

class YamlSerializer(Serializer):
    def serialize(self, data):
        return f"yaml: {data}"  # placeholder
```

#### Creators

```python
class SerializerCreator(ABC):
    @abstractmethod
    def create_serializer(self) -> Serializer:
        pass

    def dump(self, data):
        serializer = self.create_serializer()
        return serializer.serialize(data)

class JsonCreator(SerializerCreator):
    def create_serializer(self):
        return JsonSerializer()


class YamlCreator(SerializerCreator):
    def create_serializer(self):
        return YamlSerializer()
```

#### Client Code

```python
data = {"x": 10, "y": 20}

creator = JsonCreator()
print(creator.dump(data))

creator = YamlCreator()
print(creator.dump(data))
```

Will have the following workflow,

```
          Creator.dump()
                 |
                 v
     +------------------------+
     | create_serializer()    |
     +-----------+------------+
                 |
       -------------------
       |                 |
       v                 v
 JsonCreator       YamlCreator
       |                 |
       v                 v
 JsonSerializer   YamlSerializer
```

## Example 2 - Different Backend Exporter

We want a consistent **data-export workflow**, but **different backends** (Matplotlib, Qt) require preprocessing and produce different output formats.

#### Problem

The following code has multiple problems,

1. Data preparation logic is mixed with backend selection.
2. Hard to test, hard to extend.
3. Every new backend forces editing this function.
4. Violates SRP and Open/Closed principles.

```python
def export(raw_data, backend):
    if backend == "matplotlib":
        exporter = MatplotlibExporter()
        x, y = raw_data["x"], raw_data["y"]
        return exporter.export((x, y))

    elif backend == "qt":
        exporter = QtExporter()
        prep = {"points": list(zip(raw_data["x"], raw_data["y"]))}
        return exporter.export(prep)

    else:
        raise ValueError("Unknown exporter")
```

We can identify the following patterns,

1. They're all 'exporting' with a similar interface.
2. They all have data preparation steps.
3. Deciding which exporter to use is determined by the variable `backend`.

Hence,

- The **Product** is **exporting**.
- The **Creator** is **data preparation and using the exporter**.

Knowing this we want and need to,

1. Have the client code to **interface with the creator**.
2. Create a **Product** interface for exporting.
3. Create a **Creator** interface for **data preparation and exporting**.

#### Products

Create a product interface for exporting and implement exporting behaviour for **each backend**.

```python
from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, prepared_data):
        pass


class MatplotlibExporter(Exporter):
    def export(self, prepared_data):
        x, y = prepared_data
        print("Matplotlib plotting x,y…")


class QtExporter(Exporter):
    def export(self, prepared_data):
        # prepared_data is a dict with labels
        print(f"Qt drawing graph: {prepared_data}")
```

#### Creator

Creator handles **data normalization** and calls the exporter.

```python
class ExporterCreator(ABC):
    @abstractmethod
    def create_exporter(self) -> Exporter:
        pass

    @abstractmethod
    def prepare_data(self, raw):
        pass

    def export(self, raw):
        exporter = self.create_exporter()
        prepared = self.prepare_data(raw)
        return exporter.export(prepared)
```

#### Concrete Creator

```python
class MatplotlibCreator(ExporterCreator):
    def create_exporter(self):
        return MatplotlibExporter()

    def prepare_data(self, raw):
        return raw["x"], raw["y"]


class QtCreator(ExporterCreator):
    def create_exporter(self):
        return QtExporter()

    def prepare_data(self, raw):
        return {"points": list(zip(raw["x"], raw["y"]))}
```

#### Client Code

```python
raw = {"x": [1,2,3], "y": [10,20,30]}

creator = MatplotlibCreator()
creator.export(raw)

creator = QtCreator()
creator.export(raw)
```

## Example 3 - Image Exporter With Options

The Factory Method supports options **by pushing option interpretation into the concrete creator**, not the client and not the exporter interface. The client **should pass intent, not backend-specific options**. If the client has to know that PNG needs DPI but SVG doesn’t, the abstraction has already failed.

So,

- The client passes a generic options object.
- The concrete creator interprets what matters.
- The exporter receives only what it understands.

#### Product Interface - Stable

```python
class ImageExporter(ABC):
    @abstractmethod
    def export(self, image, options):
        pass
```

Here,

- `options` is deliberately opaque.
- The interface does not promise specific parameters.

#### Creator Owns Option Translation

```python
class ImageExportCreator(ABC, Generic[T]):
    @abstractmethod
    def create_exporter(self) -> ImageExporter[T]:
        pass

    @abstractmethod
    def prepare_options(self, raw_options: dict) -> T:
        pass

    def export(self, image, raw_options: dict):
        exporter = self.create_exporter()
        options = self.prepare_options(raw_options)
        exporter.export(image, options)
```

#### Concreate Creators Adapt Options

For each creator,

1. Accept the same raw option shape.
2. Extracts only what matters.
3. Silently ignores irrelevant fields.

```python
class PngCreator(ImageExportCreator[PngOptions]):
    def create_exporter(self) -> ImageExporter[PngOptions]:
        return PngExporter()

    def prepare_options(self, raw_options: dict) -> PngOptions:
        return PngOptions(
            dpi=raw_options.get("dpi", 300),
            transparent=raw_options.get("transparent", False)
        )

class SvgCreator(ImageExportCreator[SvgOptions]):
    def create_exporter(self) -> ImageExporter[SvgOptions]:
        return SvgExporter()

    def prepare_options(self, raw_options: dict) -> SvgOptions:
        return SvgOptions()  # nothing needed for SVG

class PdfCreator(ImageExportCreator[PdfOptions]):
    def create_exporter(self) -> ImageExporter[PdfOptions]:
        return PdfExporter()

    def prepare_options(self, raw_options: dict) -> PdfOptions:
        return PdfOptions(
            page_size=raw_options.get("page_size", "A4")
        )
```

Additionally, include the typehint for the provided options.

```python
class PngOptions(TypedDict, total=False):
    dpi: int
    transparent: bool

class SvgOptions(TypedDict, total=False):
    pass

class PdfOptions(TypedDict, total=False):
    page_size: str
```

#### Exporters Stay Simple

Exporters do not,

- Validate foreign options.
- Know about user intent.
- Perform format selection.

They only do format-specific work.

```python
class PngExporter(ImageExporter[PngOptions]):
    def export(self, image, options: PngOptions):
        print(f"PNG export with options: {options}, image={image}")

class SvgExporter(ImageExporter[SvgOptions]):
    def export(self, image, options: SvgOptions):
        print(f"SVG export with options: {options}, image={image}")

class PdfExporter(ImageExporter[PdfOptions]):
    def export(self, image, options: PdfOptions):
        print(f"PDF export with options: {options}, image={image}")
```

#### Client Code

The client code,

- Does not know which options are supported.
- Does not branch on option sets.
- Does not change when new formats are added.

```python
image = "my_image_data"
raw_options = {"dpi": 150, "transparent": True, "page_size": "Letter"}

png_creator = PngCreator()
png_creator.export(image, raw_options)

svg_creator = SvgCreator()
svg_creator.export(image, raw_options)

pdf_creator = PdfCreator()
pdf_creator.export(image, raw_options)
```
