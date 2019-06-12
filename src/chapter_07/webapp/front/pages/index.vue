<template>
  <v-app>
    <v-content>
      <Appbar/>
      <v-container>Hello, Vuetify!</v-container>
    </v-content>
  </v-app>
</template>
<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
@Component({
  components: {
    Appbar: () => import("@/components/appbar.vue")
  }
})
export default class IndexPage extends Vue {}
</script>
