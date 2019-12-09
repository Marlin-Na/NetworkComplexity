
## Network complexity metrics

The package implements the following metrics for graph complexity.

1. [First degree-based entropy](https://link.springer.com/article/10.1007/s12190-018-1168-x)
2. [N-th degree-based entropy](https://link.springer.com/article/10.1007/s12190-018-1168-x)
3. Topological information content
4. [Offdiagonal complexity](https://link.springer.com/chapter/10.1007/978-0-8176-4556-4_25)

## Example

```python
import networkcomplexity as nxc
import networkx as nx

# A simple graph
graph = nx.Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")

## Graph entropy based on vertex degree equivalence 
nxc.degree_entropy(graph)

## Graph entropy based on second degree equivalence
nxc.nth_degree_entropy(graph, 2)

## Topological information content
nxc.topological_info_content(graph)

## Offdiagonal complexity
nxc.offdiagonal(graph)
```