import sys
from stats import analyze_and_print

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
analyze_and_print(book_path)

