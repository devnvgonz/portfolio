def annograms(word):
    try:
        # Lee el archivo 
        with open('WORD.LST', 'r') as f:
            words = [w.strip() for w in f.readlines()]
        
        # Busca anagramas comparando las palabras 
        anagrams = [w for w in words if sorted(w) == sorted(word) and w != word]
        return anagrams
    
    except FileNotFoundError:
        return "El archivo WORD.LST no fue encontrado"
    except Exception as e:
        return f"Ocurrió un error: {e}"



if __name__ == "__main__":
    palabra = input("Ingresa una palabra para encontrar sus anagramas: ")
    resultado = annograms(palabra)
    print("Anagramas encontrados:", resultado)
