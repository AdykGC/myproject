<h1 align="center">LLM-Powered Voice Chat Interface (Fullstack Project)
<h3 align="center"></h3>


Веб-приложение с возможностью текстового и голосового взаимодействия с LLM (ChatGPT/OpenAI или локальной Ollama-моделью).

## Стек технологий

<!--Блок информации о репозитории в бейджах-->
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![CORS](https://img.shields.io/badge/CORS-enabled-blue?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-264de4?style=for-the-badge&logo=css3&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--Turbo-10a37f?style=for-the-badge&logo=openai&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Gemma3--1B-5c5c5c?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

### Frontend:
`JavaScript`
`Vue.js`
`Vite`
`CSS`
`Web Speech API`

### Backend:
`Python`
`Django`
`Django REST Framework (DRF)`
`Cross-Origin Resource Sharing (CORS) : django-cors-headers`

### Database:
`Sqlite3`

### LLM-модели:
`Ollama API: gemma3:1b`
`OpenAI API: gpt-3.5-turbo`

---

## 🖥️ Функциональность

- ✅ Ввод текста пользователем и отправка запроса к LLM.
- ✅ Получение и отображение ответа от модели.
- ✅ Выбор модели: **локальная (Ollama)** или **облачная (OpenAI)**.
- ✅ (Усложненный вариант) Голосовой ввод через кнопку микрофона.
- ✅ Обработка ошибок и индикатор загрузки.

---

# Установка и запуск

1. Клонирование репозитория

```git clone https://github.com/AdykGC/myproject.git```

2. Переход в директорию IDK

```cd myproject```

3. Создание виртуального окружения

```python3 -m venv venv```

4. Backend | Перейти в папку

```cd backend```

4. Frontend | Перейти в папку

```cd frontend```

5. Frontend | Активация виртуального окружения

```python3 -m venv venv```

```source venv/bin/activate```

5. Frontend | Активация виртуального окружения

```python3 -m venv venv```

```source venv/bin/activate```

6. Backend | Установка зависимостей

```pip3 install -r requirements.txt```

6. Frontend | Установка зависимостей

```npm install```

7. Backend | Запуск сервера

```python3 manage.py runserver```

7.  Frontend | Запуск dev-сервер

```npm run dev```

---

# Структура проекта