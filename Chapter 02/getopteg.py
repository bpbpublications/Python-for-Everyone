import getopt

#short form options
print(getopt.getopt(['-a', '-dval', '-e', 'val'], 'ad:e:')) # -- SF1
print(getopt.getopt(['-aval', '-d', '-e', 'val'], 'a:de')) # --SF2
print(getopt.getopt(['-aval', '-dval', '-e', 'val'], 'a:d:e')) # -- SF3

# long form options

print(getopt.getopt([ '--noarg','--witharg', '--witharg2=another' ],
                    '',
                    [ 'noarg', 'witharg', 'witharg2=' ])) #-- LF1
print(getopt.getopt([ '--noarg', 'val','--witharg', 'val', '--witharg2' ],
                    '',
                    [ 'noarg=', 'witharg=', 'witharg2' ])) #-- LF2
print(getopt.getopt([ '--noarg', 'val','--witharg', 'val', '--witharg2=another' ],
                    '',
                    [ 'noarg=', 'witharg=', 'witharg2=' ])) #-- LF3
print(getopt.getopt([ '--noarg', 'val','--witharg', 'val', '--witharg2','val' ],
                    '',
                    [ 'noarg=', 'witharg=', 'witharg2=' ])) #-- LF4

