import requests
import socket
from tkinter import *
import datetime
from textblob import TextBlob
import wikipedia
import psutil
import webbrowser

# Create the main application window
frame = Tk()
frame.geometry("800x600")
frame.title("procameo AI")
frame.configure(bg="#1f1f1f")

# Create a bounding box for the user and AI labels
label_box = Frame(frame, bg="#2c2c2c", bd=2, relief="groove")
label_box.grid(row=1, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

Label(label_box, text="User", font=("Helvetica", 16, "bold"), fg="#b0b0b0", bg="#2c2c2c").grid(row=1, column=1, padx=10, pady=10, sticky="w")
Label(label_box, text=" procameo AI", font=("Helvetica", 16, "bold"), fg="#b0b0b0", bg="#2c2c2c").grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Create a bounding box for user input and AI response
user_ai_frame = Frame(frame, bg="#2c2c2c", bd=2, relief="groove")
user_ai_frame.grid(row=1, column=2, rowspan=2, padx=10, pady=10, sticky="nsew")

userentry = Entry(user_ai_frame, fg="#ffffff", font=("Helvetica", 12), bg="#2c2c2c")
userentry.pack(fill="x", padx=10, pady=(10, 0))

AIentry = Text(user_ai_frame, wrap=WORD, width=50, height=10, fg="#ffffff", font=("Helvetica", 12), bg="#2c2c2c")
AIentry.pack(fill="both", expand=True, padx=10, pady=(0, 10))

AIscrollbar = Scrollbar(user_ai_frame, command=AIentry.yview)
AIscrollbar.pack(side="right", fill="y")
AIentry.config(yscrollcommand=AIscrollbar.set)
def fetch_weather():
    api_key = '80e2b44771a85fd6741a1a1845f11d6c'
    city = 'mumbai'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(weather_url)
    weather_data = response.json()

    weather_description = weather_data['weather'][0]['description']
    return f"The weather in {city} is currently {weather_description}."

def fetch_temperature():
    api_key = '80e2b44771a85fd6741a1a1845f11d6c'
    city = 'mumbai'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(weather_url)
    weather_data = response.json()

    temperature = weather_data['main']['temp']
    

    return temperature


def perform_google_search(query):
    google_api_key = 'AIzaSyBsQKBB7Obluka-lRV_-m4j1aJkvaSDR2g'
    search_engine_id = 'cx=b3896f183f3e04cbe'
    search_url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={google_api_key}&{search_engine_id}'
    
    response = requests.get(search_url)
    search_results = response.json().get('items', [])

    if search_results:
        result_text = ""
        for result in search_results:
            title = result.get('title', 'No Title')
            link = result.get('link', 'No Link')
            result_text += f"{title}: {link}\n"
        return result_text
    else:
        return "Sorry, I couldn't find any relevant information."

def perform_wikipedia_search(query):
    try:
        search_result = wikipedia.summary(query, sentences=2)
        return search_result
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]
        return f"The search query is ambiguous. Here are some possible options: {', '.join(options)}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any relevant information on Wikipedia."



# Define the function to process user input
def process_user_input(user_input):
    sentiment = TextBlob(user_input).sentiment.polarity
    greetings = ['hi', 'hello']

    if user_input.lower() in greetings:
        ai_response = "Hello, how can I assist you today?"

    # ... Other query checks ...

    elif sentiment > 0.2:  # Positive sentiment
        ai_response = "I'm glad to hear that!"
    elif sentiment < -0.2:  # Negative sentiment
        ai_response = "I'm sorry to hear that. Is there something I can do to help?"
    else:
        ai_response = "I'm here to assist you!"

    return ai_response

def get_vals():
    user_input = userentry.get()
    print(f"User entered: {user_input}")
    

    # Write the user input to the "records.txt" file
    with open("records.txt", "w") as f:
        f.write(user_input)

    greetings = ['hi', 'hello']
    
    ai_response = ""

    if user_input.lower().startswith('open '):
        website = user_input[5:]
        try:
            url = f"https://{website}"
            webbrowser.open(url)
            ai_response = f"Opening {website}."
        except Exception as e:
            ai_response = f"An error occurred: {e}"
    elif user_input.lower() in greetings:
        ai_response = "Hello, how can I assist you today."
    elif user_input.lower() == 'bye':
        ai_response = "Goodbye! Have a great day."
    elif user_input.lower() == 'weather':
        ai_response = fetch_weather()
    elif user_input.lower() == 'time':
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        ai_response = f"The current time is: {current_time}"
    elif user_input.lower() == 'date':
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        ai_response = f"Today's date is: {current_date}"
    elif user_input.lower().startswith("how to") or user_input.lower().startswith("how is"):
        query = user_input[8:]
        ai_response = perform_google_search(query)

    elif user_input.lower() == 'battery':
        battery = psutil.sensors_battery()
        percentage = battery.percent if battery else "Unknown"
        ai_response = f"The current battery percentage is: {percentage}%"
    elif user_input.lower() == 'temperature':
        temperature = fetch_temperature()
        ai_response = f"The current temperature is: {temperature}°C"
    elif user_input.lower().startswith('what to '):
        query = user_input[8:]
        ai_response = perform_google_search(query)
    elif user_input.lower().startswith('what is'):
        query = user_input[8:]
        ai_response = perform_wikipedia_search(user_input)
    elif user_input.lower().startswith('how is '):
        query = user_input[8:]
        ai_response = perform_google_search(query)
    elif 'who' in user_input.lower():
        query_start = user_input.lower().find('who') + len('who')
        query = user_input[query_start:].strip()
        ai_response = perform_google_search(query)
    elif user_input.lower().startswith('location'):
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']
        print(city)
    else:
        ai_response = "I'm sorry, I don't have information on that at the moment."

    # Check for internet connectivity
    try:
        socket.create_connection(("www.google.com", 80))
        internet_connected = True
    except OSError:
        internet_connected = False

    if not internet_connected:
        ai_response = "Please connect to the internet to use this feature."

    # Set the value of AIentry to display the AI response
    AIentry.delete(1.0, END)
    AIentry.insert(END, ai_response)

# Create a clear button to clear the AI response
def clear_response():
    AIentry.delete(1.0, END)

clear_button = Button(frame, text="Clear", command=clear_response, bg="#3f3f3f", fg="#ffffff", font=("Helvetica", 14, "bold"))
clear_button.grid(row=3, column=1, pady=10)

# Create a stylish submit button
submit_button = Button(frame, text="Submit", command=get_vals, bg="#3f3f3f", fg="#ffffff", font=("Helvetica", 14, "bold"))
submit_button.grid(row=3, column=2, pady=10)

# Configure row and column weights for proper resizing
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

# Start the Tkinter main loop
frame.mainloop()
