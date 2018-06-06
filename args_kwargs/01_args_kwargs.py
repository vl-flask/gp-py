def foo(reqd, *args, **kwargs):
    print(reqd)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
