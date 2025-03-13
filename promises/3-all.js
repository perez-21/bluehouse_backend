import { uploadPhoto, createUser } from './utils.js';

async function handleProfileSignup() {
  const { body: photo } = await uploadPhoto();
  const { firstName, lastName } = await createUser();

  console.log(`${photo} ${firstName} ${lastName}`);
}

export default handleProfileSignup;
