export function uploadPhoto() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ body: 'photo-profile-1' });
    }, 100);
  });
}

export function createUser() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ firstName: 'Guillaume', lastName: 'Salva' });
    }, 100);
  });
}
