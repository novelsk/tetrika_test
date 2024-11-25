def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for arg, annotation in zip(args, annotations.values()):
            if type(arg) is not annotation:
                raise TypeError(f"{type(arg)} is not {annotation}")
        for name, value in kwargs.items():
            annotation = annotations.get(name)
            if annotation is not None and type(value) is not annotation:
                raise TypeError(f"{name}: {type(value)} is not {annotation}")
        return func(*args, **kwargs)
    return wrapper
