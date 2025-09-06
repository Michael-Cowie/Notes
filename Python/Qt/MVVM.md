<div align='center'>
    <h1> MVVM </h1>
</div>

Qt ships a mature View/Model framework whose "model" objects (`QAbstractItemModel` and its derivatives) are view-facing adapters. They expose tabular or hierarchical data via indexes, roles and change-notification signals. MVVM (Model-View-ViewModel) is a higher-level application.

- The **Model** is a framework-agnostic domain data.
- The **View** renders.
- The **ViewModel** adapts domain data to the View and exposes commands and derived state.

When we apply MVVM to PyQt6, we keep the domain model in plain Python and let a ViewModel **own a Qt item model**. The Qt item model is still called a "model" by Qt,, but functionally it belongs to MVVM's ViewModel layer.

#### The Model - Authority on Data

The **Model** is where your applications data lives. It defines what data exists, how it is structured and what operations are allowed. **The Model provides a standard framework for queries to and edits for your data**.

- Provides **rows and column counts** so views know the structure.
- Supplies **data for each index** via the `data()` method, often differentiated by role (`DisplayRole`, `DecoratedRole`, `EditRole`).
- Accepts changes through `setData()` and notifies observers by emitting `dataChanged`.
- Declares **editability rules** through the `flags()` method.
- Holds reference to the data source (`Person` objects).

A `PeopleModel` might **wrap a list** of `Person` objects. Each row is one person and the two columns represent `Name` and `Age`.

- `rowCount` returns the number of people.
- `data(index, DisplayRole)` returns either the name or age depending on the column.
- `setData()` updates the `Person` object and emites `dataChanged` so the view repaints that cell.

Think of the Model as a **database table adapter**, it doesn't draw anything, it just knows how to answer questions like "What's in row 2, column 1?".

The MVVM pattern was designed in the .NET/WPF world, where the Model usually refers to the domain to business data itself. In Qt, however the word Model already has a very specific meaning, a class derived from `QAbstractItemModel` that acts an **adapter between raw data and views**. The dual use of the term Model can create confusion.

MVVM in Qt Reality

- **Data Source** - Your actual data is stored in a list/tree somewhere. The actual domain objects (`Person`, `Order`, `Document`) or database.
- **Qt Model** - A subclass of `QAbstractItemModel` that adapts the data source into row/columns/roles so Qt Views can render it.
- **View** - A `QTableView`, `QTreeView` etc. that knows how to paint data from a Qt Model.
- **ViewModel** - A QObject-based class that adds semantic signals and commands, making binding to ordinary widgets `QLabel`, `QLineEdit` simpler.

#### The View - Window into the Model

The **View** is how the users sees and interacts with the Models data. Views in Qt include `QTableView`, `QTreeView` and `QListView`. **The View provides a means to visually observe and interact with your data**.

- Renders the data it receives from the Model.
- Subscribes automatically to model signals (`dataChanged`, `rowsInserted`) so it stays in sync.
- Allows inline editing by creating editor widgets and writing back changes with `setData()`.
- Provides the `selectionModel()` interface to expose what the user has selected.

A `QTableView` showing the `PeopleModel` automatically paint two columns - `Name` and `Age`. When a user double-clicks a cellthe table asks the Model if its editable (via `flags`). If yes, it shows a text editor, lets the user type and then calls `setData()` on the Model.

The view is the window, it shows what's in the Model and lets the user interact with it, but it doesn't own the data.

#### The ViewModel - Bridge of Meaning

The **ViewModel** is not part of Qt's core framework, but a design pattern many developers adopt to add clarity. While the Model speaks in terms of indexes and roles, the ViewModel speakers in terms of **domain semantics**.

- Holds a reference to the Model but exposes clean, domain-specific signals.
- Provides **commands** as slots (`apply_name`, `bump_age`) instead of requiring the View to call `setData()` directly.

So the View hooks it up,

```python
self.age_inc_btn.clicked.connect(self.vm.bump_age)
```

Once the button is clicked it calls `bump_age` on the ViewModel,

```python
@pyqtSlot()
def bump_age(self):
    if self._row < 0:
        return
    self.model.bump_age(self._row)
    self._emit_state()
```

When finally makes the call on the Model,

