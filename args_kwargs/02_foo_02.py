def foo(x, *args, **kwargs):
    kwargs['name'] = "Alice"
    new_args = args + ('extra',)
    bar(x, *new_args, **kwargs)
