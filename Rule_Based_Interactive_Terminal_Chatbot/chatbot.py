import json
import re
from pathlib import Path

# Dataset location
BASE_DIR = Path(__file__).resolve().parent
FAQ_FILE = BASE_DIR / "sample_faq.json"

# Exit commands
EXIT_COMMANDS = {"bye", "exit", "quit"}

# Intent recognition rules
INTENT_PATTERNS = {
    "business_hours": [
        r"\b(hours?|timings?|working hours?|office hours?)\b",
        r"\b(when are you open|when do you open|when do you close)\b",
        r"\bworking days?\b"
    ],

    "project_submission": [
        r"\b(submit|submission|upload)\b.*\b(project|internship|github|repository)\b",
        r"\b(project|internship|github|repository)\b.*\b(submit|submission|upload)\b",
        r"\b(student workspace|public github)\b"
    ],

    "certificate": [
        r"\b(certificate|certification)\b",
        r"\b(code review|reviewed)\b"
    ]
}


class RuleBasedChatbot:

    def __init__(self):
        self.greetings = []
        self.faqs = []
        self.load_dataset()

    # Load JSON dataset
    def load_dataset(self):
        try:
            with open(FAQ_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("JSON root must be an object.")

            greetings = data.get("greetings", [])
            faqs = data.get("faqs", [])

            if not isinstance(greetings, list):
                raise ValueError("Greetings must be a list.")

            if not isinstance(faqs, list):
                raise ValueError("FAQs must be a list.")

            self.greetings = [
                item.lower().strip()
                for item in greetings
                if isinstance(item, str)
            ]

            self.faqs = [
                item for item in faqs
                if isinstance(item, dict)
                and isinstance(item.get("question"), str)
                and isinstance(item.get("answer"), str)
            ]

            if not self.faqs:
                raise ValueError("No valid FAQs found.")

        except FileNotFoundError:
            raise FileNotFoundError(
                "sample_faq.json not found. "
                "Keep it in the same folder as chatbot.py."
            )

        except json.JSONDecodeError as error:
            raise ValueError(f"Invalid JSON file: {error}")

    # Normalize user input
    def normalize_text(self, text):
        return re.sub(r"\s+", " ", text.lower().strip())

    # Greeting recognition
    def is_greeting(self, text):
        for greeting in self.greetings:
            pattern = rf"\b{re.escape(greeting)}\b"

            if re.search(pattern, text):
                return True

        return False

    # Multi-intent recognition
    def detect_intents(self, text):
        matched_intents = []

        for intent, patterns in INTENT_PATTERNS.items():

            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    matched_intents.append(intent)
                    break

        return matched_intents

    # Retrieve FAQ answer from JSON
    def get_faq_answer(self, intent):

        question_keywords = {
            "business_hours": [
                "hours of operation", "hours"
            ],

            "project_submission": [
                "submit my internship project",
                "internship project"
            ],

            "certificate": [
                "receive my certificate",
                "certificate"
            ]
        }

        keywords = question_keywords.get(intent, [])

        for faq in self.faqs:
            question = faq["question"].lower()

            if any(word in question for word in keywords):
                return faq["answer"]

        return None

    # Generate chatbot response
    def generate_response(self, user_input):

        text = self.normalize_text(user_input)

        if not text:
            return "Please enter a question."

        greeting = self.is_greeting(text)

        if greeting:
            greeting_message = (
                "Hello! Welcome to customer support. "
                "How can I help you?"
            )
        else:
            greeting_message = None

        # Detect all matching intents
        intents = self.detect_intents(text)

        responses = []

        for intent in intents:
            answer = self.get_faq_answer(intent)

            if answer:
                responses.append(answer)

        # Return multiple answers when multiple intents match
        if responses:

            if greeting_message:
                return greeting_message + "\n\n" + "\n\n".join(responses)

            return "\n\n".join(responses)

        if greeting_message:
            return greeting_message

        # Fallback response
        return (
            "Sorry, I couldn't understand your question.\n"
            "You can ask about:\n"
            "1. Business hours\n"
            "2. Internship project submission\n"
            "3. Certificate status"
        )

    # Interactive chatbot
    def run(self):

        print("=" * 55)
        print("     RULE-BASED CUSTOMER SUPPORT CHATBOT")
        print("=" * 55)

        print("Bot: Hello! I am your support assistant.")
        print("Bot: How can I help you?")
        print("Bot: Type bye, exit, or quit to stop.")
        print("-" * 55)

        while True:

            try:
                user_input = input("You: ").strip()

                # Exit handling
                if self.normalize_text(user_input) in EXIT_COMMANDS:
                    print("Bot: Thank you for contacting us. Goodbye!")
                    break

                response = self.generate_response(user_input)

                print("Bot:", response)

            except KeyboardInterrupt:
                print("\nBot: Conversation interrupted. Goodbye!")
                break

            except EOFError:
                print("\nBot: Input closed. Goodbye!")
                break

            except Exception as error:
                print("Bot: Unexpected error:", error)


# Main function
def main():

    try:
        chatbot = RuleBasedChatbot()
        chatbot.run()

    except (FileNotFoundError, ValueError) as error:
        print("Startup Error:", error)


if __name__ == "__main__":
    main()