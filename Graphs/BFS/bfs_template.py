queue = [start]
visited = {start}

while queue is not empty:
    #get the node from the queue
    node = queue.pop_front()

    for neighbor in node.neighbors:
        #add all the new neighbors in queue
        if neighbor not in visited:
            visited.add(neighbor)
            queue.push_back(neighbor)