def tokenize_test(Ls):

    """
    Tokenize uma lista de sentenças e \
    faz print a primeira palavra dessa \
    sentença tokenize

    :param ls: lista de sentenças
    """

    for sentence in Ls:
        temo_text = sentence.split()
        print(temo_text[0])


DEBUG = False

if __name__ == "__main__":
    
    if DEBUG:

        ls_text = ["ESTUDO.dev é uma iniciativa estudantil auto didata"]
        tokenize_test(ls_text)
