from translate import Translator

def translate_to_arabic(text: str) -> str:
    try:
        # Initialize the translator for English to Arabic
        translator = Translator(to_lang="ar")
        # Perform the translation
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        raise RuntimeError(f"Translation failed: {str(e)}")
