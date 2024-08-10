import requests


def fetch_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()
    quote = f"{data[0]['q']} - {data[0]['a']}"
    return quote


def main():
    while True:
        print("\nHere's a random quote for you:")
        print(fetch_quote())

        choice = input("\nWould you like another quote? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
