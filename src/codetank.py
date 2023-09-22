# App Entrypoint
import gc
import time
import sys
import random

# Global Variables
EFFECT_SPEED = 0.3
LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"

def main():
    # Program is started. Run startup sequence.
    startupSequence()
    # Program continues after startup sequence. Run proxy sequence.

    # Program continues after Proxy Iteration. Run shutdown sequence.

    # Data acquired from default style file.
    # default_style = {
    #     "var1": "I",
    #     "var2": "am",
    #     "var3": "a",
    #     "var4": "programmer"
    # }
    # for i in default_style:
    #     print(default_style[i])
    #     time.sleep(EFFECT_SPEED)
    
    # Data is written, line by line, to console in a loop w/ time delay.
    # del default_style
    # gc.collect()

def startupSequence():
    trans_table = [
        {"a": "ム"},
        {"b": "ら"},
        {"c": "つ"},
        {"d": "り"},
        {"e": "に"},
        {"f": "フ"},
        {"g": "ゲ"},
        {"h": "ヒ"},
        {"i": "イ"},
        {"j": "ジ"},
        {"k": "キ"},
        {"l": "リ"},
        {"m": "ム"},
        {"n": "ニ"},
        {"o": "オ"},
        {"p": "プ"},
        {"q": "ク"},
        {"r": "ル"},
        {"s": "ス"},
        {"t": "ツ"},
        {"u": "ウ"},
        {"v": "ヴ"},
        {"w": "ワ"},
        {"x": "ゥ"},
        {"y": "ヤ"},
        {"z": "ズ"},
        {"A": "ム"},
        {"B": "ら"},
        {"C": "つ"},
        {"D": "り"},
        {"E": "に"},
        {"F": "フ"},
        {"G": "ゲ"},
        {"H": "ヒ"},
        {"I": "イ"},
        {"J": "ジ"},
        {"K": "キ"},
        {"L": "リ"},
        {"M": "ム"},
        {"N": "ニ"},
        {"O": "オ"},
        {"P": "プ"},
        {"Q": "ク"},
        {"R": "ル"},
        {"S": "ス"},
        {"T": "ツ"},
        {"U": "ウ"},
        {"V": "ヴ"},
        {"W": "ワ"},
        {"X": "ゥ"},
        {"Y": "ヤ"},
        {"Z": "ズ"}
    ]

    phrase = "Program starting up. Please stand by."
    intro2 = "Critical Error. Phalanx.exe has found anomalies in system architecture."

    for char in phrase:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.04)

    print("")
    for idx in range(5):
        print("...")
        time.sleep(1.2)
    time.sleep(3)
    print("")
    print(LINE_UP, end=LINE_CLEAR)

    for idx in range(5):
        print(intro2)
        sys.stdout.flush()
        print(LINE_UP, end=LINE_CLEAR)
        time.sleep(random.randint(8, 15) / 10)
        print(ranStr(phrase, trans_table))
        sys.stdout.flush()
        time.sleep(random.randint(2, 5) / 100)
        print(LINE_UP, end=LINE_CLEAR)

    for idx in range(5):
        print(intro2)
        sys.stdout.flush()
        print(LINE_UP, end=LINE_CLEAR)
        time.sleep(random.randint(8, 15) / 10)
        print(glitchEffect())
        sys.stdout.flush()
        time.sleep(random.randint(2, 5) / 100)
        print(LINE_UP, end=LINE_CLEAR)

def ranStr(phrase, table):
    new_phrase = ""
    for i in range(20, len(phrase)):
        idx = random.randint(0, 45)
        ran_letter = list(table[idx].keys())[0]
        for dict in table:
            for key in dict:
                if key == ran_letter:
                    new_phrase += dict[key]
    return new_phrase

def proxySequence():
    print("Hello, World!")
    time.sleep(EFFECT_SPEED)

def shutdownSequence():
    print("Hello, World!")
    time.sleep(EFFECT_SPEED)  

def glitchEffect():
    glitch_bank = [
        " T̶̼̾h̴̢͇͂̽e̷̳̔ ̵̖̂͠ḿ̵̯̺͛a̶͖̕ẗ̷̪́r̴̛͔̂ȋ̶̝x̵͕͊̊ ̷͇̏͗h̶͎̥̽̈́a̸̛̘̤s̴͓̀ ̷̞̝́̌ỳ̶̫o̶͍͍͝ṳ̵̲̽" ,
        " c̵̳͠r̴͉̺̈̽į̶̂ṱ̵͋î̸̙̼Y̵̨͙͒c̵̘͛͠ḁ̴̢̀̚l̶̲̞̃ ̸̰͕͒ė̶̥̪̕R̴͍̈́͘r̵̯̾͒o̸̩͋͗ŕ̶̰̏.̸̛̪͠ ̵͙̫̄R̷̘̃ę̸̃̈́ļ̵́̏ë̶͕̙́͠ǎ̴̻͎s̴̟̩͛e̴̤͒͜͝ ̷̫̎p̷̰͗̃r̸̯͓̍i̸̱̓̈s̷̼̋m̷̖̖̆.̷̪̺͋ ",
        " T̴̠͈͊h̶̡̽̚ẻ̶̪̼̚y̵̥̜͛ ̶̟͒͊ā̵̤̠ȓ̵͙͗e̷̫̓ ̴͚͊ẇ̶̬̿ͅa̸̹͝t̵͔̯͛c̷̭͚͗̎h̶̲͑ḯ̸̪̐n̶̦̂̆g̴̲͝ ̶̼̖̌y̷̱̮̿ọ̸̱̚u̶̱͒.̴̠̭̕.̷̠̩͗̌.̸̲͋ "
    ]
    return random.choice(glitch_bank)

if __name__ == "__main__":
    main()