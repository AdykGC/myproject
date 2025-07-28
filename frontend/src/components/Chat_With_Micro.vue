<template>
  <section class="cta-section">
    <div class="container">
      <div class="cta-box">
        <div class="row">
          <Part_1 />
          <Part_2 />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import Part_1 from './Section_Chat_AI/col-left-text.vue'
import Part_2 from './Section_Chat_AI/col-left-IO.vue'
</script>

<script>
//    export default {
//      data() {
//        return {
//          message: '',
//          reply: '',
//          loading: false,
//          recognizing: false,
//          recognition: null,
//          selectedModel: 'ollama', // по умолчанию
//        };
//      },
//      mounted() {
//      if ('webkitSpeechRecognition' in window) {
//        this.recognition = new webkitSpeechRecognition();
//        this.recognition.lang = 'ru-RU';
//        this.recognition.continuous = true;
//        this.recognition.interimResults = true;
  //    
//        this.recognition.onresult = (event) => {
//          let finalTranscript = '';
//          for (let i = event.resultIndex; i < event.results.length; ++i) {
//            if (event.results[i].isFinal) {
//              finalTranscript += event.results[i][0].transcript;
//            }
//          }
//          if (finalTranscript.trim() !== '') {
//            this.message = finalTranscript.trim();
//            this.recognizing = false;
//            this.recognition.stop(); // останавливаем распознавание
//            this.askQuestion();      // отправляем только финальный текст
//          }
//        };
  //    
//        // this.recognition.onspeechend = () => {
//        //  this.recognition.stop();
//        //  this.recognizing = false;
//        // };
  //    
//        this.recognition.onerror = (event) => {
//          console.error('Speech recognition error', event);
//          this.recognizing = false;
//          if (event.error === 'no-speech') {
//            alert('🎤 Ничего не услышано. Попробуйте сказать что-то вслух.');
//          } else {
//            alert(`⚠️ Ошибка распознавания: ${event.error}`);
//          }
//        };
  //    
//        this.recognition.onend = () => {
//          this.recognizing = false;
//        };
//      } else {
//        alert('Ваш браузер не поддерживает распознавание речи.');
//      }
//    },
//      methods: {
//        async askQuestion() {
//          if (!this.message.trim()) return;
    //    
//          this.loading = true;
//          console.log(`📤 Отправляем (${this.selectedModel}):`, this.message);
//          let url = 'http://localhost:8000/api/chat/ollama/';
//          if (this.selectedModel === 'openai') {
//            url = 'http://localhost:8000/api/chat/openai/';
//          }
//          try {
//            const res = await fetch(url, {
//              method: 'POST',
//              headers: { 'Content-Type': 'application/json' },
//              body: JSON.stringify({ message: this.message }),
//            });
//            const data = await res.json();
//            this.reply = data.reply || '⚠️ No response received.';
//          } catch (error) {
//            this.reply = '⚠️ Error: ' + error.message;
//          } finally {
//            this.loading = false;
//          }
//        },
//        startRecognition() {
//          if (this.recognition) {
//            if (!this.recognizing) {
//              this.recognizing = true;
//              this.recognition.start();
//            } else {
//              this.recognizing = false;
//              this.recognition.stop();
//            }
//          }
//        },
//      },
//    };
</script>


<style scoped>
.cta-section {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  padding: 80px 0;
  background-color: #ffffff;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 16px;
}
.cta-box {
  position: relative;
  background-color: #04004b; /* bg-primary */
  border-radius: 8px;
  padding: 70px;
  overflow: hidden;
  z-index: 1;
}
.row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 20px;
}
.col {
  flex: 1 1 50%;
  padding: 16px;
}
.left {
  display: flex;
  flex-direction: column; /* расположить элементы вертикально */
  justify-content: flex-start;
  align-items: flex-start; /* выравнивание по левому краю */
  gap: 16px; /* расстояние между заголовками */
}

.right {
  display: flex;
  justify-content: flex-end;
  gap: 16px;
  flex-wrap: wrap;
}
.subheading {
  display: block;
  margin-bottom: 16px;
  font-size: 16px;
  font-weight: 500;
  color: white;
}
.heading {
  margin: 0;
  font-weight: bold;
  color: white;
  line-height: 1.2;
}
.heading + .heading {
  margin-top: 10px;
}
.btn {
  padding: 12px 28px;
  font-size: 16px;
  font-weight: 500;
  border-radius: 6px;
  text-decoration: none;
  transition: all 0.3s ease;
}
.btn-light {
  background-color: #ffffff;
  color: #4f46e5;
}
.btn-light:hover {
  background-color: #f3f4f6;
}
.btn-dark {
  background-color: #ec4899;
  color: white;
}
.btn-dark:hover {
  opacity: 0.9;
}
.bg-svg {
  position: absolute;
  z-index: -1;
}
.top-left {
  top: 0;
  left: 0;
}
.bottom-right {
  bottom: 0;
  right: 0;
}
</style>

<style scoped>
  button {
    max-width: 520px;
    min-width: 320px;
    display: flex;
    overflow: hidden;
    position: relative;
    padding: 0.875rem 72px 0.875rem 1.75rem;
    background-color: #039be5;
    background-image: linear-gradient(to top right, #039be5, #29b6f6);
    color: #ffffff;
    font-size: 15px;
    white-space: nowrap;
    line-height: 1.25rem;
    font-weight: 700;
    text-align: center;
    cursor: pointer;
    vertical-align: middle;
    align-items: center;
    border-radius: 0.5rem;;
    gap: 0.75rem;
    box-shadow:
    0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);
    border: 2px solid #ffffff; /* Темный бордер */
    transition: all 0.6s ease;
  }

  button span {
    background-color: rgb(3 155 229);
    display: grid;
    position: absolute;
    right: 0;
    place-items: center;
    width: 3rem;
    height: 100%;
  }

  button span svg {
    width: 1.5rem;
    height: 1.5rem;
  }

  button:hover {
    box-shadow:
      0 4px 30px rgba(4, 176, 255, 0.419),
      0 2px 30px rgba(11, 157, 255, 0.419);
      border-color: #000000; /* Темный бордер при hover */
  }


.input {
  width: 100%;
  max-width: 480px;
  padding: 12px 16px;
  font-size: 16px;
  margin-top: 16px;
  border: 2px solid #ffffff;
  border-radius: 8px;
  outline: none;
}
.reply {
  margin-top: 20px;
  background-color: #ffffff;
  color: #000000;
  padding: 12px 16px;
  border-radius: 8px;
  max-width: 480px;
}
</style>
