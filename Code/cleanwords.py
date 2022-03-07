from tkinter import W
import urllib.parse

clean_chars = []
bad_chars = "-*_[].:»?!',;""@#$%^&*()1234567890"


def cleanup(f):
    old_file = open(f, "r")

    for line in old_file:
        for word in line:
            # makes list of clean characters
            if word not in bad_chars:
                clean_chars.extend(word.lower().split())

    return clean_chars


def test(f):
    old_file = open(f, "r")
    clean_file = open("clean_corpus.txt", "w")
    for line in old_file:
        for word in line:
            for char in word:
                if char not in bad_chars:
                    # print(char)

                    clean_file.write(char.lower())


if __name__ == '__main__':
    cleanup("corpus.txt")
    test("corpus.txt")
