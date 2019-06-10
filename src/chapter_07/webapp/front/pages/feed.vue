<template>
  <div>
    <PostPreview class="post-preview" v-for="post in posts" :key="post.id" :post="post"/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Post from "@/models/post";

@Component({
  components: {
    PostPreview: () => import("@/components/post-preview.vue")
  },
  async asyncData() {
    let data: Post[] = [
      { id: 0, title: "hello Vue", description: "Vue start" },
      { id: 1, title: "hello nuxt", description: "Nuxt start" },
      { id: 2, title: "hello ts", description: "TypeScript start" }
    ];
    return {
      posts: data
    };
  }
})
export default class FeedPage extends Vue {
  posts: Post[] = [];
}
</script>

