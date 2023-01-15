export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsByLocation = students.filter((element) => element.location === city);

  for (const item of studentsByLocation) {
    item.grade = 'N/A';
  }

  const updateGrade = studentsByLocation.map((element) => {
    const elementCopy = element;
    for (const property of newGrades) {
      if (elementCopy.id === property.studentId) elementCopy.grade = property.grade;
    }
    return elementCopy;
  });
  return updateGrade;
}
