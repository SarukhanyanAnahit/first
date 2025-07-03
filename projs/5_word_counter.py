import argparse

def clean(text):
    punc='-_*/\\|`~@#$%^&+=.,!?;:"\'()[]{}<>'
    for char in punc:
        text=text.replace(char, '')
    file_words=text.lower().split()
    return [el for el in file_words]

def count(words):
    md={}
    for el in words:
        if el not in md:
            md[el]=1
        else:
            md[el]+=1
    return md

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('fname', help='name of txt file')
    parser.add_argument('-number', type=int, help='number of pairs')
    args = parser.parse_args()
    return args

def main():
    args=arguments()

    try:
        with open(args.fname, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("file not found")

    words=clean(text)
    diction=count(words)
    sort_words=sorted(diction.items(), key=lambda x: x[1], reverse=True)

    print("most frequent words:\n")
    for w, c in sort_words[:args.number]:
        print(f"{w} : {c}")

if __name__=="__main__":
    main()