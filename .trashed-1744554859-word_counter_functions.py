def get_sentence_input() -> str:
    
    return input("Enter a sentence: ").strip()

def count_words(sentence: str) -> int:
  
    return len(sentence.split())

if __name__ == "__main__":
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} {'word' if word_count == 1 else 'words'}.")
