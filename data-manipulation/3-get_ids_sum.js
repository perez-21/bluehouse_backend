function getStudentIdsSum(students) {
  return students.reduce((acc, current) => acc + current.id, 0);
}

export default getStudentIdsSum;
