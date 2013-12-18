''' prepends a single rule to all gitignore files '''

import sys, glob

def prepend(line, filename):
    # save contents of file
    f = open(filename, 'r')
    original = f.read()
    f.close()
    # reopen file, deleting all content
    f = open(filename, 'w')
    f.write(line)
    f.write('\n')
    # append original file contents
    f.write(original)
    f.close()

if __name__ == '__main__':
    rule = sys.argv[1]

    # TODO should change this to arg flag (-n or something)
    if rule == 'newline':
        rule = ''
        print 'prepending newline'
    else:
        # keep it simple, only allow adding 1 rule
        if len(sys.argv) > 2:
            print "warning: only adding 1 rule"
        print "prepending rule: {0}".format(rule)

    files = glob.glob('*.gitignore')
    for filename in files:
        prepend(rule, filename)
