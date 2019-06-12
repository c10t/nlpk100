import NuxtConfiguration from '@nuxt/config'

const config: NuxtConfiguration = {
  css: [
    '@/assets/style.css'
  ],
  head: {
    link: [
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500' }
    ]
  },
  serverMiddleware: [
    { path: '/api', handler: '@/server/api/index.ts' }
  ],
  modules: [
    '@nuxtjs/vuetify'
  ],
  vuetify: {
    theme: {
      primary: '#f23567',
      secondary: '#02eea3',
      accent: '#ee02c3',
      error: '#ee2d02'
    }
  }
}

export default config
