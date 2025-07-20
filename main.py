import time
import sys

lyrics = [
    ("Tingnan natin nang husto (Pagmasdan mo nang maigi)", 0.3),
    ("Ang makulay kong mundo (Mga tao sa paligid)", 0.4),
    ("Kahit minsa'y magulo (Kahit medyo alanganin)", 0.4),
    ("Yayakapin nang buo (Ikaw pa rin ang hahanapin)", 0.4)
]

def type_out(text, delay=0.16):  
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def play_lyrics(lyrics):
    for line, line_delay in lyrics:
        type_out(line)
        time.sleep(line_delay)

if __name__ == "__main__":
    print("Now playing: Aura by IV of Spades\n")
    play_lyrics(lyrics)