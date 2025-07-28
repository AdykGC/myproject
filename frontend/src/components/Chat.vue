<template>
  <section class="cta-section">
    <div class="container">
      <div class="cta-box">
        <div class="row">
          <div class="col left">
            <h2 class="heading"><span>Hi there!</span></h2>
            <h1 class="heading"><span>What would you like to know?</span></h1>
            <h4 class="heading">
              <span>Use one of the most common prompts below or ask your own question</span>
            </h4>

            <input
              v-model="message"
              type="text"
              class="input"
              placeholder="Type your question here..."
            />
            <p v-if="reply" class="reply">🤖 {{ reply }}</p>
          </div>

          <div class="col left">
            <button @click="askQuestion" :disabled="loading">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="#fff" viewBox="0 0 256 256">
                <path d="M80,128V64a48,48,0,0,1,96,0v64a48,48,0,0,1-96,0Zm128,0a8,8,0,0,0-16,0,64,64,0,0,1-128,0,8,8,0,0,0-16,0,80.11,80.11,0,0,0,72,79.6V240a8,8,0,0,0,16,0V207.6A80.11,80.11,0,0,0,208,128Z"></path>
              </svg>
              {{ loading ? 'Asking...' : 'Ask whatever you want' }}
              <span>
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="#fff" viewBox="0 0 256 256">
                  <path d="M48,80v96a8,8,0,0,1-16,0V80a8,8,0,0,1,16,0Zm189.66,42.34-96-96A8,8,0,0,0,128,32V72H72a8,8,0,0,0-8,8v96a8,8,0,0,0,8,8h56v40a8,8,0,0,0,13.66,5.66l96-96A8,8,0,0,0,237.66,122.34Z"></path>
                </svg>
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      message: '',
      reply: '',
      loading: false,
    };
  },
  methods: {
    async askQuestion() {
      if (!this.message.trim()) return;

      this.loading = true;
      try {
        const res = await fetch('http://localhost:8000/api/chat/ollama/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
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
  },
};
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
