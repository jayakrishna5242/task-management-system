import streamlit as st
import sys
import os
# Streamlit UI
st.title("🤖 Personal Assistant Chatbot")
st.write("Hello! I am your personal assistant. Let's get started!")

# Step 1: Get user's name first
user_name = st.text_input("What is your name?")

# Only proceed if name is entered
if user_name:
    st.write(f"Hi {user_name}! What would you like me to do today? 😊")

    # Categories after name
    categories = {
        'Book Tickets 🎟': ['Train Ticket', 'Flight Ticket', 'Metro Ticket'],
        'Shopping 🛍': ['Online', 'Offline'],
        'Entertainment 🎧': ['Music', 'Movies'],
        'Food & Delivery 🍕': ['Order Food'],
        'Health & Medicine 💊': ['Order Medicine'],
        'Set Reminders ⏰': ['Set Reminder'],
        'Exit 🚪': ['Bye']
    }

    # Step 2: Choose category
    category = st.selectbox("Choose a category:", list(categories.keys()))

    # Step 3: Based on category, ask next question
    if category:
        action = st.selectbox(f"What would you like to do in {category}?", categories[category])

        # Step 4: If Shopping, ask Online/Offline
        if category == 'Shopping 🛍' and action:
            shop_type = st.radio("Do you want to shop Online 🛒 or Offline 🏬?", ["Online", "Offline"])
            
            if shop_type == "Online":
                product = st.text_input("What type of product are you looking for? (e.g., Clothes, Electronics, Groceries)")
                website = st.selectbox("Which website do you prefer?", ["Amazon", "Flipkart", "Myntra"])
            else:
                city = st.text_input("Which city are you shopping in?")
                store_type = st.text_input("What kind of store are you looking for? (e.g., Clothing, Electronics)")

        # Step 5: Show output on submit
        if st.button("Submit"):
            if category == 'Shopping 🛍':
                if shop_type == "Online" and product and website:
                    output = f"{user_name}, you can shop for *{product}* at [{website}](https://www.{website.lower()}.com/). Happy shopping! 🛍😊"
                elif shop_type == "Offline" and city and store_type:
                    output = f"{user_name}, you can find *{store_type}* stores in *{city}*. Happy shopping! 🏬😊"
                else:
                    output = f"Please provide complete information to proceed with shopping, {user_name}."
            
            elif category == 'Book Tickets 🎟' and action:
                ticket_links = {
                    'Train Ticket': 'https://www.irctc.co.in/',
                    'Flight Ticket': 'https://www.makemytrip.com/',
                    'Metro Ticket': 'https://www.irctc.co.in/'
                }
                output = f"{user_name}, here’s the link to book your {action.lower()}: 🔗 [{action}]({ticket_links[action]})."

            elif category == 'Entertainment 🎧' and action:
                entertainment_links = {
                    'Music': 'https://open.spotify.com/',
                    'Movies': 'https://www.youtube.com/'
                }
                output = f"{user_name}, enjoy {action.lower()} at [{action}]({entertainment_links[action]}). 🎵🎬"

            elif category == 'Food & Delivery 🍕' and action == 'Order Food':
                output = f"{user_name}, order delicious food from:\n- [Swiggy](https://www.swiggy.com/)\n- [Zomato](https://www.zomato.com/) 🍕🍔"

            elif category == 'Health & Medicine 💊' and action == 'Order Medicine':
                output = f"{user_name}, order your medicines online at [MedPlus](https://www.medplusmart.com/). 💊"

            elif category == 'Set Reminders ⏰' and action == 'Set Reminder':
                task = st.text_input("What task should I remind you about?")
                time = st.time_input("At what time?")
                if task and time:
                    output = f"{user_name}, I’ve set a reminder for *{task}* at *{time}* ⏰."
                else:
                    output = "Please enter a task and time to set the reminder."

            elif category == 'Exit 🚪' and action == 'Bye':
                output = f"Goodbye, {user_name}! Have a great day! 😊"

            else:
                output = "Sorry, I didn't understand that. Please choose an option."

            # Show final output
            st.success(output)
