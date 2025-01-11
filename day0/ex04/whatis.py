import sys

sys.tracebacklimit = 0

args = sys.argv

if len(args) < 2 :
	sys.exit()

assert len(args) == 2, "more than one argument is provided"

try :
	n = int(sys.argv[1])
except ValueError:
	n = None

assert n is not None, "argument is not an integer"

if (n % 2 == 0) :
	print("I'm Even.")
else :
	print("I'm Odd.")


