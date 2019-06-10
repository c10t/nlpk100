import NuxtConfiguration from '@nuxt/config'

const config: NuxtConfiguration = {
  css: [
    '@/assets/style.css'
  ],
  head: {
    link: [
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500' }
    ]
  }
}

export default config
