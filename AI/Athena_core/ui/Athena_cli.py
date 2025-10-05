# User interface (CLI stub).
def main():
    print("Welcome to AthenaPrime CLI!")
    while True:
        cmd = input("Command (perceive/act/recall/exit): ").strip().lower()
        if cmd == "perceive":
            data = input("What should Athena perceive? ")
            print(f"Perceived: {data}")
        elif cmd == "act":
            action = input("What should Athena do? ")
            print(f"Acting: {action}")
        elif cmd == "recall":
            print("Recalling memory (stub)...")
        elif cmd == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
