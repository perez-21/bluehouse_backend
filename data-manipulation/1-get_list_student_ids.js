function getListStudentIds(arr) {
  if (!Array.isArray(arr)) {
    return [];
  }
  return arr.map((record) => record.id);
}

export default getListStudentIds;
