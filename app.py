from util import send_a_request

def main():
    print("Hello, world!")
    xyz = input("Enter a value: ")
    print(f"You entered {xyz}")
    send_a_request(xyz)


if __name__ == "__main__":
    main()
