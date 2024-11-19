import requests as req

def main():
    print("A single file with a vulnerability.")
    xyz = input("Enter a domain: ")
    print(f"You entered {xyz}")
    q = f"https://{xyz}"
    print(f"The URL is: {q}")
    x = req.get(q)
    print(f"{x.status_code}")


if __name__ == "__main__":
    main()
