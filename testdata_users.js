const firebase = require('firebase/compat/app');
require('firebase/compat/firestore');

const firebaseConfig = {
  apiKey: "AIzaSyDkiAnxFTj9l8YcPwfHGBIVb10ltKL2Q5U",
  authDomain: "bisonadvisor-c37cb.firebaseapp.com",
  projectId: "bisonadvisor-c37cb",
  storageBucket: "bisonadvisor-c37cb.appspot.com",
  messagingSenderId: "668841962708",
  appId: "1:668841962708:web:2750e327e71bbe022f1f41",
  measurementId: "G-H9V6XL0YK5"
};

firebase.initializeApp(firebaseConfig);

const db = firebase.firestore();

// Adding a new user document to 'users' collection

//student users
db.collection("users").add({
  username: "testuser1",
  password: "123456",
  type: "student"
})
.then(docRef => {
  console.log("Document written with ID: ", docRef.id);
})
.catch(error => {
  console.error("Error adding document: ", error);
});

db.collection("users").add({
  username: "testuser2",
  password: "456789",
  type: "student"
})
.then(docRef => {
  console.log("Document written with ID: ", docRef.id);
})
.catch(error => {
  console.error("Error adding document: ", error);
});

//advisor users
db.collection("users").add({
  username: "testuser3",
  password: "abcabc",
  type: "advisor"
})
.then(docRef => {
  console.log("Document written with ID: ", docRef.id);
})
.catch(error => {
  console.error("Error adding document: ", error);
});

db.collection("users").add({
  username: "testuser4",
  password: "ababab",
  type: "advisor"
})
.then(docRef => {
  console.log("Document written with ID: ", docRef.id);
})
.catch(error => {
  console.error("Error adding document: ", error);
});

//admin users
db.collection("users").add({
  username: "testuser5",
  password: "123abc",
  type: "admin"
})
.then(docRef => {
  console.log("Document written with ID: ", docRef.id);
})
.catch(error => {
  console.error("Error adding document: ", error);
});

db.collection("users").add({
  username: "testuser6",
  password: "abc123",
  type: "admin"
})
.then(docRef => {
  console.log("Document written with ID: ", docRef.id);
})
.catch(error => {
  console.error("Error adding document: ", error);
});