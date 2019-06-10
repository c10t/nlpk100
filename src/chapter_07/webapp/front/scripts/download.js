const fs = require('fs')
const path = require('path')

const download = async () => {
  const filepath = path.join(process.cwd(), '/data/sample.txt')
  const contents = await fs.promises.readFile(filepath, { encoding: 'utf-8' }).catch(err => err)
  console.log(contents)
}

download()
