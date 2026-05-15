const fs = require('fs');
function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) =>line.trim() !== '');
    const students = lines.slice(1);

    console.log (`Number of students: ${students.length}`);
    const fields = {};
    students.forEach((student) => {
      const columns = student.split(',');
      const firstName = columns[0];
      const field = columns[3];

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    });

    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
