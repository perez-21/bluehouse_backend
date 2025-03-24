function getStudentsByLocation(students, city) {
  return students.filter((student) => student.location.includes(city));
}

export default getStudentsByLocation;
