import requests


def fetch_quote():
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        quote = f"{data[0]['q']} - {data[0]['a']}"
        return quote
    except requests.exceptions.RequestException as e:
        return f"Error fetching quote: {e}"


def main():
    print("Welcome to the Random Quote Generator!")
    while True:
        print("\nFetching a random quote for you...")
        print(fetch_quote())

        choice = input("\nWould you like another quote? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Thank you for using the Random Quote Generator! Goodbye!")
            break


if __name__ == "__main__":
    main()
