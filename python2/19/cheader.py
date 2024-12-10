import sys, re
pattDefine = re.compile(
    '^#[\t ]*define[\t ]+(\w+)[\t ]*(.*)')

pattInclude = re.compile(
    '^#[\t ]*include[\t ]+[<"]([\w\./]+)')

def scan(fileobj):
    count = 0
    for line in fileobj:
        count += 1
        matchobj = pattDefine.match(line)
        if matchobj:
            name = matchobj.group(1)
            body = matchobj.group(2)
            print(count, 'defined', name, '=', body.strip())
            continue
        matchobj = pattInclude.match(line)
        if matchobj:
            start, stop = matchobj.span(1)
            filename = line[start:stop]
            print(count, 'include', filename)

if len(sys.argv) == 1:
    scan(sys.stdin)
else:
    scan(open(sys.argv[1], 'r'))