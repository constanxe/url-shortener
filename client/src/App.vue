<template>
  <div id="app">
    <h2>URL Shortener</h2>
    URL: <input type="url" v-model="urlInput"> <button @click="generateShortenedUrl()" @keydown.enter="generateShortenedUrl()">Shorten</button><br>
    <div v-if="shortenedUrl">
      Shortened URL: <a target="_blank" :href="shortenedUrl">{{shortenedUrl}}</a> <button @click="copyShortenedUrl()">Copy</button>
    </div>
    <div class="error">{{errorMessage}}</div>
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
    generateShortenedUrl() {
      this.shortenedUrl = '';

      const url = this.urlInput.trim();
      if (!url) {
        this.errorMessage = 'Please enter a URL';
        return;
      }
      if (!this.isValidUrl(url)) {
        this.errorMessage = 'Please enter a valid URL';
        return;
      }
      this.errorMessage = '';

      axios.post('http://localhost:3000', {url})
        .then(response => this.shortenedUrl = 'http://localhost:3000/' + response.data.shortened_key)
        .catch(error => this.errorMessage = error.response.data.message || error.message);
    },
    copyShortenedUrl() {
      navigator.clipboard.writeText(this.shortenedUrl)
    },

    isValidUrl(input) {
      try {
      	return Boolean(new URL(input));
      } catch (error) {
      	return false;
      }
    }
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
  margin-top: 60px;
}

input {
  margin-bottom: 6px;
}

.error {
  color: red;
}
</style>
