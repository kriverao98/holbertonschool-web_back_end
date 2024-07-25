export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    const a = true;
    if (a === true) {
      resolve('true');
    }
  });
}
