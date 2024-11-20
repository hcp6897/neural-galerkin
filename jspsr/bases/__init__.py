def get_basis(name, **kwargs):
    r"""Get a basis instance given keyword arguments.
    
    :param name: name of the basis
    :return: basis instance
    """
    if name == "BezierTensorBasis":
        from .bezier_tensor import BezierTensorBasis
        return BezierTensorBasis()
    elif name == "AdditiveHermite":
        from .hermite_ns import AdditiveHermite
        return AdditiveHermite(**kwargs)
    else:
        raise NotImplementedError
