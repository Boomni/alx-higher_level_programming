#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];

const fileAContents = fs.readFileSync(fileA, 'utf-8');
const fileBContents = fs.readFileSync(fileB, 'utf-8');

fs.writeFileSync(process.argv[4], `${fileAContents}${fileBContents}`);
