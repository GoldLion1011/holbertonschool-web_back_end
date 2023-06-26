// now do it asynchronously

const fs = require('fs');

const countStudents = async (file) => {
  let content;
  try {
    content = await fs.promises.readFile(file, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  lines = lines.split('\n');
  lines = lines.filter((line) => line !== '').slice(1);
  console.log(`Number of students: ${lines.length}`);

  const field = lines.map((line) => line.split(',')[3]);
  const eachField = [...new Set(field)];
  const dict = {};

  eachField.forEach((fieldName) => {
    const studentsPerField = lines
      .filter((line) => line.endsWith(fieldName))
      .map((line) => {
        const split = line.split(',');
        return split[0];
      });
    dict[fieldName] = studentsPerField.length;
  });
};
