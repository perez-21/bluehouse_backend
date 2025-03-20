class ALXCOURSE {
  constructor(name, length, students) {
    // check name
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    this.name = name;

    // check length
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    }
    this.length = length;

    // check length
    if (!Array.isArray(students)) {
      throw TypeError('Students must be an array');
    }
    this.students = students;
  }
}

export default ALXCOURSE;
