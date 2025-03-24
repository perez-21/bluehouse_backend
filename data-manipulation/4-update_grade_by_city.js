function updateStudentGradeByCity(students, city, newGrades) {
  const studentByCity = students.filter((student) =>
    student.location.includes(city),
  );

  return studentByCity.map((student) => {
    const newGrade = newGrades.find((grade) => student.id === grade.studentId);

    if (!newGrade) {
      student.grade = 'N/A';
      return student;
    }
    student.grade = newGrade.grade;
    return student;
  });
}

export default updateStudentGradeByCity;
