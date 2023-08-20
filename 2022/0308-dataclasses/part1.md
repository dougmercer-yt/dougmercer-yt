---
marp: true
theme: uncover
class: invert
---

# How dataclasses can jump-start your Python code!

Doug Mercer

---

### Python Data Model - Series

* Help you understand and use elements of the Python data model to make rich, Pythonic classes
* Example-driven exploration of features
* *Subscribe* to be notified of future videos in the series!

---

### In this video...


* Methods for initializing, representing, comparing, and hashing objects
* Use these methods to create a rich, Pythonic object
* Evaluate how `dataclasses` make this task easier

---

### Example: Content Management System

* Create a `BlogPost` object
* Display a nice representation of the blog post
* Make blogs sortable by title and content
* Use `__slots__` to save memory
* Make object hashable to store in a content addressable file system

---

### Lessons Learned

* Special methods such as `__repr__`, `__eq__`, and `__hash__` can help us create rich objects that work with Python's built-in functions and operators.
* The `__slots__` attribute helps us make more memory efficient objects at the expense of dynamically created attributes
* `dataclasses` make the job of implementing rich objects much easier

---

# Thanks for Watching!


---

# Python Data Model

Doug Mercer