# 🧠 Voice ChatGPT Interface (Fullstack Test Project)

Веб-приложение с возможностью текстового и голосового взаимодействия с LLM (ChatGPT/OpenAI или локальной Ollama-моделью).

## 🚀 Стек технологий

### 🔹 Frontend
- **Vue 3 (Composition API)** — фреймворк для SPA.
- **Vanilla CSS** + кастомная стилизация с элементами Tailwind-подхода.
- **Web Speech API** — голосовой ввод (Speech-to-Text).

### 🔹 Backend
- **Python 3.13**
- **Django** — веб-фреймворк.
- **Django REST Framework (DRF)** — API-слой.
- **Ollama API** — подключение к локальной LLM-модели (`gemma3:1b`).
- **OpenAI API** — взаимодействие с GPT-4 или GPT-3.5 через OpenAI SDK `>=1.0.0`.

---

## 🖥️ Функциональность

- ✅ Ввод текста пользователем и отправка запроса к LLM.
- ✅ Получение и отображение ответа от модели.
- ✅ Выбор модели: **локальная (Ollama)** или **облачная (OpenAI)**.
- ✅ (Усложненный вариант) Голосовой ввод через кнопку микрофона.
- ✅ Обработка ошибок и индикатор загрузки.

---

# 📦 Установка и запуск

# Backend (Django)

##### Перейти в папку backend:
cd backend

##### Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate

##### Установка зависимостей
pip install -r requirements.txt

##### Запуск сервера
python manage.py runserver

# Frontend

##### Перейти в папку frontend:
cd frontend

##### Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate

##### Установка зависимостей
npm install

##### Запуск dev-сервер
npm run dev

---

# Структура проекта