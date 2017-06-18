from .AI import AI

# Write an interface that is a bit lower level than the parser,
# so that the parser will pass into this class.  This will have 
# all of the functions that need to be implemented (such as do)

class Interface:
    def __init__(self):
        self.ai = aria.AI()
        self.sm = self.ai.sm
        
    # For now, result and otherwise are Python code that is evaled
    # Consider changing to Python Code objects that are compiled
    def cond(self, condition: str, result: str, otherwise: str) -> None:
        return None

    def query(self, name: str) -> str:
        if name in query_map:
            return query_map[name]

    def stop(self) -> None:
        self.ai.stop()
        self.ai.parse("r")
        self.ai._wait_frame()

    def do(self, action: "str", *params):
        if action in do_map:
            return do_map[action](*params)
        
