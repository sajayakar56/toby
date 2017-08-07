import aria
import string
import re

##################
# COMMANDS #######
##################
# stop DONE 
# if () () ()
# do _ DONE 
# rdo _ DONE
# try _ : moveto, defs
# ?___: query
# def

class Parser:
    def __init__(self):
        self.ai = aria.AI()
        self.player_num = 2

    # errors handled here, always returns a string
    def lang_parse(self, s: str) -> str:
        try:
            # Revise this; this can allow arbitrary code to be executed
            if ("if" in s):
                return self.cond(s[3:])
            if s == "q":
                raise SystemExit
            if s[0] == "?":
                return self.query(s[1:])
            if s == "stop":
                return self.stop()
            s = s.split()
            if s[0] == "do":
                return self.do(s[1])
            if s[0] == "rdo":
                return self.do(s[1], True)
            return "ERROR: Invalid statement '%s'" % s
                
        except Exception as e:
            return str(e)

    # Far from implemented
    def cond(self, expr) -> None:
        return expr
        # expr = re.compile(expr)
        # condition = expr.match("(*)")
        
    def stop(self) -> None:
        self.ai.stop()
        self.ai.parse("r")
        self.ai._wait_frame()

    def do(self, action: str, r: bool = False) -> None:
        m = self.do_map
        action = action.split(",")
        action, params = action[0], action[1:]
        # print(action, params)
        if action in m:
            action = m[action]
            if r:
                action += "; r"
            if params:
                action = action(*params)
            print(action)
            self.ai.do(action)
        
    def query(self, s: str) -> str:
        m = self.query_map
        if s in m:
            return str(eval(self.query_map[s]))
        return ("ERROR: Invalid query")

    query_map = {"x2": "self.ai.sm.p2.x",
                "y2": "self.ai.sm.p2.y",
                "state2": "self.ai.sm.p2.action",
                "x1": "self.ai.sm.p1.x",
                "y1": "self.ai.sm.p1.y",
                "state1": "self.ai.sm.p1.action",
                "dist": "self.ai.sm.p2.dist(self.ai.sm.p1)"}

    @property
    def do_map(self):
        return {"d_tilt": self.ai.dTilt,
                "u_tilt": self.ai.uTilt,
                "wavedash": self.ai.waveDash,
                "walk_left": self.ai.walkLeft,
                "walk_right": self.ai.walkRight,
                "crouch": self.ai.crouch,
                "jab": self.ai.jab}
    

# REPL
if __name__ == "__main__":
    p = Parser()
    while True:
        print(">", end=" ")
        ret = p.lang_parse(input())
        if ret:
            print(ret)
    

