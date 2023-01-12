def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class) or (hasattr(obj, "__class__") and issubclass(obj.__class__, a_class))
