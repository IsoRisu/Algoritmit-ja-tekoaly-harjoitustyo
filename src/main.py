import random

def main():
    while True:
        # Read input commands from the program
        command = input().strip()
        
        # Process input commands and generate output responses
        # Implement your AI logic here

        move = random.randint(0,6)
        print(f"MOVE:{move}")
        print("jipii")
        
if __name__ == "__main__":
    main()