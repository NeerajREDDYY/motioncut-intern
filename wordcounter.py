import re

# Function to count the number of words in a sentence or paragraph
def count_words(text):
    # Remove punctuation and split the text into words
    words = re.findall(r'\b\w+\b', text)
    # Return the number of words
    return len(words)

# Function to get user input and handle empty input
def get_user_input():
    while True:
        user_input = input("Please enter a sentence or paragraph to count the words (or 'exit' to finish): ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            exit(0)
        elif user_input.strip() == '':
            print("No input provided. Please enter some text.")
        else:
            return user_input

# Main function to run the word counter program
def main():
    while True:
        try:
            # Get user input
            text = get_user_input()
            # Count the words using the count_words function
            word_count = count_words(text)
            # Display the word count
            print(f"The number of words in your text is: {word_count}")
        except Exception as e:
            # Handle any unexpected errors
            print(f"An unexpected error occurred: {e}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()