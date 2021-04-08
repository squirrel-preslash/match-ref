import inspect

class ScopeReference(object):
    """ An object representing the current namespace of the callee.
    
    Attribute access can be used to retrieve variables from the current
    scope of your program. This class is designed to be used in conjunction
    with the "case"-statement where references to variables are only allowed
    if they contain qualified (dotted) names.
    
    This constructor takes no arguments and implements only a single function 
    called __getattr__(), which resolves local as well as global names, in this
    order.
    
    Example:
        >>> from matchref import ref
        >>> value = 10
        >>> def function():
        ...     local_value = 50
        ...     print("Local:", ref.local_value)
        ...     print("Global:", ref.value)
        >>> function()
        Local: 50
        Global: 10
    
    """
    
    def __getattr__(self, name):
        """ Resolves a variable from the calling stack-frame's namespace """
        environment = inspect.currentframe().f_back
        try:
            local_namespace = environment.f_locals
            if name in local_namespace:
                return local_namespace[name]
            global_namespace = environment.f_globals
            if name in global_namespace:
                return global_namespace[name]
            
            raise NameError("referenced name '" + name + "' is not defined")
            
        finally:
            del environment

ref = ScopeReference()
