/**
 * Function to get students located in a specific city
 * @param {Array} students - Array of student objects
 * @param {string} city - City to filter students by
 * @returns {Array} - Array of students located in the specified city
 */
function getStudentsByLocation(students, city) {
  if (!Array.isArray(students) || typeof city !== 'string') {
    return [];
  }

  return students.filter((student) => student.location === city);
}

export default getStudentsByLocation;
