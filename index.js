const express = require('express');
const axios = require('axios');
const path = require('path');
const fs = require('fs')

const app = express();
const port = 3000;

app.use(express.static('public'));

app.get('/api/getFile/:title', (req, res) => {
    // Extract the title from the request parameters
    const title = req.params.title;
    
    // Specify the path to the JSON file based on the title
    const filePath = path.join(__dirname, 'db', `${title}.json`);

    // Read the content of the JSON file
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            res.status(500).send('Internal Server Error');
            return;
        }

        // Parse the JSON data
        const jsonData = JSON.parse(data);

        // Send the JSON data as a response
        res.json(jsonData);
    });
});

app.listen(port, () => {
    console.log(`Node.js server listening at http://localhost:${port}`);
});