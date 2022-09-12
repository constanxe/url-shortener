<template>
  <div v-if="shortenedUrl">
    Shortened URL: <a target="_blank" :href="shortenedUrl">{{shortenedUrl}}</a>
    &nbsp;<button @click="copyShortenedUrl()">Copy</button>
  </div>
</template>

<script>
export default {
  name: 'ShortenedUrlResult',
  props: {
    shortenedUrl: String
  },
  methods: {
    copyShortenedUrl() {
      navigator.clipboard.writeText(this.shortenedUrl);
    },
  }
}
</script>
