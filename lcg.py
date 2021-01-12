def lcg(seedVal):
    
    # Values of a, c and m were taken from the wikipedia link in the README.md
    a = 214013
    c = 2531011
    m = 2**32
    
    seedVal = (a * seedVal + c) % m
    return seedVal

def main():
    seedVal = input("Enter a seed value: ")
    print(lcg(int(seedVal)))

if __name__ == "__main__":
    main()
