// Error on ts-node when "module": "esnext" in tsconfig.json
// ref: https://github.com/TypeStrong/ts-node/issues/510
// import fs from 'fs'
// import path from 'path'
const fs = require('fs')
const path = require('path')
const readline = require('readline')

const download = async () => {
  const filepath = path.join(process.cwd(), '/data/sample.txt')
  const filestream = fs.createReadStream(filepath)
  const rl = readline.createInterface({ input: filestream, crlfDelay: Infinity })
  for await (const line of rl) {
    console.log(`line from file: ${line}`)
  }
  // const contents = await fs.promises.readFile(filepath, { encoding: 'utf-8' }).catch(err => err)
  // console.log(contents)
}

download()
