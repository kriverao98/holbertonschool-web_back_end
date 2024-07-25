export default function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    promise
      .then(() => {
        const response = {
          status: 200,
          body: 'success',
        };
        resolve(response);
      })
      .catch(() => {
        reject(new Error());
      });
  }).then((response) => {
    console.log('Got a response from the API');
    return response;
  });
}
