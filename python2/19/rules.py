def internal_rule(string):
    i = string.split(' if ')
    t = i[1].split(' then ')
    r = i[0].split('rule ')
    return {'rule': r[1].strip(), 'if':internal(t[0]), 'then':internal(t[1])}

def external_rule(rule):
    return ('rule '    + rule['rule']           +
            ' if '     + external(rule['if'])   +
            ' then '   + external(rule['then']) + '.')

def internal(conjunct):
    res = []                                    
    for clause in conjunct.split(','):          
        res.append(clause.split())              
    return res

def external(conjunct):
    strs = []
    for clause in conjunct:                     
        strs.append(' '.join(clause))           
    return ', '.join(strs)                      