<template>
  <div id="app">
    URL: <input v-model="urlInput"> <button @click="generateShortenedUrl()" @keydown.enter="generateShortenedUrl()">Shorten</button><br>
    <div v-if="shortenedUrl">Shortened URL: <a :href="shortenedUrl" target="_blank">{{shortenedUrl}}</a></div>
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
        this.errorMessage = 'Please enter a URL to shorten';
        return;
      }
      this.errorMessage = '';

      axios.post('http://localhost:3000', {url})
        .then(response => this.shortenedUrl = 'http://localhost:3000/' + response.data.shortened_key)
        .catch(error => this.errorMessage = error.response.data.message || error.message);
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

.error {
  color: red;
  margin-top: 6px;
}
</style>
