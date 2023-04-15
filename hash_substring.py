# python3
# Krists Kristaps Dūda 221RDB518 10.grupa
import compute_hash


def read_input(filename):
    
    input = input().rstrip()

    if input == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input == 'F':
        try:
            with open(f"./tests/{filename}") as f:
                content = f.readline()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except: 
            raise ValueError(f"Error reading {filename}")
        pattern = content[0].strip()
        text = content[1].strip()  
    else:
        raise ValueError(f"Invalid input type: {input}")
    
    return pattern, text
            
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and
    # capital f (input from file) to choose which input 
    # type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't 
    # need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using 
    # Rabin Karp alghoritm
    prime = 10**9 + 7
    base = 256
    
    patterhash = 0
    texthash = 0
    pattern_len, text_len = len(pattern), len(text)
    pattern_hash = compute_hash(pattern, prime, base)
    text_hash = compute_hash(text[:pattern_len], prime, base)
    occur = set()
    if pattern_hash == text_hash and pattern == text[:pattern_len]:
        occur
    for i in range(1, text_len - pattern_len + 1):
        text_hash = (text_hash * base + ord(text[i -1])) * pow(base, pattern_len, prime) + ord(text[i + pattern_len -1]) % prime
        if pattern_hash == text_hash and pattern == text[i:i + pattern_len]:
            occur.add(i)
    return occur


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

