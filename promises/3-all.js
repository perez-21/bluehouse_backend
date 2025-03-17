import { uploadPhoto, createUser } from './utils.js';

function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([photoData, userData]) => {
      console.log(
        `${photoData.body} ${userData.firstName} ${userData.lastName}`,
      );
    })
    .catch((error) => console.error('Signup system offline'));
}

export default handleProfileSignup;
