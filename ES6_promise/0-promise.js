export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const a = true;
    if (a === true) {
      resolve('true');
    } else { 
        resolve('false');
    }
  });
}
