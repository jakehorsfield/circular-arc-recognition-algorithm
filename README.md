# How to use

**Warning:**
This program is a very basic brute-force algorithm:
it just checks all possible permutations of the vertex set.
There are polynomial-time algorithms that determine
whether an input graph is circular-arc, but I think it would be a
nontrivial project to implement them.

- Create a list of vertices, e.g.:
```python
V = [1,2,3,4,5]
```

- Create a list of edges, e.g.:
```python
E = [[1,2],[2,3],[3,4],[4,5],[5,1]]
```

Note that the algorithm takes the symmetric closure of E,
so the order of the vertices in an edge does not matter,
e.g. [1,2] and [2,1] are considered to be equivalent.

- Call the is_ca function:
```python
is_ca(V,E)
```

- Run the program:
```
python recognition.py
```

- With this example we receive the following output:
```
======
V = [1, 2, 3, 4, 5]
E = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]
The graph is circular-arc.
Tucker ordering: (1, 2, 3, 4, 5)
======
```

A `Tucker ordering` refers to a circular ordering 
v_1, ..., v_n of the vertex-set of a graph such that
for all 1 <= i < j <= n, if v_iv_j is an edge, then
either 
- v_i is adjacent to each of v_{i+1}, ..., v_j
or
- v_j is adjacent to each of v_{j+1},...,v_n,v_1,...,v_i
