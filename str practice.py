print("one", end=" ")
print("two", end=" "*3)
print("three")
print("\t~~~four")

my_s = "DuckRabbit"
duck = my_s[:4]
rabbit = my_s[-6:]
print(rabbit+duck)


def main():
    u_name = input("Enter your name in this format: last, first: ")
    last_name = input("How many letters are in your last name? ")

    first = u_name[last_len:]
    last = u_name[:last_len]
    
    print(first,last)
    
if __name__ == "__main__":
    main()
