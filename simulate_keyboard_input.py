
import keyboard
import time

practice = True
replay_state = False
current_role = 2
turtle_2 = 0
turtle_4 = 1
long = 2
total_role = 3
chat_model = False
role_list = ["2龟", "4龟", "龙"]




def release_all_keys():
    event_list = []
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 31, name='s',time = 0.01, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 17, name='w',time = 0.03, modifiers=False, is_keypad=False))
    keyboard.play(event_list)
    
    
def long_lr_flag():

    event_list = []
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.01, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 17, name='w',time = 0.03, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 17, name='w',time = 0.12, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.12, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 31, name='s',time = 0.13, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 36, name='j',time = 0.13, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 36, name='j',time = 0.19, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 31, name='s',time = 0.19, modifiers=False, is_keypad=False))
    keyboard.play(event_list)

def long_rl_flag():
    event_list = []
    event_list.append(keyboard.KeyboardEvent('down', 30, name='a',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0.01, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 30, name='a',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 17, name='w',time = 0.03, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 17, name='w',time = 0.12, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0.12, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 31, name='s',time = 0.13, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 36, name='j',time = 0.13, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 36, name='j',time = 0.19, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 31, name='s',time = 0.19, modifiers=False, is_keypad=False))
    keyboard.play(event_list)

def long_up_down_flag():
    event_list = []
    event_list.append(keyboard.KeyboardEvent('down', 17, name='w',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 17, name='w',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 31, name='s',time = 0.04, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 36, name='j',time = 0.04, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 36, name='j',time = 0.14, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 31, name='s',time = 0.14, modifiers=False, is_keypad=False))
    keyboard.play(event_list)

def t2_lr_flag_bisha():
    # print("2龟从左到右  飞腿+必杀")
    event_list = []
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 31, name='s',time = 0, modifiers=False, is_keypad=False))
    
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.03, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 37, name='k',time = 0.03, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.09, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 37, name='k',time = 0.09, modifiers=False, is_keypad=False))
    
    event_list.append(keyboard.KeyboardEvent('down', 36, name='j',time = 0.10, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 17, name='w',time = 0.10, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 36, name='j',time = 0.15, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 17, name='w',time = 0.15, modifiers=False, is_keypad=False))
    keyboard.play(event_list)

def t2_rl_flag_bisha():
    # print("2龟从右到左  飞腿+必杀")
    event_list = []
    event_list.append(keyboard.KeyboardEvent('up', 30, name='d',time = 0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 31, name='s',time = 0, modifiers=False, is_keypad=False))
    
    event_list.append(keyboard.KeyboardEvent('down', 30, name='a',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 30, name='a',time = 0.05, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 37, name='k',time = 0.05, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0.09, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 37, name='k',time = 0.09, modifiers=False, is_keypad=False))
    
    event_list.append(keyboard.KeyboardEvent('down', 36, name='j',time = 0.10, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 17, name='w',time = 0.10, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 36, name='j',time = 0.15, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 17, name='w',time = 0.15, modifiers=False, is_keypad=False))
    keyboard.play(event_list)
    
def t4_rl_flag_bisha():
    # print("4龟从右到左  飞腿+必杀")
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

def t4_lr_flag_bisha():
    # print("4龟从左到右  飞腿+必杀")
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


def run():
    event_list = []
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.03, modifiers=False, is_keypad=False))
    keyboard.play(event_list)

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
    
def qianmenhuanshu():
    cnt = 0
    # print("千门幻术...")
    release_all_keys()
    event_list = []
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.0, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.02, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 32, name='d',time = 0.05, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 32, name='d',time = 0.20, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 30, name='a',time = 0.20, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('down', 31, name='s',time = 0.20, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 30, name='a',time = 0.20, modifiers=False, is_keypad=False))
    event_list.append(keyboard.KeyboardEvent('up', 31, name='s',time = 0.20, modifiers=False, is_keypad=False))
    keyboard.play(event_list)
    cnt += 1


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
    global current_role
    global chat_model
    if event.name == 'esc' and event.event_type == "down":
        chat_model = bool(1 - chat_model)
        print("chat model: ", chat_model)
    if chat_model:
        return
        
    # Shred 百裂拳
    if  event.name == "y" and event.event_type == "down":
        bailie()
    
    # Shred 千门幻术
    if event.name == 'm' and event.event_type == "down":
        qianmenhuanshu()
    
    # 跑起来 成功
    elif event.name == 'r'and event.event_type == "down":
        run()
    # 左飞腿
    elif event.name == 'h'and event.event_type == "down":
        if current_role == turtle_2 or current_role == turtle_4:
            rl_flyLag()
        elif current_role == long:
            long_rl_flag()
    # 右飞腿
    elif event.name == 'l'and event.event_type == "down":
        if current_role == turtle_2 or current_role == turtle_4:
            lr_flyLag()
        elif current_role == long:
            long_lr_flag()
    elif event.name == 'i' and event.event_type == "down":
        if current_role == long:
            long_up_down_flag()
            
    # 龟飞腿必杀从左到右
    elif event.name =="e" and event.event_type == "down":
        if current_role ==  turtle_2:
            t2_lr_flag_bisha()
        elif current_role ==  turtle_4:
            t4_lr_flag_bisha()
            
    # 龟飞腿必杀从右到左
    elif event.name =="q" and event.event_type == "down":
        if current_role ==  turtle_4:
            t4_rl_flag_bisha()
        elif current_role ==  turtle_2:
            t2_rl_flag_bisha()
    elif event.name == '=' and event.event_type == "down":
        current_role = (current_role+1) % (total_role)
        print("current role : ", role_list[current_role])
    

## 录制技能
def recordSkill():
    keyboard.start_recording();
    time.sleep(5);
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
    
    f = keyboard.hook(on_triggered)
    print("current role : ", role_list[current_role])
    time.sleep(2000)
    
    # recordSkill()
        