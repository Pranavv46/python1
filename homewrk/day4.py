web_dev = ["Arjun", "Neha", "Ravi"]
data_sci = ["Kiran", "Meera", "Sahil"]
ui_ux = ["Tina", "Rahul", "Asha"]

all_participants=[web_dev,data_sci,ui_ux]

web_dev.append("divya")
data_sci.insert(1,"vikram")
ui_ux.pop()

data_sci_copy= data_sci.copy()
data_sci.clear

print("First two Web Dev participants:", web_dev[:2])
name_lengths = [len(name) for name in data_sci_copy]
print("Name lengths (Data Science):", name_lengths)
is_asha_present = "Asha" in web_dev or "Asha" in data_sci_copy or "Asha" in ui_ux
print("Is Asha in any workshop?", is_asha_present)
first_participants = (web_dev[0], data_sci_copy[0], ui_ux[0])
print("First participant from each workshop:", first_participants)
print("\n--- Final Workshop Lists ---")
print("Web Development:", web_dev)
print("Data Science (copied):", data_sci_copy)
print("UI/UX Design:", ui_ux)