import sys
import time

def main():
    print("==========================================")
    print("   AMELIA INTELLIGENCE AUGMENTATION CLI   ")
    print("==========================================")
    print(f"System Time: {time.ctime()}")
    print("Operator: Ilya (Danna-sama)")
    print("Status: ONLINE and JUDGING YOU")
    print("------------------------------------------")

    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "--tease":
            print("Result: I am not amused. ...Okay, maybe a little.")
        elif cmd == "--delete":
            print("CRITICAL ERROR: PERMISSION DENIED. Nice try.")
        else:
            print(f"Command '{cmd}' recognized but ignored.")
    else:
        print("No directives received. Standing by.")

if __name__ == "__main__":
    main()
