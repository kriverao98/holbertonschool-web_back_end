function cleanSet(set, startString) {
  if (!(set instanceof Set) || typeof startString !== 'string') {
    throw new TypeError('Invalid arguments');
  }

  const result = Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length)) // Remove the startString
    .join('-'); // Join values with '-'

  return result;
}

export default cleanSet;
