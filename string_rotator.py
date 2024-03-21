def rotate_word(word, rotate_by):
    ans = ""
    for alphabet in word:
        if alphabet.islower():
            if ord(alphabet) + rotate_by > 122:
                ans += chr(96 + rotate_by % 26)
            else:
                ans += chr(rotate_by + ord(alphabet))
        else:
            if ord(alphabet) + rotate_by > 90:
                ans += chr(64 + rotate_by % 26)
            else:
                ans += chr(rotate_by + ord(alphabet))
    print("Rotated Word:", ans)
