import { Component, Vue, Prop } from 'vue-property-decorator'
import Artist, { sampleArtist } from '@/models/artist'

@Component
export default class ArtistsTable extends Vue {
  headers = [
    { text: 'Name', align: 'left', value: 'name' },
    { text: 'Area', align: 'left', value: 'area' },
    { text: 'Aliases', align: 'left', value: 'aliases' },
    { text: 'Begin', align: 'left', value: 'begin' },
    { text: 'End', align: 'left', value: 'end' },
    { text: 'Tags', align: 'left', value: 'tags' },
    { text: 'Rating', align: 'left', value: 'rating' },
  ]

  artists = [sampleArtist]
}
