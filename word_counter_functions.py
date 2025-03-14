def get_sentence_input() -> str:
    
    return input("Enter a sentence: ").strip()

def count_words(text: str) -> int:
   
    return len(text.split())

def main():
    
    user_sentence = get_sentence_input()
    word_count = count_words(user_sentence)
    print(f"The sentence contains {word_count} {'word' if word_count == 1 else 'words'}.")

if __name__ == "__main__":
    main()
