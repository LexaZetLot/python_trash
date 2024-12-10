trace = True

def rangetest(argchecks, failif):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            code     = func.__code__
            allargs  = code.co_varnames[:code.co_argcount]
            funcname = func.__name__
            def onError(argname, criteria):
                errfmt = '%s argument "%s" not %s'
                raise TypeError(errfmt % (func.__name__, argname, criteria))
            def onCall(*pargs, **kargs):
                expected    = list(allargs)
                positionals = expected[:len(pargs)]
                for (argname, criteria) in argchecks.items():
                    if argname in kargs:
                        if failif(kargs[argname], criteria):
                            onError(argname, criteria)
                        elif argname in positionals:
                            position = positionals.index(argname)
                            if failif(pargs[position], criteria):
                                onError(argname, criteria)
                    else:
                        if trace:
                            print('Argument "{0}" defaulted'.format(argname))
                return func(*pargs, **kargs)
            return onCall
    return onDecorator