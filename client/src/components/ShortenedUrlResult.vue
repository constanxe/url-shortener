<template>
  <div v-if="shortenedUrl">
    <b>Shortened URL: <a target="_blank" :href="shortenedUrl">{{shortenedUrl}}</a></b>
    &nbsp;<button @click="copyShortenedUrl()">Copy</button>
  </div>
</template>

<script>
export default {
  name: 'ShortenedUrlResult',
  props: {
    shortenedUrl: String,
  },
  methods: {
    copyShortenedUrl() {
      navigator.clipboard.writeText(this.shortenedUrl);
    },
  }
}
</script>
