def word_count(s):
    counts = {}
    ignore = [
        '"', ':', ';', ',', '.', '-', '+', '=',
        '/', '\\', '|', '[' ,']', '{', '}', '(',
        ')', '*', '^', '&']
    # clean string 
    for ch in s:
        if ch in ignore:
            s = s.replace(ch, "")
    s = s.lower()
    s = s.split(" ")

    # get word counts on split string by adding to dict
    for word in s:
        if len(word) == 0:
            continue
        elif word in counts:
            counts[word] += 1
        else:
            counts[word] = 1


    print(counts)
    return counts




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))