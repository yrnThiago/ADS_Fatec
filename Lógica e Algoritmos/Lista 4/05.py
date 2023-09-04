def palavra_eh_valida(palavra: str) -> bool:
    if palavra.isalnum() and len(palavra) > 4:
        for letra in letras_selecionadas:
            if letra in palavra: return True
            
        return False

letras_selecionadas = 'python'
palavras = """
The Python Software Foundation and the global Python community welcome and encourage participation by everyone. 
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. 
We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.""".lower().split()

palavras_filtradas = [p for p in palavras if palavra_eh_valida(p)]
print(len(palavras_filtradas))

