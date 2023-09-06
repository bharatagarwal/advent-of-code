Given

```python
coordinate = [0, 0]
houses = set(tuple(coordinate))
```

This is the wrong syntax. set() is expecting an iterator.
the right syntax would be

```python
houses = {tuple(coordinate)}
```
