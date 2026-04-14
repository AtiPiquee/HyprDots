# We import the main class
from textual_wizard import Wizard

# We import the input types we want
from textual_wizard.inputs import Integer, Number, Select, Text

# We define our questions in a list
MY_QUESTIONS = [
    Text("name", "What is your name?", placeholder="John Doe", allow_blank=False),
    Select(
        "animal",
        "What is your favourite animal?",
        options=[
            ("I love dogs 🐶", "dog"),
            ("I love cats 😺", "cat"),
            ("Something else...", "other"),
        ],
    ),
    Integer("pet_count", "How many pets do you have?"),
    Number("height", "How tall are you (in meters)", placeholder="1.70"),
]

# We create the wizard and run it,
# getting the user's inputs in the answers dict
wiz = Wizard(MY_QUESTIONS, "MyApp", "Hello")
answers = wiz.run()

print(f"Your name is {answers['name']}.")