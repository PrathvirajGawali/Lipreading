def get_kannada_translation(english_text):
    translations = {
        "Hello": "ನಮಸ್ಕಾರ",
        "Stop navigation.": "ನ್ಯಾವಿಗೇಶನ್ ನಿಲ್ಲಿಸಿ.",
        "I am sorry.": "ಕ್ಷಮಿಸಿ.",
        "Thank you.": "ಧನ್ಯವಾದಗಳು.",
        "Good bye.": "ವಿದಾಯ.",
        "Nice to meet you.": "ನಿಮ್ಮನ್ನು ಭೇಟಿ ಮಾಡಿದ್ದು ಸಂತೋಷ.",
        "How are you?": "ನೀವು ಹೇಗಿದ್ದೀರಾ?",
        "Begin": "ಆರಂಭಿಸಿ",
        "Choose": "ಆಯ್ಕೆಮಾಡಿ",
        "Connection": "ಸಂಪರ್ಕ",
        "Navigation": "ನ್ಯಾವಿಗೇಶನ್",
        "Next": "ಮುಂದೆ",
        "Previous": "ಹಿಂದೆ",
        "Start": "ಪ್ರಾರಂಭಿಸಿ",
        "Stop": "ನಿಲ್ಲಿಸಿ",
        "Well": "ಚೆನ್ನಾಗಿದ್ದಾರೆ",
        "I love this game.": "ನಾನು ಈ ಆಟವನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ.",
        "You are welcome.": "ಸ್ವಾಗತ",
        "Have a good time.": "ಉತ್ತಮ ಸಮಯವನ್ನು ಕಳೆಯಿರಿ."
    }
    return translations.get(english_text, "ಅನುವಾದ ಲಭ್ಯವಿಲ್ಲ")
