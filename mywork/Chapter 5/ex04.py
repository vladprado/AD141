import sys

args = sys.argv
args.pop(0)
args_sum = 0
for arg in args:
    args_sum += int(arg)
args_avg = args_sum / len(args)

print(args, args_sum, args_avg)
