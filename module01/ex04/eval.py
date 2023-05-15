class Evaluator:

    # Zip : Retourne une tuple avec les deux elements stockes + un .next(),
    # qui permet de passer au tuple suivant.
    def zip_evaluate(coefs: 'list[float]', words: 'list[str]') -> float:
        if len(coefs) != len(words):
            return -1.0
        ret: float = 0.0
        for item in zip(coefs, words):
            ret += float(len(item[1]) * item[0])
        return ret

    # Enumerate : Retourne un objet iterable qui se fait yield
    def enumerate_evaluate(coefs: 'list[float]', words: 'list[str]'):
        if (len(coefs) != len(words)):
            print("Error: coefs and words must have the same length.")
            return -1.0
        ret: float = 0.0
        for index, word in enumerate(words):
            ret += float(len(word) * coefs[index])
        return ret


if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    ret = Evaluator.zip_evaluate(coefs, words)
    print(ret)

    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42, 2.0]
    ret = Evaluator.enumerate_evaluate(coefs, words)
    print(ret)
