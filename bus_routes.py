from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        # Create a map from bus stop to routes
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        # Initialize BFS
        queue = deque()
        visited_routes = set()
        visited_stops = set()

        # Start with all routes that include the source stop
        for route_index in stop_to_routes[source]:
            queue.append((route_index, 1))
            visited_routes.add(route_index)

        while queue:
            current_route, buses_taken = queue.popleft()

            # Check if the target is in the current route
            if target in routes[current_route]:
                return buses_taken

            # Explore all stops in the current route
            for stop in routes[current_route]:
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    # Explore all routes that include this stop
                    for next_route in stop_to_routes[stop]:
                        if next_route not in visited_routes:
                            visited_routes.add(next_route)
                            queue.append((next_route, buses_taken + 1))

        return -1
    
solution = Solution()
routes = [[1,2,7],[3,6,7]]
source = 1
target = 6
result = solution.numBusesToDestination(routes, source, target)
print(result)
