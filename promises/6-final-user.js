import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) => results);
}

export default handleProfileSignup;
