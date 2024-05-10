// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-auth.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDkJdt4OMzwXox91-dv3o9ZloIqHdVhJCc",
  authDomain: "ddos-finder.firebaseapp.com",
  projectId: "ddos-finder",
  storageBucket: "ddos-finder.appspot.com",
  messagingSenderId: "460420813801",
  appId: "1:460420813801:web:b749283c8818b97d467178"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
auth.languageCode = 'it';

const provider = new GoogleAuthProvider();

// Google Authentication Button
const googleLoginBtns = document.querySelectorAll("#google-login-btn");
googleLoginBtns.forEach(btn => {
  btn.addEventListener("click", function() {
    signInWithPopup(auth, provider)
      .then((result) => {
        // This gives you a Google Access Token. You can use it to access the Google API.
        const credential = GoogleAuthProvider.credentialFromResult(result);
        // const token = credential.accessToken;
        // The signed-in user info
        const user = result.user;

        // Redirect to Home page
        window.location.href = "home.html";
      })
      .catch((error) => {
        // Handle Errors here
        const errorCode = error.code;
        const errorMessage = error.message;
        console.error(`Error [${errorCode}]: ${errorMessage}`);
      });
  });
});
