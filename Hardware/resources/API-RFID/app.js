const express = require('express')
const info = require('./id.json')
const app = express()

app.use(express.text())

app.get('/about.json', function (req, res) {
    res.json({
        routes: [
            {
                name: "about.json",
                method: "GET",
            },
            {
                name: "get_info",
                method: "POST",
                parameters: "none",
                body: "Raw bytes uid",
                response: "found user",
                response_code: [200, 401]
            },
            {
                name: "open",
                method: "POST",
                parameters: "none",
                body: "Raw bytes uid",
                response: "none",
                response_code: [200, 401]
            }
        ]
    })
})

app.route('/get_info').post(function (req, res) {
    var chunk;

    req.on('data', function (data) {
        chunk = data;
    })

    req.on('end', function () {
        info.map((uid) => {
            if (Buffer.compare(chunk, new Buffer.from(uid.uid, "hex")) == 0) {
                uid.authorized = null;
                res.send(200, uid).end()
            }
        })
        res.status(401).end()

    })
})

app.route('/open').post(function (req, res) {
    var chunk;

    req.on('data', function (data) {
        chunk = data;
    })

    req.on('end', function () {
        info.map((uid) => {
            if (Buffer.compare(chunk, new Buffer.from(uid.uid, "hex")) == 0) {
                if (uid.authorized)
                    res.status(200).end()
            }
        })
        res.status(401).end()

    })
})

app.listen(3000)