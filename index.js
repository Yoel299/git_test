const express = require('express')
const mysql = require('mysql2/promise')
const bluebird = require('bluebird')

const app = express()

let howw

async function go() { 
    howw = await mysql.createConnection({
        host: 'localhost',
        port: 3307,
        user: 'root',
        password: 'example',
        database: 'pets',
        Promise: bluebird
    })
    app.listen(3000)
}

go()

app.get('/', async (req, res) => {
    const [users] = await db.execute('SELECT * FROM users')
    console.log(users)
    res.send('<h1>Hello World!</h1>')
})


