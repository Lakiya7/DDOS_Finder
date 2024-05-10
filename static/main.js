// main.js
// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDkJdt4OMzwXox91-dv3o9ZloIqHdVhJCc",
  authDomain: "ddos-finder.firebaseapp.com",
  projectId: "ddos-finder",
  storageBucket: "ddos-finder.appspot.com",
  messagingSenderId: "460420813801",
  appId: "1:460420813801:web:b749283c8818b97d467178"
};

// Initialize Firebase
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.21.0/firebase-app.js";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/9.21.0/firebase-auth.js";

// Initialize Firebase app and authentication
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Initialize GoogleAuthProvider
const provider = new GoogleAuthProvider();

// Add event listener to the Google login button
document.getElementById("login").addEventListener("click", () => {
  signInWithPopup(auth, provider)
    .then((result) => {
      // Get the signed-in user info
      const user = result.user;
      console.log("User signed in:", user);

      // Optional: Handle the user's token for further server-side processing
      const token = result._tokenResponse.oauthIdToken;
      console.log("User token:", token);

      // Optionally redirect to another page after successful login
      window.location.href = "ISP_Web_App/templates/web.html";
    })
    .catch((error) => {
      // Handle Errors here
      console.error("Error during sign-in:", error.message);
      alert("Sign-in failed. Please try again.");
    });
});
