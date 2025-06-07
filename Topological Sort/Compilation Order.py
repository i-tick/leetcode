# There are a total of n classes labeled with the English alphabet; i.e. A, B, C, and so on. Some classes are dependent
#  on other classes for compilation. Given a list of dependency pairs, find the order in which the classes should be 
# compiled.

from collections import deque, defaultdict

def find_compilation_order(dependencies):

  res = []
  graph = defaultdict(list)
  indeg = defaultdict(int)
  nodes = set()
  
  # Build the graph and calculate in-degrees
  for child, par in dependencies:
    graph[par].append(child)
    nodes.add(par)
    nodes.add(child)
    indeg[child] += 1
  
  # Initialize in-degrees for nodes with no incoming edges
  q = deque()
  for node in nodes:
    if indeg[node] == 0:
      q.append(node)

  # Perform topological sort using Kahn's algorithm
  # Process nodes with no incoming edges
  # and reduce in-degrees of their neighbors
  # If a neighbor's in-degree becomes zero, add it to the queue
  while q:
    node = q.popleft()
    res.append(node)
    for nei in graph[node]:
      indeg[nei] -= 1
      if indeg[nei] == 0:
        q.append(nei)
        
  # If we can process all nodes, we have a valid order
  
  # If not, return an empty list indicating a cycle
  # or that not all nodes can be processed
  if len(res) != len(graph):
    return []
  return res

# Time complexity: O(V + E)
# Space complexity: O(V + E)
  