# ─────────────────────────────────────────
# LONGEST PALINDROMIC SUBSTRING
# ─────────────────────────────────────────
# Goal — find the longest substring of a string that reads
#         the same forwards and backwards
#
# Approach — Expand Around Center
#   Every palindrome has a center — either a single character (odd)
#   or a gap between two characters (even)
#   Expand outward from every possible center and track the longest

def expand_around_center(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left  = left  - 1
        right = right + 1

    # left and right have gone one step too far — walk back
    return left + 1, right - 1


def longest_palindromic_substring(string):
    if len(string) == 0:
        return ""

    best_start = 0
    best_end   = 0

    center = 0

    while center < len(string):

        # Case 1 — Odd length palindrome  (single character center)
        # e.g.  "racecar" centers on 'e'
        odd_start, odd_end = expand_around_center(string, center, center)

        # Case 2 — Even length palindrome  (gap between two characters center)
        # e.g.  "abba" centers between the two b's
        even_start, even_end = expand_around_center(string, center, center + 1)

        if odd_end - odd_start > best_end - best_start:
            best_start = odd_start
            best_end   = odd_end

        if even_end - even_start > best_end - best_start:
            best_start = even_start
            best_end   = even_end

        center = center + 1

    return string[best_start : best_end + 1]


# ─────────────────────────────────────────
# PRINT HELPER
# ─────────────────────────────────────────

def print_result(string, result):
    print("Input string      :", string)
    print("Longest palindrome:", result)
    print("Length            :", len(result))


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == '__main__':

    print("=== Example 1 — Odd length palindrome ===")
    print_result("racecar", longest_palindromic_substring("racecar"))

    print()

    print("=== Example 2 — Even length palindrome ===")
    print_result("abbatest", longest_palindromic_substring("abbatest"))

    print()

    print("=== Example 3 — Palindrome in the middle ===")
    print_result("abacabad", longest_palindromic_substring("abacabad"))

    print()

    print("=== Example 4 — Multiple palindromes, pick longest ===")
    print_result("xyzabacabadpqr", longest_palindromic_substring("xyzabacabadpqr"))

    print()

    print("=== Example 5 — All same characters ===")
    print_result("aaaaaaa", longest_palindromic_substring("aaaaaaa"))

    print()

    print("=== Example 6 — No palindrome longer than 1 ===")
    print_result("abcdef", longest_palindromic_substring("abcdef"))

    print()

    print("=== Example 7 — Single character ===")
    print_result("a", longest_palindromic_substring("a"))