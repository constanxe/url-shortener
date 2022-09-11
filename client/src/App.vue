<template>
  <div id="app">
    <h2>URL Shortener</h2>
    <div class="label">Let's get started!<br>Insert your URL here.</div>
    <input type="search" v-model="urlInput"> <button @click="pasteUrlInput()">Paste</button> <br>
    <button @click="generateShortenedUrl()" @keydown.enter="generateShortenedUrl()">Shorten</button>

    <div class="result">
      <div v-if="shortenedUrl">
        Shortened URL: <a target="_blank" :href="shortenedUrl">{{shortenedUrl}}</a>
        &nbsp;<button @click="copyShortenedUrl()">Copy</button>
      </div>

      <div class="error label" v-html="errorMessage"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld
  },
  data() {
    return {
      urlInput: 'https://blog.gds-gov.tech/terragrunt-in-retro-i-would-have-done-thesefew-things-e5aaac451942',
      shortenedUrl: '',
      errorMessage: ''
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
        this.errorMessage = 'Please enter a <b>valid</b> URL';
        return;
      }
      this.errorMessage = '';

      axios.post('http://localhost:3000', {url})
        .then(response => this.shortenedUrl = 'http://localhost:3000/' + response.data.shortened_key)
        .catch(error => this.errorMessage = error.response.data && error.response.data.message || error.message);
    },
    pasteUrlInput() {
      navigator.clipboard.readText()
        .then(text => this.urlInput = text)
        .catch(err => this.errorMessage = 'Failed to read clipboard contents due to ' + err);
    },
    copyShortenedUrl() {
      navigator.clipboard.writeText(this.shortenedUrl);
    },
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
</style>
