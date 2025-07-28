<template>
  <div class="col left">
    <label style="color: white; margin-top: 10px;">
      <select v-model="selectedModel" style="margin-left: 10px;">
        <option value="ollama">🖥️ Ollama (локально)</option>
        <option value="openai">☁️ OpenAI (через API)</option>
      </select>
    </label>


    <div class="input-button-wrapper">

      <!-- Кнопка отправки голосового -->
      <button class="BTN-1" @click="startRecognition" :disabled="recognizing">
        <span>
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#205c9d" viewBox="0 0 256 256">
            <path d="M80,128V64a48,48,0,0,1,96,0v64a48,48,0,0,1-96,0Zm128,0a8,8,0,0,0-16,0,64,64,0,0,1-128,0,8,8,0,0,0-16,0,80.11,80.11,0,0,0,72,79.6V240a8,8,0,0,0,16,0V207.6A80.11,80.11,0,0,0,208,128Z"></path>
          </svg>
        </span>
        {{ recognizing ? '' : '' }}
      </button>

      <!-- Инпут для вопроса -->
      <div class="input-wrapper">
        <input v-model="message" type="text" class="input" placeholder="Ask whatever you want" />
      </div>

      <!-- Кнопка отправки вопроса -->
      <button class="BTN-2" @click="askQuestion" :disabled="loading">
        <span>
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#ffffff8c" viewBox="0 0 256 256">
            <path d="M48,80v96a8,8,0,0,1-16,0V80a8,8,0,0,1,16,0Zm189.66,42.34-96-96A8,8,0,0,0,128,32V72H72a8,8,0,0,0-8,8v96a8,8,0,0,0,8,8h56v40a8,8,0,0,0,13.66,5.66l96-96A8,8,0,0,0,237.66,122.34Z"></path>
          </svg>
        </span>
        {{ loading ? '' : '' }}
      </button>
    </div>
    <p v-if="reply" class="reply">🤖 {{ reply }}</p>
  </div>
</template>


<style scoped>
.input-button-wrapper {
  display: flex;
  min-width: 500px;
  max-width: 500px;
  width: 100%;
}

.input-wrapper {
  position: relative;
  flex: 1;
}

.input-wrapper input {
  width: 100%;
  padding: 0.7rem 0.2rem 0.7rem 0.2rem;
  border: 3px solid #1c448f;
  border-left: none;
  border-right: none;
  border-radius: 0 0 0 0;
  box-sizing: border-box;
  font-size: 1.2rem;
  background-color: #04004B;
  color: #ffffff8c;
}
.input-wrapper input::placeholder {
  color: #ffffff8c;
  outline: none;
}
.input-button-wrapper button {
  padding: 0 1rem;
  cursor: pointer;
}

.BTN-1 {
  border: 3px solid #1c448f;
  border-right: none;
  border-radius: 9px 0 0 9px;
  background-color: #04004B;
}
.BTN-2 {
  border: 3px solid #1c448f;
  border-left: none;
  border-radius: 0 9px 9px 0;
  background-color: #266fbd;
}

.input-button-wrapper button:hover {
  background-color: #97deff;
}

.reply {
  margin-top: 20px;
  background-color: #ffffff;
  color: #000000;
  padding: 12px 16px;
  border-radius: 8px;
  max-width: 1000px;
}
</style>


<script>
export default {
  data() {
    return {
      message: '',
      reply: '',
      loading: false,
      recognizing: false,
      recognition: null,
      selectedModel: 'ollama', // по умолчанию
    };
  },
  mounted() {
  if ('webkitSpeechRecognition' in window) {
    this.recognition = new webkitSpeechRecognition();
    this.recognition.lang = 'ru-RU';
    this.recognition.continuous = true;
    this.recognition.interimResults = true;

    this.recognition.onresult = (event) => {
      let finalTranscript = '';
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          finalTranscript += event.results[i][0].transcript;
        }
      }
      if (finalTranscript.trim() !== '') {
        this.message = finalTranscript.trim();
        this.recognizing = false;
        this.recognition.stop(); // останавливаем распознавание
        this.askQuestion();      // отправляем только финальный текст
      }
    };

    // this.recognition.onspeechend = () => {
    //  this.recognition.stop();
    //  this.recognizing = false;
    // };

    this.recognition.onerror = (event) => {
      console.error('Speech recognition error', event);
      this.recognizing = false;
      if (event.error === 'no-speech') {
        alert('🎤 Ничего не услышано. Попробуйте сказать что-то вслух.');
      } else {
        alert(`⚠️ Ошибка распознавания: ${event.error}`);
      }
    };

    this.recognition.onend = () => {
      this.recognizing = false;
    };
  } else {
    alert('Ваш браузер не поддерживает распознавание речи.');
  }
},
  methods: {
    async askQuestion() {
      if (!this.message.trim()) return;

      this.loading = true;
      console.log(`📤 Отправляем (${this.selectedModel}):`, this.message);
      let url = 'http://localhost:8000/api/chat/ollama/';
      if (this.selectedModel === 'openai') {
        url = 'http://localhost:8000/api/chat/openai/';
      }
      try {
        const res = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: this.message }),
        });
        const data = await res.json();
        this.reply = data.reply || '⚠️ No response received.';
      } catch (error) {
        this.reply = '⚠️ Error: ' + error.message;
      } finally {
        this.loading = false;
      }
    },
    startRecognition() {
      if (this.recognition) {
        if (!this.recognizing) {
          this.recognizing = true;
          this.recognition.start();
        } else {
          this.recognizing = false;
          this.recognition.stop();
        }
      }
    },
  },
};
</script>