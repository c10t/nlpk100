import express from 'express'

const app = express()

app.get('/', (req, res) => {
  res.send({ hello: 'express' })
})

export default app
