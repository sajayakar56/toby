import aria


def memory_map_tests():
    ai = aria.AI()
    while True:
        data = ai.lookup("P1 X", float)
        if data:
            print(data)
            return


def ai_parser():
    x = aria.AI()
    while True:
        x.parse(input())


def ai_dTilt():
    x = aria.AI()
    x.do(x.dTilt)

def ai_waveDash():
    x = aria.AI()
    x.do(x.waveDash(0))

if __name__ == "__main__":
    ai_waveDash()
