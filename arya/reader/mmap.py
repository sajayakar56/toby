from .watcher import MemoryWatcher
import struct

class MemoryMap:
    # int32 addr -> value: bytes
    data = {}

    def __init__(self):
        self.mw = MemoryWatcher()
        self.update()

    def lookup(self, addr: int) -> bytes:
        if addr in self.data:
            return self.data[addr]
        return None

    # Debug this function to see if received data is ever multiple
    def update(self) -> None:
        received_data = self.mw.receive()
        while received_data:
            addr, value = received_data
            self.data[addr] = value
            received_data = self.mw.receive()


# Should be global Melee State class? 
# Contains current stage, state counter, etc?
class State:
    def __init__(self, mm):
        self.mm = mm

    @property
    def frame(self) -> float:
        return self.mm.lookup(0x479d60)

    def __str__(self) -> str:
        return str(self.frame)

# Need to revisit this code when I actually remember how it works            
class Player:
    def __init__(self, number, mm):
        self.number = number
        self.mult = number - 1
        self.mm = mm
        self.offsets = [3728]

    def dist(self, other) -> float:
        x1, y1, x2, y2 = self.x, self.y, other.x, other.y
        if not (x1 or x2):
            return 100
        elif not (y1 or y2):
            return (x2 - x1)
        else:
            return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    @property
    def x(self) -> float:
        raw_value = self.offset_lookup(4534416, 0)
        return_val = bytes_to_float(raw_value)
        return nullHandler(return_val, 0)

    @property
    def y(self) -> float:
        raw_value = self.offset_lookup(4534420, 0)
        return_val = bytes_to_float(raw_value)
        return nullHandler(return_val, 0)

    @property
    def dmg(self) -> int:
        raw_value = self.offset_lookup(4534496, 0)
        return_val = bytes_to_int(raw_value)
        return nullHandler(return_val, 0)

    @property
    def stocks(self) -> int:
        raw_value = self.offset_lookup(4534542, 0)
        return_val = bytes_to_int(raw_value)
        return nullHandler(return_val, 0)

    @property
    def facing(self) -> str:
        raw_value = self.offset_lookup(4534464, 0)
        return_val = bytes_to_int(raw_value)
        if (return_val == 32959):
            return_val = "left"
        elif (return_val == 32831):
            return_val = "right"
        return nullHandler(return_val, "N/A")

    @property
    def action(self) -> str:
        raw_value = self.offset_lookup(4534688, 0)
        return_val = bytes_to_int(raw_value)
        if return_val in actions:
            return_val = actions[return_val]
        return nullHandler(return_val, "STANDING")

    @property
    def action_frame(self) -> int:
        raw_value = self.offset_lookup(4536868, 0)
        return_val = bytes_to_int(raw_value)
        return nullHandler(return_val, 0)

    @property
    def invulnerable(self) -> bool:
        raw_value = self.offset_lookup(4541212, 0)
        return_val = bytes_to_int(raw_value)
        if (return_val in (1, 2)):
            return_val = True
        return nullHandler(return_val, False)

    def offset_lookup(self, base: int, offset: int):
        addr = base + (self.mult * self.offsets[offset])
        return self.mm.lookup(addr)
        
    def __str__(self):
        return """
Player %d
    x: %s
    y: %s
    %%: %s
    facing: %s
    action: %s
    action_counter: %s
    invulnerable: %s
""" % (self.number, self.x, self.y, self.dmg,
       self.facing, self.action, self.action_frame, self.invulnerable)
            
def nullHandler(val, other):
    if val is None:
        return other
    return val

def bytes_to_float(b: bytes) -> float:
    if not b:
        return None
    return struct.unpack(">f", b)[0]


def bytes_to_int(b: bytes, endian="<") -> float:
    if not b:
        return None
    if endian == "<":
        b = b.ljust(4, b'\x00')
    # else:
        # b = b.rjust(4, b'\x00')
    return struct.unpack(endian + "i", b)[0]

