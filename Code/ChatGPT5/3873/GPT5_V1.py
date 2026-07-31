from collections import defaultdict, deque

class Solution(object):
    def maxActivated(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        # Build bipartite graph:
        # x-value node <-> point <-> y-value node
        x_id = {}
        y_id = {}

        xcnt = 0
        ycnt = 0

        for x, y in points:
            if x not in x_id:
                x_id[x] = xcnt
                xcnt += 1
            if y not in y_id:
                y_id[y] = ycnt
                ycnt += 1

        x_adj = [[] for _ in range(xcnt)]
        y_adj = [[] for _ in range(ycnt)]

        point_x = [0] * n
        point_y = [0] * n

        for i, (x, y) in enumerate(points):
            xi = x_id[x]
            yi = y_id[y]
            point_x[i] = xi
            point_y[i] = yi
            x_adj[xi].append(i)
            y_adj[yi].append(i)

        comp = [-1] * n
        comp_size = []
        x_comp = [-1] * xcnt
        y_comp = [-1] * ycnt

        cid = 0

        # Find connected components
        for i in range(n):
            if comp[i] != -1:
                continue

            q = deque([i])
            comp[i] = cid
            size = 0

            while q:
                p = q.popleft()
                size += 1

                xi = point_x[p]
                if x_comp[xi] == -1:
                    x_comp[xi] = cid
                    for nxt in x_adj[xi]:
                        if comp[nxt] == -1:
                            comp[nxt] = cid
                            q.append(nxt)

                yi = point_y[p]
                if y_comp[yi] == -1:
                    y_comp[yi] = cid
                    for nxt in y_adj[yi]:
                        if comp[nxt] == -1:
                            comp[nxt] = cid
                            q.append(nxt)

            comp_size.append(size)
            cid += 1

        answer = 1

        # Existing x/y coordinates
        xs = list(x_id.items())
        ys = list(y_id.items())

        # Best using an existing x
        for _, xi in xs:
            seen = set()
            total = 1
            for p in x_adj[xi]:
                c = comp[p]
                if c not in seen:
                    seen.add(c)
                    total += comp_size[c]
            answer = max(answer, total)

        # Best using an existing y
        for _, yi in ys:
            seen = set()
            total = 1
            for p in y_adj[yi]:
                c = comp[p]
                if c not in seen:
                    seen.add(c)
                    total += comp_size[c]
            answer = max(answer, total)

        # Best using one existing x and one existing y
        for _, xi in xs:
            base = {}
            for p in x_adj[xi]:
                c = comp[p]
                base[c] = comp_size[c]

            base_sum = sum(base.values())

            for _, yi in ys:
                total = base_sum
                for p in y_adj[yi]:
                    c = comp[p]
                    if c not in base:
                        total += comp_size[c]
                answer = max(answer, total + 1)

        return answer
