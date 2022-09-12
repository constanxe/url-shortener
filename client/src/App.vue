<template>
  <div id="app">
    <h2>URL Shortener<button class="btn__theme" @click="toggleTheme" title="Toggle theme" aria-label="Toggle theme">{{theme == 'light' ? '🌙' : '☀️'}}</button></h2>
    <div class="label">Let's get started!<br>Insert your URL here.</div>
    <input type="search" v-model="urlInput" @keydown.enter="generateShortenedUrl()"> <button @click="pasteUrlInput()">Paste</button> <br>
    <button @click="generateShortenedUrl()">Shorten</button>

    <div class="result">
      <ShortenedUrlResult :shortenedUrl="shortenedUrl"/>
      <div class="error label" v-html="errorMessage"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ShortenedUrlResult from './components/ShortenedUrlResult.vue'

const serverUrl = 'http://localhost:3000';

export default {
  name: 'App',
  components: {
    ShortenedUrlResult
  },
  data() {
    return {
      urlInput: 'https://blog.gds-gov.tech/terragrunt-in-retro-i-would-have-done-thesefew-things-e5aaac451942',
      shortenedUrl: '',
      errorMessage: '',
      theme: 'light'
    }
  },
  methods: {
    isValidUrl(input) {
      try {
      	return Boolean(new URL(input));
      } catch (error) {
      	return false;
      }
    },

    generateShortenedUrl() {
      this.shortenedUrl = '';

      const url = this.urlInput.trim();
      if (!url) {
        this.errorMessage = 'Please enter a URL';
        return;
      }
      if (!this.isValidUrl(url)) {
        this.errorMessage = 'Please enter a <b>valid</b> URL with http(s) in front';
        return;
      }
      this.errorMessage = '';

      axios.post(serverUrl, {url})
        .then(response => this.shortenedUrl = serverUrl + response.data.shortened_key)
        .catch(error => this.errorMessage = error.response.data && error.response.data.message || error.message);
    },

    pasteUrlInput() {
      navigator.clipboard.readText()
        .then(text => this.urlInput = text)
        .catch(err => this.errorMessage = 'Failed to read clipboard contents due to ' + err);
    },

    // ref: https://dev.to/lindaojo/dark-mode-using-css-variables-vue-js-37il
    toggleTheme() {
      this.theme = this.theme == 'light' ? 'dark' : 'light'; //toggles theme value
      document.documentElement.setAttribute('data-theme', this.theme); // sets the data-theme attribute
      localStorage.setItem('theme', this.theme); // stores theme value on local storage
    }
  }
}
</script>

<style lang="scss">
:root, [data-theme=light] {
  --color-text: black;
  --color-default: white;
}
[data-theme=dark] {
  --color-text: white;
  --color-default: #2a313a;

  a {
    color: var(--color-text);
  }
}

body {
  background-color: var(--color-default);
  color: var(--color-text);
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 30vh;
}

input {
  width: 60%;
  max-width: 580px;
}

input,
button {
  padding: 3px;
}

input,
.label {
  margin-bottom: 6px;
}

.result {
  margin-top: 30px;

  .error {
    color: red;
  }
}

button:hover {
  cursor: pointer;
}

.btn__theme {
  all: unset;
}
</style>
