import firebase from "firebase";
import "firebase/auth";
import "firebase/firestore";

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const config = {
  apiKey: "AIzaSyARPVUbWZI-L9VoswbfPUMUk1M0WRkcNUg",
  authDomain: "requiz-54781.firebaseapp.com",
  projectId: "requiz-54781",
  storageBucket: "requiz-54781.appspot.com",
  messagingSenderId: "744263977007",
  appId: "1:744263977007:web:b118bc584ed6225c4bdeda",
  measurementId: "G-JGW386WPMB",
};

if (!firebase.apps.length) {
  firebase.initializeApp(config);
}

const app = firebase.app();
const auth = firebase.auth();
const db = firebase.firestore();
const now = firebase.firestore.Timestamp.now();
export { auth, db, now };
console.log(app.name ? "Firebase Mode Activated!" : "Firebase not working :(");
