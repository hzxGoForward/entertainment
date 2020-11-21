# from pymouse import PyMouse
# from pykeyboard import PyKeyboard
import keyboard
import time

# m = PyMouse()
# k = PyKeyboard()
# time.sleep(3);
# k.type_string(".........")

# time.sleep(3);
# send_location = m.position();

# m.click(send_location[0],send_location[1])

stop = False

def run():
    interval= 0.04
    keyboard.send('d')
    time.sleep(interval)
    keyboard.send('d',True, False)
    time.sleep(interval)

def flyLag():
    e1 = keyboard.KeyboardEvent('down',32, name='d',time = 0.45, modifiers=False, is_keypad=False)
    e2 = keyboard.KeyboardEvent('up',32, name='d',time = 0.48, modifiers=False, is_keypad=False)
    e3 = keyboard.KeyboardEvent('down',32, name='d',time = 0.52,modifiers=False, is_keypad=False)
    e4 = keyboard.KeyboardEvent('down',37, name='k',time = 0.55, modifiers=False, is_keypad=False)
    e5 = keyboard.KeyboardEvent('up',32, name='d',time = 0.63,modifiers=False, is_keypad=False)
    e6 = keyboard.KeyboardEvent('up',37, name='k',time = 0.65, modifiers=False, is_keypad=False)
    event_list = [e1, e2, e3, e4, e5, e6]
    keyboard.play(event_list)


def shred():
    e1 = keyboard.KeyboardEvent('down',32, name='d',time = 0.94, modifiers=False, is_keypad=False)
    e2 = keyboard.KeyboardEvent('down',31, name='s',time = 0.96, modifiers=False, is_keypad=False)
    e3 = keyboard.KeyboardEvent('down',36, name='j',time = 0.98, modifiers=False, is_keypad=False)
    e4 = keyboard.KeyboardEvent('up',32, name='d',time = 1.00, modifiers=False, is_keypad=False)
    e5 = keyboard.KeyboardEvent('up',36, name='j',time = 1.03, modifiers=False, is_keypad=False)
    e6 = keyboard.KeyboardEvent('up',31, name='s',time = 1.07, modifiers=False, is_keypad=False)
    event_list = [e1, e2, e3, e4, e5, e6]
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
    flyLag()
    time.sleep(0.15)
    tuQiu()



# event 类型是keyboard.KeyboardEvent
def on_triggered(event):
    interval= 0.04
    # Shred 必杀技
    if  event.name == "o" :
        # print("Triggered!")
        shred()
        
    # 吐球
    elif event.name == "n" :
        tuQiu()

    elif event.name == 'm':
        keyboard.press('j')
        time.sleep(interval);
        keyboard.release('j');
    
    # 跑起来 成功
    elif event.name == 'r':
        run()
    
    # 飞腿
    elif event.name == 'p':
        flyLag()

    # 飞行+吐球
    elif event.name == 'l':
        flayLay_tuQiu()

## 录制技能
def recordSkill():
    keyboard.start_recording();
    time.sleep(4);
    eventlist = keyboard.stop_recording();
    i = 0
    for e in eventlist:
        i += 1
        print("e{} = keyboard.KeyboardEvent('{}',{}, name='{}',time = {}, modifiers={}, is_keypad={})".format(i, e.event_type, e.scan_code, e.name, e.time,False, False));
    keyboard.play(eventlist)



if __name__ == "__main__":
    
    print("start to listening")
    f = keyboard.hook(on_triggered)
    time.sleep(1000)
    # recordSkill()



