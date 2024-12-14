import heapq

class PathfindingRobot:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def is_valid(self, position):
        x, y = position
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] != 1

    def find_path(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        open_list = []
        heapq.heappush(open_list, (0, self.start))
        came_from = {}
        cost = {self.start: 0}

        while open_list:
            current_cost, current = heapq.heappop(open_list)

            if current == self.goal:
                # Reconstruct path
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for dx, dy in directions:
                neighbor = (current[0] + dx, current[1] + dy)
                if self.is_valid(neighbor):
                    new_cost = cost[current] + 1  # Uniform cost for simplicity
                    if neighbor not in cost or new_cost < cost[neighbor]:
                        cost[neighbor] = new_cost
                        priority = new_cost
                        heapq.heappush(open_list, (priority, neighbor))
                        came_from[neighbor] = current
        return None


# Example grid: 0 = free, 1 = obstacle
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

start = (0, 0)
goal = (3, 3)

robot = PathfindingRobot(grid, start, goal)
path = robot.find_path()
print("Path:", path)
