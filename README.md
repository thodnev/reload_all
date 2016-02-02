# reload_all
A recursive reloader inpired by Mark Lutz's book.
Currently only Python3 is supported

```python
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
``` 
    ... for implementation details, see reload_all.py ...
