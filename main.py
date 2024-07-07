def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        split = text.lower().split()
        # Start a dict with keys for each word
        word_count = {}
        for word in split:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        top_10_common_words = sorted(word_count, key=word_count.get, reverse=True)[:10]
        
        print("The top 10 most common words are:")
        for word in top_10_common_words:
            print(f"'{word}' has been used {word_count[word]} times.")

if __name__ == "__main__":
    main()