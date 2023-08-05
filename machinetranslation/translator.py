from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    try:
        french_text = MyMemoryTranslator(source="english", target="french").translate(english_text)
        return french_text
    except Exception as translation_error:
        print(f"Translation Error: {translation_error}")
        return ""


def french_to_english(french_text):
    try:
        english_text = MyMemoryTranslator(source="french", target="english").translate(french_text)
        return english_text
    except Exception as translation_error:
        print(f"Translation Error: {translation_error}")
        return ""

if __name__ == "__main__":
    print(english_to_french("Hello, world!"))
    print(french_to_english("Bonjour, le monde!"))