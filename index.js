const express = require('express');
const axios = require('axios');
const path = require('path');
const fs = require('fs')

const app = express();
const port = 3000;

app.use(express.static('public'));

app.get('/api/getFile/:title', (req, res) => {
    const title = req.params.title;
    
    const filePath = path.join(__dirname, 'db', `${title}.json`);

    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            res.status(500).send('Internal Server Error');
            return;
        }

        const jsonData = JSON.parse(data);

        res.json(jsonData);
    });
});

app.listen(port, () => {
    console.log(`Node.js server listening at http://localhost:${port}`);
});