```python
def bump_age(self, row: int):
    if 0 <= row < len(self._people):
        self._people[row].age += 1
        idx = self.index(row, self.AGE)
        """
        dataChanged is a predefined signal of `QAbstractItemModel`. Its purpose is purely structural and technical
        to notify any attached views (Such as QTableView, QTreeView, or proxy models) that the data at certain
        indexes has changed.

        You don't connect to dataChanged. Qt's infrastructure views and helpers already listen to it behind the
        scenes.

        table = QTableView()
        table.setModel(my_model)

        The QTableView automatically connects to the models signals, including,

        - dataChanged - Triggers the view to repaint the affected cells.
        - rowsInserted/rowsRemoved - Updates the row count and redraws the table.
        - layoutChanged/modelReset - Causes a full layout recalculation.

        When you emit,

            self.dataChanged.emit(index, index, [Qt.ItemDataRole.DisplayRole])

        The QTableView says "oh, cell (row, col) needs repainting" and it fetches the new value from model.data(...)
        """
        self.dataChanged.emit(idx, idx, [Qt.ItemDataRole.DisplayRole])
```

- Translates selection (row indexes) into meaningful state ("current person is Alice").
- Emits semantic signals like `nameChanged(str)` or `statusChanged(str)` for the View to consume.

In a `PeopleViewModel`, selecting row 1 (Bob) might trigger,

- Updating its internal `_current_row`.
- Emitting `nameChanged("Bob")` so a `QLineEdit` updates.
- Emitting `statusChanged("Selected Bob, age 30")` so a status label updates.

The ViewModel is the interpreter, it listens to the low-level technical language of Qt and translates it into human-meaningful events that the UI can bind to.

#### The SelectionModel - State of Choice

Selection is so central in user interfaces that Qt dedicates a whole class, `QItemSelectionModel`, to track it. It sits between the Model and the View.

- Tracks which indexes are selected.
- Tracks the "current" item. The one with keyboard focus.
- Emits signals such as `selectionChanged` and `currentChanged`.
- Can be shared across multiple Views so they synchronize their selection state.

If the user clicks on "Bob" in the table, the `QItemSelectionModel` emites `selectionChanged`.

- A `QLabel` bound to this event might update to say "Selected: Bob, 30.".
- If a second view (`QListView`) shares the same selection model, it will also highlight Bob automatically.

The SelectionModel is the highlighter pen, it doesn't own the book (the data) or the page (the view), it just says "This is what's currently highlighted".

#### Qt's View/Model

Qt's View/Model architecture separates the presentation widgets from a data source interface. A View (`QTreeView`, `QListView`, `QTableView`) never touches your data structures directly, it only talks to a Model implementing `QAbstractItemModel`. The model supplies,

- **Shape** - Using `rowCount`, `columnCount`, `index` and `parent` for trees.
- **Data** - Data is keyed by roles such as `DisplayRole`, `DecorationRole` and custom roles.
- **Mutations** - Mutations are performed using `setData`, `insertRows`, `removesRows`, etc...
- **Notifications** - Notification are performed using `dataChanged`, `rowsInserted`, etc... which are usually wrapped in `begin*/end*` guards.

Painting/editing of individual cells is delegated to delegates (`QStyledItemDelegate`), which the View invokes. This design predates MVVM and uses the "Model" to mean the Views data interface, and not your business layer.

```C++
#include <QApplication>
#include <QTreeView>
#include <QStandardItemModel>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    QStandardItemModel model;
    model.setHorizontalHeaderLabels({ "Name" });

    auto *root = model.invisibleRootItem();

    auto *docs = new QStandardItem("Documents");
    docs->appendRow(new QStandardItem("Resume.docx"));
    docs->appendRow(new QStandardItem("Report.pdf"));

    auto *pics = new QStandardItem("Pictures");
    pics->appendRow(new QStandardItem("Holiday.png"));
    pics->appendRow(new QStandardItem("Family.jpg"));

    root->appendRow(docs);
    root->appendRow(pics);

    QTreeView view;
    view.setModel(&model);
    view.expandAll();
    view.resize(400, 300);
    view.setWindowTitle("Qt View/Model (C++)");
    view.show();

    return app.exec();
}
```

Here, the data folder and files are created directly as `QStandardItem`. This is idiomatic Qt View/Model, quick to build, tightly couples your apps data to Qt classes and not readily testable without Qt.

#### Recreation as MVVM in PyQt6

