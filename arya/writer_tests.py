from writer import Writer
w = Writer()
# Perform dash attack
w.parse("t MAIN 0.2 0.5, p A; r", "; ")
w.advance()
w.advance()
