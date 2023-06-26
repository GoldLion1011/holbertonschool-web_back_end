// creates a function to count students in a database file

const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n');

    if (lines.length === 0) {
      throw new Error('Cannot load the database');
    }

    const students = lines.map((line) => line.split(','))
      .filter((student) => student.length === 4 && student.every((field) => field.trim() !== ''))
      .map((student) => ({
        firstName: student[0].trim(),
        lastName: student[1].trim(),
        age: parseInt(student[2].trim()),
        field: student[3].trim(),
      }));

    const fieldCounts = {};
    students.forEach((student) => {
      if (!fieldCounts[student.field]) {
        fieldCounts[student.field] = {
          count: 0,
          names: [],
        };
      }
      fieldCounts[student.field].count++;
      fieldCounts[student.field].names.push(student.firstName);
    });

    console.log(`Number of students: ${students.length}`);
    Object.entries(fieldCounts).forEach(([field, { count, names }]) => {
      console.log(`Number of students in ${field}: ${count}. List: ${names.join(', ')}`);
    });
  } catch (error) {
    console.error(error.message);
  }
}

// Usage example
countStudents('path/to/database.csv');
