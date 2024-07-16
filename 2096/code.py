class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = collections.defaultdict(list)

        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                graph[node.left.val].append((node.val, 'U'))
                graph[node.val].append((node.left.val, 'L'))

                queue.append(node.left)

            if node.right:
                graph[node.right.val].append((node.val, 'U'))
                graph[node.val].append((node.right.val, 'R'))

                queue.append(node.right)

        queue = collections.deque([(startValue, "")])
        seen = set()

        while queue:
            curr_val, curr_path = queue.popleft()

            if curr_val in seen:
                continue

            seen.add(curr_val)

            if curr_val == destValue:
                return curr_path

            else:
                for child, direction in graph[curr_val]:
                    if child not in seen:
                        queue.append((child, curr_path + direction)) 
