import sys

def customized_hello(first_name, last_name, prefix):
    print("Hello %s %s %s!" % (prefix, first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    prefix = sys.argv[3]
    customized_hello(first_name, last_name, prefix)
