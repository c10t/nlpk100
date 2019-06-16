import { Component, Vue, Prop } from 'vue-property-decorator'
import Artist from '@/models/artist'

@Component
export default class ArtistsTable extends Vue {
  headers = [
    { text: 'Name', align: 'left', value: 'name' }
  ]

  artists = []
}
