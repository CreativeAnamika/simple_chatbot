import google.generativeai as genai


def load_system_prompt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def get_gemini_chat():
    genai.configure(api_key="AIzaSyCnrpz3NKaFVdjEDSpIjBpSzXg1fPHIs3w")
#AIzaSyDTxGI3fpRjHCrXlLTyyixQq46DTsOkQ4s
    prompt = load_system_prompt("chatbot_app/prompts/system_prompt.txt")

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-8b",
        system_instruction=prompt
    )

    return model.start_chat(history=[])
