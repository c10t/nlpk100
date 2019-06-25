export const sampleArtist: Artist = {
  id: 20660,
  gid: 'ecf9f3a3-35e9-4c58-acaa-e707fba45060',
  name: 'Oasis',
  sort_name: 'Oasis',
  area: 'United Kingdom',
  aliases: [{ name: 'オアシス', sort_name: 'オアシス' }],
  begin: { year: 1991 },
  end: { year: 2009, month: 8, date: 28 },
  tags: [{ count: 13, value: 'rock' }, { count: 2, value: 'pop' }],
  rating: { count: 13, value: 86 }
}

export default interface Artist {
  id: number
  gid: string
  name: string
  sort_name: string
  area: string
  aliases: {
    name: string
    sort_name: string
  }[]
  begin: {
    year?: number
    month?: number
    date?: number
  }
  end: {
    year?: number
    month?: number
    date?: number
  }
  tags: {
    count: number
    value: string
  }[]
  rating: {
    count: number
    value: number
  }
}
