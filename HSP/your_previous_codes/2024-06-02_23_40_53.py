import requests

# Replace with your Wit.ai server access token
wit_ai_token = 'NW52QVIPIDIW2AUOWM2CMN7GOWZXY43Z'
headers = {
    'Authorization': f'Bearer {wit_ai_token}',
    'Content-Type': 'application/json'
}

def get_response(message):
    url = 'https://api.wit.ai/message'
    params = {
        'v': '20230301',
        'q': message
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

def parse_response(response):
    if 'intents' in response and response['intents']:
        intent = response['intents'][0]['name']
        entities = response['entities']
        return f"Intent: {intent}, Entities: {entities}"
    else:
        return "I couldn't understand that. Could you rephrase?"

print("Hello, I am your Wit.ai chatbot. How can I help you today?")

while True:
    try:
        # Get user input
        user_input = input("You: ")

        # Get the bot's response from Wit.ai
        response = get_response(user_input)
        
        # Parse and print the bot's response
        bot_response = parse_response(response)
        print(f"Bot: {bot_response}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
