import argparse
import random

from pprint import(
    pformat
)


def generate_emoji():
    emoji_start = '0001f601'
    emoji_end = '0001f64f'
    
    emoji_code = random.randint(int(emoji_start, 16), int(emoji_end, 16))
    emoji = chr(emoji_code)

    return emoji

def generate_alhabet():
    alphabet = []
    for _ in range(10):
        alphabet.append(random.choice(generate_emoji()))
    
    return alphabet
    
def encode_string(string, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x)) for x in "{}".split(" ")])))'.format(
            pformat(d2),
            " ".join("".join(d1[int(i)] for i in str(ord(ch))) for ch in string)
        )
    )

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        prog="Emfuscator",
        description="This program translates program into emoji\'s",
        epilog="Only for research purposes")
    
    parser.add_argument(
        "-f", "--file",
        metavar='FILE',
        action="store",
        type=str,
        required=True,
        help='File to save ouput'
    )
    
    parser.add_argument(
        "-o", "--output",
        metavar='FILE',
        action="store",
        type=str,
        help='File to save ouput'
    )
    
    args = parser.parse_args()
    
    with open(args.file, "r", encoding="UTF8") as input:   
        res = encode_string(input.read(), generate_alhabet())
        
        if args.output:
            with open(args.output, "w", encoding="UTF8") as output:
                output.write(res)
        else:
            print(res)