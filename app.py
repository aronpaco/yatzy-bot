import secrets

def roll(result):
    number_to_keep = 1
    for i in range(5):
        if result[i] != number_to_keep:
            result[i] = secrets.randbelow(6) + 1
    print(result)

def main():
    result = [0, 0, 0, 0, 0]
    reroll = [1,2,3,4,5]
    for _ in range(5):
        roll(result)

if __name__ == "__main__":
    main()
