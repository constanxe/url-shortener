<template>
  <div id="app">
    URL: <input v-model="url"> <button @click="generateShortenedUrl()" @keydown.enter="generateShortenedUrl()">Shorten</button><br>
    <div v-if="shortenedUrl" >Shortened URL: <a :href="shortenedUrl" target="_blank">{{shortenedUrl}}</a></div>
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
      url: 'https://blog.gds-gov.tech/terragrunt-in-retro-i-would-have-done-thesefew-things-e5aaac451942',
      shortenedUrl: '',
      errorMessage: ''
    }
  },
  methods: {
    generateShortenedUrl() {
      this.shortenedUrl = '';
      this.errorMessage = '';

      axios.post('http://localhost:3000', {url: this.url})
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
}
</style>
