<template>
  <div id="app">
    URL: <input v-model="url"> <button @click="generateShortenedUrl()">Shorten</button><br>
    Shortened URL: <a :href="shortenedUrl">{{shortenedUrl}}</a>
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
      shortenedUrl: ''
    }
  },
  methods: {
    generateShortenedUrl() {
      axios.post('http://localhost:3000', {url: this.url})
        .then(response => this.shortenedUrl = 'http://localhost:3000/' + response.data.shortened_key)
        .catch(error => console.log(response.data.message || error));
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
</style>
