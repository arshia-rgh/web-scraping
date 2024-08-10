def validate_category(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if arg not in ["car", "motorcycle", "truck"]:
                raise ValueError("The category should be car motorcycle or truck")

        return func(self, *args, **kwargs)

    return wrapper
