import sys
script, encoding, error = sys.argv


def main(lauguage_file, encoding, errors):
    line = lauguage_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(lauguage_file, encoding, errors)


def print_line( line, encoding, errors):
    next_lang = line.strip()
    raw_byts = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_byts.decode(encoding, errors=errors)

    print(raw_byts, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)