MVVM asks that the **Model** be "pure" domain data, independent of the UI toolkit. The **ViewModel** adapts that domain to the View and surfaces commands. The **View** is passive. In PyQt6, the View still needs a `QAbstractItemModel`. Therefore, the ViewModel **owns** a Qt item model and fills it from the domain. The domain remains a testable plain Python.

#### Model - Domain Model

```Python
class FileNode:
    """A domain node for folders/files. No Qt dependencies."""
    def __init__(self, name: str, children=None):
        self.name = name
        self.children = children or []
```

This class models the business reality. It is a tree of folders **without any Qt imports**. You can load/save it from JSON, a database or a service and unit-test it without a GUI.

#### ViewModel

The ViewModel is a `QObject` that **owns a** `QStandardItemModel` or custom subclass or `QAbstractItemModel`. It is responsible for translating `FileNode → QStandardItem`. It can also expose commands (slots) such as add/rename/remove and derived state (e.g. counts) via properties and signals, keeping View declarative.

```python
import sys
from PyQt6.QtCore import QObject, Qt
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QApplication, QTreeView, QVBoxLayout, QWidget

UserRole_Node = Qt.ItemDataRole.UserRole + 1  # store domain node on each item

class FileNode:
    def __init__(self, name: str, children=None):
        self.name = name
        self.children = children or []

class TreeViewModel(QObject):
    """Owns the Qt item model and adapts FileNode → QStandardItemModel."""
    def __init__(self, root: FileNode):
        super().__init__()
        self._root = root
        self._model = QStandardItemModel()
        self._model.setHorizontalHeaderLabels(["Name"])
        self._populate(self._model.invisibleRootItem(), root)

    def _populate(self, parent_item: QStandardItem, node: FileNode):
        item = QStandardItem(node.name)
        item.setEditable(False)
        item.setData(node, UserRole_Node)          # keep a back-reference to the domain
        parent_item.appendRow(item)
        for child in node.children:
            self._populate(item, child)

    def get_model(self) -> QStandardItemModel:
        return self._model                         # emits dataChanged

class TreeViewWidget(QWidget):
    """The View; binds to the ViewModel’s model and forwards user actions."""
    def __init__(self, view_model: TreeViewModel):
        super().__init__()
        self.setWindowTitle("PyQt6 MVVM — Folder Tree")
        self.tree = QTreeView()
        self.tree.setModel(view_model.get_model())
        self.tree.expandAll()

        layout = QVBoxLayout(self)
        layout.addWidget(self.tree)

if __name__ == "__main__":
    file_root = FileNode("Root", [
        FileNode("Documents", [FileNode("Resume.docx"), FileNode("Report.pdf")]),
        FileNode("Pictures",  [FileNode("Holiday.png"), FileNode("Family.jpg")]),
    ])
    app  = QApplication(sys.argv)

    view = TreeViewWidget(TreeViewModel(file_root))
    view.resize(420, 320)
    view.show()

    sys.exit(app.exec())
```

The **domain** tree is authoritative. Each `QStandardItem` holds a pointer to its `FileNode` in a custom role so commands can modify the domain and then reflect changes in the View. The **View** binds to `vm.get_model()` and **emits no business logic**. The **ViewModel** exposes commands such as `addChild`, `rename` and `removes` as slots, which is Qt idiom for MVVM "actions".

#### Why Qt's Model Is Inside MVVM ViewModel

The "Model" in Qt is defined by the needs of the **View**. It is an interface with indexes and roles plus mutation signals. The "Model" in MVVM is defined by the business. It is application state and rules, **without toolkit types**. Those are different axes. In an MVVM PyQt6 app, the Qt item model belongs to the ViewModel because it is the binding surface that the View consumes. It adapts domain objects to rows, columns and roles. It additionally emits notifications to refresh the View. The domain classes remain independent and testable.

This separation has pragmatic benefits. The domain can be unit-tested without Qt. The View can be replaced (Widgets ↔ QML) without rewriting the domain. The ViewModel can impose shape, filtering, sorting and validation without polluting the View or the domain.

#### Design Choices and Their Consequences

##### `QStandardItemModel` vs custom `QAbstractItemModel`

`QStandardItemModel` is convenient and fine for small to medium trees. You can store domain pointers in a user role, as above. For very large trees, lazy loading or strict one-to-one mapping, a custom subclass of `QAbstractItemModel` is superioer. You can implement `index`, `parent`, `rowCount`, `columnCount` and `data` using each `QModelIndex`'s `internalPointer` to reference the exact `FileNode`. In both approaches, the **ViewModel is where this model is created and managed**.

