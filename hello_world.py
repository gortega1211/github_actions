import os

def main() -> None:
    name = os.getenv("USERNAME")
    print(f"Hello, {name} from GitHub!")

if __name__ == "__main__":
    main()