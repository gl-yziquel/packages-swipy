import swipl

class Query:
    def __init__(self, query, inputs={}):
        self.state = swipl.open_query(query, inputs)
    def __iter__(self):
        return self
    def __next__(self):
        rc = swipl.next_solution(self.state)
        if rc == False or rc["status"] == False:
            raise StopIteration()
        else:
            return rc
    def __del__(self):
        swipl.close_query(self.state)

def once(query, inputs={}, keep=False):
    return swipl.call(query, inputs, keep)

def consult(file):
    once("consult(File)", {"File":file})

def interact():
    import code
    vars = globals()
    vars.update(locals())
    try:
        import readline
        import rlcompleter
        readline.set_completer(rlcompleter.Completer(vars).complete)
        readline.parse_and_bind("tab: complete")
    except:
        pass
    code.InteractiveConsole(vars).interact();

    
