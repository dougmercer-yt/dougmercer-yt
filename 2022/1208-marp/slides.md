---
marp: true
theme: uncover
class: invert
math: mathjax
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

# <!--fit-->An Intro to Marp :rocket:

<span style="color:gray">By:</span> Doug Mercer

---

## Slide Header

* Use Markdown to write slides!
* Tons of cool features!

---

## Code!

```python
def add(a, b):
    """A super useful function."""
    return a + b
```

---

## Math!

A single line expression...

$\mathcal{O}(n\log{n})$

OR, a multiline expression...

$$
\begin{align}
x &= 1 + \frac{1}{2} \\
  &= 1.5
\end{align}
$$

---

# Images

![height:5in](logo.jpg)

---

![bg hue-rotate:90deg saturate](logo.jpg)
Marp has a variety of image modifiers.

---

![bg blur](logo.jpg)
![bg greyscale blur](logo.jpg)
![bg sepia blur](logo.jpg)

You can stack backgrounds horizontally...

---

![bg vertical blur](logo.jpg)
![bg greyscale blur](logo.jpg)
![bg sepia blur](logo.jpg)

... or vertically!

---

# Two columns?

![height:4in](logo.jpg)

* a
* b

---

## Two columns!

![bg left height:4in](logo.jpg)

* a
* b

---
<!--_color: red-->
<!--_backgroundColor: black-->

# <!--fit-->Huge
---

# Multi columns in Marp!

<div class="columns">
<div>

## Column 1
* a
* b
* c

</div>
<div>

## Column 2

* d
* e
* f

</div>
</div>
