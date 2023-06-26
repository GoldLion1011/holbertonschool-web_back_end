// create a function to count students in a file

const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');
    let count = 0;
    let fields;
    const dict = {};
    for (const i in lines) {
      if (lines[i]) {
        count += 1;
        fields = lines[i].split(',');
        if (!dict[fields[3]]) {
          dict[fields[3]] = [];
        }
        dict[fields[3]].push(fields[0]);
      }
    }
    console.log(`Number of students: ${count}`);
    for (const key in dict) {
      if (key) {
        const list = dict[key];
        console.log(`Number of students in ${key}: ${list.length}. List: ${list.toString().replace(/,/g, ', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
