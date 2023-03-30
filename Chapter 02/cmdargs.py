# cmdargs_eg1
import sys
prog_name = sys.argv[0]
args = sys.argv[1:]
count = len(args)
print(prog_name) # -- Cmd1
print(args) # -- Cmd2
print(count) # -- Cmd3
for x in sys.argv:
    print(f"Argument: , {x}") # -- Cmd4

# cmdargs: Note1
import sys
print(sys.argv[1])

# cmdargs: Note2
import sys
print(sys.argv[1] + sys.argv[2]) # -- TC1
print(int(sys.argv[1]) + int(sys.argv[2])) # -- TC2


