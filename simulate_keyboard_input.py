
import keyboard
import time

practice = True
replay_state = False

def t4_lr_flag_bisha():
    event_list = []
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 31, name='s',time = 0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.03, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 37, name='k',time = 0.05, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.06, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 37, name='k',time = 0.06, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 17, name='w',time = 0.08, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 17, name='w',time = 0.09, modifiers=False, is_keypad=False))
    keyboard.play(event_list)
    
def t4_rl_flag_bisha():
    event_list = []
    event_list.append(keyboard.KeyboardEvent('up', 30, name='d',time = 0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 31, name='s',time = 0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 30, name='a',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 30, name='a',time = 0.04, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 37, name='k',time = 0.04, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0.06, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 37, name='k',time = 0.06, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 17, name='w',time = 0.07, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 17, name='w',time = 0.09, modifiers=False, is_keypad=False))
    keyboard.play(event_list)
    
def turtle_4_feitui_bisha():
    pass

def run():
    interval= 0.04
    keyboard.send('d')
    time.sleep(interval)
    keyboard.send('d',True, False)
    time.sleep(interval)

def lr_flyLag():
    event_list = []
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.03, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 37, name='k',time = 0.04, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.07, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 37, name='k',time = 0.07, modifiers=False, is_keypad=False))
    keyboard.play(event_list)

def rl_flyLag():
    event_list = []
    event_list.append(keyboard.KeyboardEvent('down', 30, name='a',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 30, name='a',time = 0.05, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 37, name='k',time = 0.05, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0.08, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 37, name='k',time = 0.08, modifiers=False, is_keypad=False))
    keyboard.play(event_list)

def bailie():
    event_list = []
    event_list.append(keyboard.KeyboardEvent('down', 36, name='j',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 36, name='j',time = 0.01, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 36, name='j',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 36, name='j',time = 0.20, modifiers=False, is_keypad=False))
    keyboard.play(event_list)


def tuQiu():
    e1 = keyboard.KeyboardEvent('down',31, name='s',time = 0.94, modifiers=False, is_keypad=False)
    e2 = keyboard.KeyboardEvent('down',32, name='d',time = 0.96, modifiers=False, is_keypad=False)
    e3 = keyboard.KeyboardEvent('down',36, name='j',time = 0.98, modifiers=False, is_keypad=False)
    e4 = keyboard.KeyboardEvent('up',32, name='d',time = 1.00, modifiers=False, is_keypad=False)
    e5 = keyboard.KeyboardEvent('up',36, name='j',time = 1.03, modifiers=False, is_keypad=False)
    e6 = keyboard.KeyboardEvent('up',31, name='s',time = 1.07, modifiers=False, is_keypad=False)
    event_list = [e1, e2, e3, e4, e5, e6]
    keyboard.play(event_list)


def flayLay_tuQiu():
    lr_flyLag()
    time.sleep(0.15)
    tuQiu()



# event 类型是keyboard.KeyboardEvent
def on_triggered(event):
    interval= 0.04
    # Shred 必杀技
    if  event.name == "o" and event.event_type == "down":
        # print("Triggered!")
        bailie()
    # 吐球
    elif event.name == "n" and event.event_type == "down":
        tuQiu()
    # 跑起来 成功
    elif event.name == 'r'and event.event_type == "down":
        run()
    # 左飞腿
    elif event.name == 'h'and event.event_type == "down":
        rl_flyLag()
    # 右飞腿
    elif event.name == 'l'and event.event_type == "down":
        lr_flyLag()
    # # 飞行+吐球
    # elif event.name == 'l'and event.event_type == "down":
    #     flayLay_tuQiu()
    elif event.name =="e" and event.event_type == "down":
        t4_lr_flag_bisha()
    elif event.name =="q" and event.event_type == "down":
        t4_rl_flag_bisha()
    elif event.name == 'x' and event.event_type == "down":
        global practice
        global replay_state
        practice = bool(1- practice)
        replay_state = bool(1 - replay_state)
        keyboard.unhook_all()
        print("Replay state")

## 录制技能
def recordSkill():
    keyboard.start_recording();
    time.sleep(4);
    eventlist = keyboard.stop_recording();
    
    i = 0
    first_time = 0
    print("event_list = []")
    if eventlist[0].event_type== "down" and eventlist[0].name == 'x':
        global practice
        global replay_state
        practice = bool(1- practice)
        replay_state = bool(1 - replay_state)
        print("Practice state")
    else:
        for e in eventlist:
            if first_time == 0:
                first_time = e.time
            t = e.time - first_time
            print("event_list.append(keyboard.KeyboardEvent('{}', {}, name='{}',time = {}, modifiers={}, is_keypad={}))".format(e.event_type, e.scan_code, e.name, round(t, 2), False, False));
        print("keyboard.play(event_list)")
        keyboard.play(eventlist)



if __name__ == "__main__":
    while True:
        if practice:
            f = keyboard.hook(on_triggered)
            time.sleep(2000)
        elif replay_state:
            recordSkill()
        