#### Two-way Updates

From **domain → view**, call the proper begin/end wrappers (or use `QStandardItem` helpers) and emit `dataChanged` when values mutate. From **domain → domain**, route user intent as ViewModel slots, validate, update the domain, then update the Qt model. This is Qt's analogue to "two-way-binding.

```python
from dataclasses import dataclass
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex, QObject, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QApplication, QWidget, QTableView, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
import sys

UserRole_Object = Qt.ItemDataRole.UserRole + 1

@dataclass
class Person:
    name: str
    age: int

class PeopleModel(QAbstractTableModel):
    """Model - Remains the authority on data, roles, and editability."""
    NUMBER_OF_COLUMNS = 2
    NAME, AGE = range(NUMBER_OF_COLUMNS)

    def __init__(self, people: list[Person]):
        super().__init__()
        self._people = people

    def rowCount(self, parent=QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self._people)

    def columnCount(self, parent=QModelIndex()) -> int:
        return 0 if parent.isValid() else self.NUMBER_OF_COLUMNS

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        """ Given a QModelIndex, retrieves the People object to represent the data on the cell for the role."""
        if not index.isValid():
            return None
        p = self._people[index.row()]
        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            return p.name if index.column() == self.NAME else p.age
        if role == UserRole_Object:
            return p
        return None

    def setData(self, index: QModelIndex, value, role=Qt.ItemDataRole.EditRole) -> bool:
        """
        Given a QModelIndex, use this information to get the Model data (People object) and update it from
        the notified edited data from the View.
        """
        if not index.isValid() or role != Qt.ItemDataRole.EditRole:
            return False
        p = self._people[index.row()]
        if index.column() == self.NAME:
            nv = str(value)
            if nv == p.name:
                return False
            p.name = nv
        else:
            try:
                v = int(value)
            except (TypeError, ValueError):
                return False
            if v == p.age:
                return False
            p.age = v
        self.dataChanged.emit(index, index, [role, Qt.ItemDataRole.DisplayRole])
        return True

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        """
        - Horizontal orientation is column header. Here it is "Name" and "Age".
        - Vertical orientation is the row number. Here it is a row number, 1, 2, 3...
        """
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        elif orientation == Qt.Orientation.Horizontal:
            return ["Name", "Age"][section]
        elif orientation == Qt.Orientation.Vertical:
            return section + 1

    def flags(self, index: QModelIndex):
        """
        Every `QModelIndex` in a Qt model has flags (a bitmask of `Qt.ItemFlag` values). These flags tell the view
        if an item is,

        - Enabled (Can be interacted with at all)
        - Selectable
        - Editable
        - ...

        If you don't override `flags`, Qt assumes only enabled + selectable. For a valid cell, combine these flags
        with bitwise OR `|`,

        - ItemIsEnabled - The cell can be interacted with.
        - ItemIsSelectable - The cell can be selected (Highlighted).
        - ItemIsEditable - The cell can be edited by the user (e.g. double-click and type).

        In Qt, the view should not know or decide about the data, only how to present it. The model is the authority on,

        - What data exists.
        - How it can be accessed.
        - What operations are allowed (editable, checkable, drag-drop etc...)

        The views job is only to ask the model and render accordingly. Editability lives in the model because
        editability is a property of the data, not of the widget showing it.
        """
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        return (
            Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsSelectable
            | Qt.ItemFlag.ItemIsEditable
        )

    def bump_age(self, row: int):
        if 0 <= row < len(self._people):
            self._people[row].age += 1
            idx = self.index(row, self.AGE)

            """
            dataChanged is a predefined signal of `QAbstractItemModel`. Its purpose is purely structural and technical
            to notify any attached views (Such as QTableView, QTreeView, or proxy models) that the data at certain
            indexes has changed.

            You don't connect to dataChanged. Qt's infrastructure views and helpers already listen to it behind the
            scenes.

            table = QTableView()
            table.setModel(my_model)

            The QTableView automatically connects to the models signals, including,

            - dataChanged - Triggers the view to repaint the affected cells.
            - rowsInserted/rowsRemoved - Updates the row count and redraws the table.
            - layoutChanged/modelReset - Causes a full layout recalculation.

            When you emit,

                self.dataChanged.emit(index, index, [Qt.ItemDataRole.DisplayRole])

            The QTableView says "oh, cell (row, col) needs repainting" and it fetches the new value from model.data(...)
            """
            self.dataChanged.emit(idx, idx, [Qt.ItemDataRole.DisplayRole])

class PeopleVM(QObject):
    """
    ViewModel exposing commands and state. The ViewModel owns state and commands, never touches widgets.
    It orchestrates edits via the Model. Holds a reference to the model, not to any widgets.
    """
    nameChanged = pyqtSignal(str)
    statusChanged = pyqtSignal(str)

    def __init__(self, model: PeopleModel):
        super().__init__()
        self.model = model
        self._row = -1

    def _emit_state(self):
        if self._row < 0:
            self.nameChanged.emit("")
            self.statusChanged.emit("—")
            return

        p = self.model.data(self.model.index(self._row, 0), UserRole_Object)
        self.nameChanged.emit(p.name)
        self.statusChanged.emit(f"Selected: {p.name}, age {p.age}")

    @pyqtSlot(int)
    def set_current_row(self, row: int):
        self._row = row
        self._emit_state()

    @pyqtSlot(str)
    def apply_name(self, name: str):
        if self._row < 0:
            return
        idx = self.model.index(self._row, PeopleModel.NAME)
        if self.model.setData(idx, name, Qt.ItemDataRole.EditRole):
            self._emit_state()

    @pyqtSlot()
    def bump_age(self):
        if self._row < 0:
            return
        self.model.bump_age(self._row)
        self._emit_state()

class PeopleView(QWidget):
    """
    View builds the UI and binds to the ViewModel. View owns all widget/layout creation and purely binds UI events to
    ViewModel slots and listens to ViewModel signals to update widgets. No business logic; delegates to VM via signals/slots.
    """
    def __init__(self, vm: PeopleVM):
        super().__init__()
        self.vm = vm
        self.table = QTableView()
        self.table.setModel(vm.model)
        self.table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        self.name_edit = QLineEdit()
        self.apply_name_btn = QPushButton("Apply Name")
        self.age_inc_btn = QPushButton("Increase Age")
        self.status = QLabel("—")

        form = QHBoxLayout()
        form.addWidget(QLabel("Name:"))
        form.addWidget(self.name_edit)
        form.addWidget(self.apply_name_btn)
        form.addWidget(self.age_inc_btn)

        root = QVBoxLayout(self)
        root.addWidget(self.table)
        root.addLayout(form)
        root.addWidget(self.status)

        self.table.selectionModel().selectionChanged.connect(self._on_selection_changed)
        self.apply_name_btn.clicked.connect(lambda: self.vm.apply_name(self.name_edit.text()))
        self.age_inc_btn.clicked.connect(self.vm.bump_age)
        self.vm.nameChanged.connect(self.name_edit.setText)
        self.vm.statusChanged.connect(self.status.setText)

        if self.vm.model.rowCount() > 0:
            self.table.selectRow(0)
            self._on_selection_changed()

    @pyqtSlot()
    def _on_selection_changed(self, *args):
        idxs = self.table.selectionModel().selectedRows()
        row = idxs[0].row() if idxs else -1
        self.vm.set_current_row(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = PeopleView(PeopleVM(PeopleModel([Person("Alice", 25), Person("Bob", 30), Person("Charlie", 35)])))
    w.setWindowTitle("MVVM: Domain ⇄ Model ⇄ ViewModel ⇄ View")
    w.resize(640, 360)
    w.show()

    sys.exit(app.exec())
```

#### Selection and Navigation

The View owns a `QItemSelectionModel`. If you need the ViewModel to react to selection, connect the Views `selectionModel().selectChanged` to a ViewModel slot. Because the Qt model stores a domain pointer for each item, the ViewModel can translate a selected `QModelIndex` back into a `FileNode` reliably.

#### Filtering and Composition

`QSortFilterProxyModel` and similar are natural "sub-ViewModels". Place them inside the ViewModel layer, upstream of the View and expose the proxy to the View. In MVVM terms, a proxy is a view-facing adapter that reshapes the same domain into a different presentation.

#### Editing and Validation

Expose edits as ViewModel commands. If you enable in-place editing, your models `flags` must include `ItemIsEditable` and `setData` should validate and synchronize the domain before emitting `dataChanged`. Centralizing validation in the ViewModel keeps the View dumb and the domain honest.
