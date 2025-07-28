# python '/Users/adilkhanaltynbek/Desktop/CODE/Experimental_project_2/myproject/backend/backend/Test_Ollama.py'
import ollama

def main():
    try:
        response = ollama.chat(
            model='gemma3:1b',
            messages=[
                {"role": "user", "content": "Привет, расскажи интересный факт о космосе."}
            ]
        )
        print("Ответ от модели:")
        print(response['message']['content'])
    except Exception as e:
        print("❌ Ошибка при обращении к модели Ollama:", e)

if __name__ == "__main__":
    main()
