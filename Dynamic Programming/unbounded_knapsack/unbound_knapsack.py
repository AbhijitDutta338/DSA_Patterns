# ─────────────────────────────────────────
# UNBOUNDED KNAPSACK
# ─────────────────────────────────────────
# Unbounded = each item can be picked UNLIMITED times
# Goal      = maximize total value within weight capacity

def get_next_item(items, after=None):
    found = after is None
    for item in items:
        if not found:
            if item == after:
                found = True
            continue
        return item
    return None


def unbounded_knapsack(items, capacity):
    # dp[w] = max value achievable with exactly weight w
    dp       = [0] * (capacity + 1)
    selected = [[] for _ in range(capacity + 1)]

    weight = 1

    while weight <= capacity:
        item = get_next_item(items)

        while item is not None:
            item_weight, item_value = item

            if item_weight <= weight:
                candidate = dp[weight - item_weight] + item_value

                if candidate > dp[weight]:
                    dp[weight]       = candidate
                    selected[weight] = selected[weight - item_weight] + [item]

            item = get_next_item(items, item)

        weight = weight + 1

    return dp[capacity], selected[capacity]


# ─────────────────────────────────────────
# PRINT HELPER
# ─────────────────────────────────────────

def print_result(max_value, chosen_items, capacity):
    print("Capacity         :", capacity)
    print("Max value        :", max_value)
    print("Items chosen     :")

    index = 0
    while index < len(chosen_items):
        item_weight, item_value = chosen_items[index]
        print("  Item", index + 1, "— weight:", item_weight, "  value:", item_value)
        index = index + 1

    total_weight = 0
    index = 0
    while index < len(chosen_items):
        total_weight = total_weight + chosen_items[index][0]
        index = index + 1

    print("Total weight used:", total_weight)


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == '__main__':

    # Each item is (weight, value)
    # Items can be picked UNLIMITED times

    items = [
        (2, 5),    # Item A — weight 2, value 5
        (3, 8),    # Item B — weight 3, value 8
        (4, 9),    # Item C — weight 4, value 9
        (5, 10)    # Item D — weight 5, value 10
    ]

    capacity = 10

    max_value, chosen_items = unbounded_knapsack(items, capacity)

    print("=== Unbounded Knapsack ===")
    print_result(max_value, chosen_items, capacity)

    print()

    # Second example — show repeated item usage clearly
    items_2 = [
        (1, 1),    # Item A — weight 1, value 1
        (3, 4),    # Item B — weight 3, value 4
        (4, 5),    # Item C — weight 4, value 5
        (5, 7)     # Item D — weight 5, value 7
    ]

    capacity_2 = 8

    max_value_2, chosen_items_2 = unbounded_knapsack(items_2, capacity_2)

    print("=== Unbounded Knapsack (Example 2) ===")
    print_result(max_value_2, chosen_items_2, capacity_2)