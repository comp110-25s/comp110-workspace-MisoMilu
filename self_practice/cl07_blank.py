"""One shot wordle"""


def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    # TODO 1
    if len(word) != len(secret):
        print("Words are different lengths.")
        return False
    # TODO 2
    if idx < len(secret):
        if word[idx] != secret[idx]:
            print(f"{word[idx]}isnt the secret word's next letter.")
            return False
        else:
            print(
                f"{word[idx]} is at idex{idx} for both words! Checking next letters..."
            )  # check from each index until they are true

        return guess_secret(word=word, secret=secret, idx=idx + 1)

    # TODO 3
    print("They are the same word!")
    return True

    # add a input function
