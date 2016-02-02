'''
A recursive reloader inpired by Mark Lutz's book.

Author: thodnev
'''
import importlib, sys

def reload_all(top_module, max_depth=20):
    '''
    A reload function, which recursively traverses through
    all submodules of top_module and reloads them from most-
    nested to least-nested. Only modules containing __file__
    attribute could be reloaded.
    
    Returns a dict of not reloaded(due to errors) modules:
      key = module, value = exception

    Optional attribute max_depth defines maximum recursion
    limit to avoid infinite loops while tracing
    '''
    module_type = type(importlib)   # get the 'module' type
    for_reload = dict() # modules to reload: K=module, V=depth
    
    def trace_reload(module, depth):    # recursive
        nonlocal for_reload
        depth += 1
        if type(module) == module_type and depth < max_depth:
            # if module is deeper and could be reloaded
            if (for_reload.get(module, 0) < depth
                and hasattr(module, '__file__') ):
                    for_reload[module] = depth
            # trace through all attributes recursively       
            for name, attr in module.__dict__.items():
                trace_reload(attr, depth)


    trace_reload(top_module, 0)         # start tracing
    reload_list = sorted(for_reload, reverse=True,
                         key=lambda k:for_reload[k])
    not_reloaded = dict()
    for module in reload_list:
        try:
            importlib.reload(module)
        except:     # catch and write all errors
            not_reloaded[module]=sys.exc_info()[0]
            
    return not_reloaded
                
    
