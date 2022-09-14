<template>
  <div id="app">
    <h2>
      URL Shortener
      <button class="theme" @click="toggleTheme" :title="`Change theme to ${getOtherTheme()} mode`" :aria-label="`Change theme to ${getOtherTheme()} mode`">
        {{theme == 'light' ? '🌙' : '☀️'}}
      </button>
    </h2>

    <div class="label">Let's get started!<br>Insert your URL here.</div>

    <input type="search" v-model="urlInput" @keydown.enter="generateShortenedUrl()"> <button @click="pasteUrlInput()">Paste</button> <br>
    <button @click="generateShortenedUrl()">Shorten</button>

    <div class="result">
      <ShortenedUrlResult :shortenedUrl="shortenedUrl"/>
      <div class="label" :class="{error: !isLoading}" v-html="message"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ShortenedUrlResult from './components/ShortenedUrlResult.vue'

const serverUrl = 'http://localhost:3000/';

export default {
  name: 'App',
  components: {
    ShortenedUrlResult
  },
  data() {
    return {
      urlInput: 'https://blog.gds-gov.tech/terragrunt-in-retro-i-would-have-done-thesefew-things-e5aaac451942',
      shortenedUrl: '',
      message: '',
      isLoading: false,
      theme: 'light',
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
        this.message = 'Please enter a URL.';
        return;
      }
      if (!this.isValidUrl(url)) {
        this.message = 'Please enter a <b>valid</b> URL with http(s) in front.';
        return;
      }

      this.message = 'Loading...';
      this.isLoading = true;

      axios.post(serverUrl, {url})
        .then(response => {
          this.message = '';
          this.isLoading = false;
          this.shortenedUrl = serverUrl + response.data.shortened_key;
        })
        .catch(error => {
          this.isLoading = false;
          this.message = 'Failed to shorten URL due to ' + (error.response
            ? error.response.data.message // server is running -> can return response
            : error.message + `<br><small>Please ensure server is running at <a href="${serverUrl}">${serverUrl}</a></small>`
          )
        });
    },

    pasteUrlInput() {
      navigator.clipboard.readText()
        .then(text => this.urlInput = text)
        .catch(err => this.message = 'Failed to read clipboard contents due to ' + err);
    },

    getOtherTheme() {
      return this.theme == 'light' ? 'dark' : 'light';
    },
    setTheme() {
      document.documentElement.setAttribute('data-theme', this.theme);
    },
    toggleTheme() { // ref: https://dev.to/lindaojo/dark-mode-using-css-variables-vue-js-37il
      this.theme = this.getOtherTheme(); //toggles theme value
      this.setTheme(); // sets the data-theme attribute
      localStorage.setItem('theme', this.theme); // stores theme value on local storage
    },
  },
  mounted() {
    this.theme = localStorage.getItem('theme');
    document.documentElement.setAttribute('data-theme', this.theme)
  }
}
</script>

<style lang="scss">
:root,
[data-theme=light] {
  --color-text: black;
  --color-default: white;
}
[data-theme=dark] {
  --color-text: white;
  --color-default: #2a313a;

  a {
    color: inherit;
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
  margin-top: 26vh;
  font-size: 20px;
}

.result {
  margin-top: 30px;

  .error {
    color: red;
  }
}

/* elements */
input {
  outline: none;
  width: 60%;
  max-width: 580px;
  padding: 6px;
  margin-top: 12px;
}

input,
button {
  font-size: 16px;
}

button {
  border: none;
  color: white;
  padding: 8px 12px;
  margin-top: 8px;
  border-radius: 18px;
  background-color: rgb(243, 189, 88);

  &:hover {
    cursor: pointer;
  }

  &.theme {
    all: unset;
  }
}
</style>
