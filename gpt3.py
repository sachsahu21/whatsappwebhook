import openai

# Set your OpenAI API key here (replace 'YOUR_API_KEY' with your actual API key)
openai.api_key  = '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'

def get_chat_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # You can choose different engines based on your plan
            prompt=prompt,
            max_tokens=150  # Adjust the response length as needed
        )
        return response['choices'][0]['text'].strip()
    except openai.error.OpenAIError as e:
        # Handle errors
        print("Error:", e)
        return None

if __name__ == "__main__":
    # while True:
        # user_input = input("You: ")
        user_input = 'Who are you'
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            # break

        chat_prompt = f"You said: {user_input}\nChatGPT: "
        response = get_chat_response(chat_prompt)
        print("ChatGPT:", response)
