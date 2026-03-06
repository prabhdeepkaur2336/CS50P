def main():
    user=input("Enter:")
    print(convert(user))


def convert(text):
    text=text.replace(":)","😇")
    text=text.replace(":(","🙁")
    return text



main()