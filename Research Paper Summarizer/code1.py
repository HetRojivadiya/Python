import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci",  # Use the "davinci" engine
        prompt=prompt,
        max_tokens=50,  # Control the length of the response
        temperature=0.7,  # Adjust the randomness of the output
    )
    return response.choices[0].text.strip()

def main():
    print("ChatGPT: Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("ChatGPT: Goodbye!")
            break
        
        prompt = f"You: {user_input}\nChatGPT:"
        response = chat_with_gpt(prompt)
        
        print(f"ChatGPT: {response}")

if __name__ == "__main__":
    main()
