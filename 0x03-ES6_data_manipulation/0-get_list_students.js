export default function getListStudents() {
  function Student(id, firstName, location) {
    return {
      id,
      firstName,
      location,
    };
  }
  const student1 = Student(1, 'Guillaume', 'San Francisco');
  const student2 = Student(2, 'James', 'Columbia');
  const student5 = Student(5, 'Serena', 'San Francisco');

  const studentList = [];
  studentList.push(student1, student2, student5);
  return studentList;
}
