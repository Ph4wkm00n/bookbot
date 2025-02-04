def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    # print(text)
    word_count = count_words(book_text)
    # print("Word count:", word_count)

    counts = count_alpha_chars(book_text)
    """
    print("Character counts:")
    for char, count in counts.items():
        # Use repr(char) to clearly show spaces and special characters.
        print(f"{repr(char)}: {count}")
    """
# Print the report
    print("Report:")
    print("Total words:", word_count)
    print("Alphabet character counts:")
    
    # Sort keys alphabetically for a neat report
    for char in sorted(counts.keys()):
        print(f"The '{char}'character was found {counts[char]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    
    #Counts the number of words in the given text.
    # Split the text by whitespace and count the resulting parts.
    words = text.split()
    return len(words)

def count_alpha_chars(book_text): 
    
    #Counts the frequency of each character in the given text.
    # Initialize an empty dictionary to store character counts.
    char_count = {}
    
    # Convert the entire text to lowercase and iterate through each character.
    for char in book_text.lower():
        
        if char.isalpha():  # Only count alphabet characters
            char_count[char] = char_count.get(char, 0) + 1
    
    return char_count



main()
