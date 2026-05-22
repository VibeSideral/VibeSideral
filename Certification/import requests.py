try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"Error: Required module not found. Please install: pip install requests beautifulsoup4")
    raise

def print_secret_message(doc_url):
    # Download the Google Doc page
    response = requests.get(doc_url)
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text("\n")

    # Dictionary to store characters by (x, y) coordinates
    grid = {}

    # Track grid boundaries
    max_x = 0
    max_y = 0

    # Read each line from the document
    for line in text.splitlines():
        parts = line.strip().split()

        # Expected format: character x y
        if len(parts) != 3:
            continue

        char, x, y = parts

        # Skip invalid coordinate rows
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            continue

        # Store character in grid
        grid[(x, y)] = char

        # Update maximum dimensions
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Print the grid row by row
    for y in range(max_y + 1):
        row = ""

        for x in range(max_x + 1):
            row += grid.get((x, y), " ")

        print(row)


# Example usage
print_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)