# from libmelee    
actions = {0: "DEAD_DOWN",
           1: "DEAD_LEFT",
           2: "DEAD_RIGHT",
           4: "DEAD_FLY_STAR",
           6: "DEAD_FLY",
           7: "DEAD_FLY_SPLATTER",
           8: "DEAD_FLY_SPLATTER_FLAT",
           12: "ON_HALO_DESCENT",
           13: "ON_HALO_WAIT",
           14: "STANDING",
           15: "WALK_SLOW",
           16: "WALK_MIDDLE",
           17: "WALK_FAST",
           18: "TURNING",
           19: "TURNING_RUN",
           20: "DASHING",
           21: "RUNNING",
           24: "KNEE_BEND",
           25: "JUMPING_FORWARD",
           26: "JUMPING_BACKWARD",
           27: "JUMPING_AERIAL_FORWARD",
           28: "JUMPING_AERIAL_BACKWARD",
           29: "FALLING", 
           32: "FALLING_AERIAL",
           35: "DEAD_FALL",
           36: "SPECIAL_FALL_FORWARD",
           37: "SPECIAL_FALL_BACK",
           38: "TUMBLING",
           39: "CROUCH_START",
           40: "CROUCHING",
           41: "CROUCH_END",
           42: "LANDING",
           43: "LANDING_SPECIAL",
           44: "NEUTRAL_ATTACK_1",
           45: "NEUTRAL_ATTACK_2",
           46: "NEUTRAL_ATTACK_3",
           50: "DASH_ATTACK",
           51: "FTILT_HIGH",
           52: "FTILT_HIGH_MID",
           53: "FTILT_MID",
           54: "FTILT_LOW_MID",
           55: "FTILT_LOW",
           56: "UPTILT",
           57: "DOWNTILT",
           60: "FSMASH_MID",
           63: "UPSMASH",
           64: "DOWNSMASH",
           65: "NAIR",
           66: "FAIR",
           67: "BAIR",
           68: "UAIR",
           69: "DAIR",
           70: "NAIR_LANDING",
           71: "FAIR_LANDING",
           72: "BAIR_LANDING",
           73: "UAIR_LANDING",
           74: "DAIR_LANDING",
           75: "DAMAGE_HIGH_1",
           76: "DAMAGE_HIGH_2",
           77: "DAMAGE_HIGH_3",
           78: "DAMAGE_NEUTRAL_1",
           79: "DAMAGE_NEUTRAL_2",
           80: "DAMAGE_NEUTRAL_3",
           81: "DAMAGE_LOW_1",
           82: "DAMAGE_LOW_2",
           83: "DAMAGE_LOW_3",
           84: "DAMAGE_AIR_1",
           85: "DAMAGE_AIR_2",
           86: "DAMAGE_AIR_3",
           87: "DAMAGE_FLY_HIGH",
           88: "DAMAGE_FLY_NEUTRAL",
           89: "DAMAGE_FLY_LOW",
           90: "DAMAGE_FLY_TOP",
           91: "DAMAGE_FLY_ROLL",
           178: "SHIELD_START",
           179: "SHIELD",
           180: "SHIELD_RELEASE",
           181: "SHIELD_STUN",
           182: "SHIELD_REFLECT",
           183: "TECH_MISS_UP",
           184: "LYING_GROUND_UP",
           185: "LYING_GROUND_UP_HIT",
           186: "GROUND_GETUP",
           187: "GROUND_ATTACK_UP",
           188: "GROUND_ROLL_FORWARD_UP",
           189: "GROUND_ROLL_BACKWARD_UP",
           190: "TECH_MISS_DOWN",
           192: "LYING_GROUND_DOWN",
           193: "DAMAGE_GROUND",
           194: "NEUTRAL_GETUP",
           195: "GETUP_ATTACK",
           196: "GROUND_ROLL_FORWARD_DOWN",
           197: "GROUND_ROLL_BACKWARD_DOWN",
           199: "NEUTRAL_TECH",
           200: "FORWARD_TECH",
           201: "BACKWARD_TECH",
           212: "GRAB",
           213: "GRAB_PULLING",
           214: "GRAB_RUNNING",
           216: "GRAB_WAIT",
           217: "GRAB_PUMMEL",
           218: "THROW_FORWARD",
           219: "THROW_BACK",
           220: "THROW_UP",
           221: "THROW_DOWN",
           224: "GRABBED_WAIT_HIGH",
           225: "PUMMELED_HIGH",
           226: "GRAB_PULL",
           227: "GRABBED",
           228: "GRAB_PUMMELED",
           229: "GRAB_ESCAPE",
           233: "ROLL_FORWARD",
           234: "ROLL_BACKWARD",
           235: "SPOTDODGE",
           236: "AIRDODGE",
           239: "THROWN_FORWARD",
           240: "THROWN_BACK",
           241: "THROWN_UP",
           242: "THROWN_DOWN",
           245: "EDGE_TEETERING_START",
           246: "EDGE_TEETERING",
           251: "SLIDING_OFF_EDGE",
           252: "EDGE_CATCHING",
           253: "EDGE_HANGING",
           254: "EDGE_GETUP_SLOW",
           255: "EDGE_GETUP_QUICK",
           256: "EDGE_ATTACK_SLOW",
           257: "EDGE_ATTACK_QUICK",
           258: "EDGE_ROLL_SLOW",
           259: "EDGE_ROLL_QUICK",
           322: "ENTRY",
           323: "ENTRY_START",
           324: "ENTRY_END",
           342: "NEUTRAL_B_CHARGING",
           343: "NEUTRAL_B_ATTACKING",
           344: "NEUTRAL_B_FULL_CHARGE",
           345: "WAIT_ITEM",
           346: "NEUTRAL_B_CHARGING_AIR",
           347: "NEUTRAL_B_ATTACKING_AIR",
           348: "NEUTRAL_B_FULL_CHARGE_AIR",
           349: "SWORD_DANCE_1",
           350: "SWORD_DANCE_2_HIGH",
           351: "SWORD_DANCE_2_MID",
           352: "SWORD_DANCE_3_HIGH",
           353: "SWORD_DANCE_3_MID",
           354: "SWORD_DANCE_3_LOW",
           355: "SWORD_DANCE_4_HIGH",
           356: "SWORD_DANCE_4_MID",
           357: "SWORD_DANCE_4_LOW",
           358: "SWORD_DANCE_1_AIR",
           359: "SWORD_DANCE_2_HIGH_AIR",
           360: "SWORD_DANCE_2_MID_AIR",
           361: "SWORD_DANCE_3_HIGH_AIR",
           362: "SWORD_DANCE_3_MID_AIR",
           363: "SWORD_DANCE_3_LOW_AIR",
           364: "SWORD_DANCE_4_HIGH_AIR",
           365: "SWORD_DANCE_4_MID_AIR",
           366: "SWORD_DANCE_4_LOW_AIR",
               # FOX_ILLUSION_START = 0x15e
               # FOX_ILLUSION = 0x15f
               # FOX_ILLUSION_SHORTENED = 0x160
               # FIREFOX_WAIT_GROUND = 0x161 #Firefox wait on the ground
               # FIREFOX_WAIT_AIR = 0x162 #Firefox wait in the air
               # FIREFOX_GROUND = 0x163 #Firefox on the ground
               # FIREFOX_AIR = 0x164 #Firefox in the air
               # DOWN_B_GROUND_START = 0x168
               # DOWN_B_GROUND = 0x169
               # SHINE_TURN = 0x16c
               # DOWN_B_STUN = 0x16d #Fox is stunned in these frames
               # DOWN_B_AIR = 0x16e
               # UP_B_GROUND = 0x16f
               # SHINE_RELEASE_AIR = 0x170
           368: "UP_B",
           369: "MARTH_COUNTER",
           371: "MARTH_COUNTER_FALLING",
           374: "WAVEDASH_SLIDE",
           65535: "UNKNOWN_ANIMATION"}
