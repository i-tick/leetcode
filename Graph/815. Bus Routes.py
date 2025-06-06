# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Example 2:

# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1

from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # Create a mapping from bus stop to the list of buses that go through that stop
        stop_to_buses = defaultdict(list)
        for bus_index, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_index)

        # BFS initialization
        queue = deque([source])
        visited_stops = {source}
        visited_buses = set()
        buses_taken = 0

        while queue:
            for _ in range(len(queue)):
                current_stop = queue.popleft()

                # Check if we reached the target
                if current_stop == target:
                    return buses_taken

                # Explore all buses that go through the current stop
                for bus_index in stop_to_buses[current_stop]:
                    if bus_index in visited_buses:
                        continue
                    
                    visited_buses.add(bus_index)
                    for next_stop in routes[bus_index]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append(next_stop)
            buses_taken += 1 # level+=1 
        return -1
# Time Complexity: O(N + E) where N is the number of bus stops and E is the total number of bus routes.
# Space Complexity: O(N + E) for the adjacency list representation of the bus stops and routes.
# Note: The function uses a breadth-first search (BFS) approach to find the minimum number of buses required to travel from the source bus stop to the target bus stop.
# It constructs a mapping of bus stops to the buses that serve them, then explores the bus stops level by level, counting the number of buses taken until it reaches the target.
# If the target is reached, it returns the number of buses taken; otherwise, it returns -1 if the target cannot be reached.