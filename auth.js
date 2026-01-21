import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { 
  getAuth,
  createUserWithEmailAndPassword,
  sendEmailVerification,
  signInWithEmailAndPassword,
  signOut
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

import { firebaseConfig } from "./firebase-config.js";

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// SIGNUP
window.signup = function() {
  let email = document.getElementById("email").value;
  let password = document.getElementById("password").value;

  createUserWithEmailAndPassword(auth, email, password)
    .then(userCredential => {
      sendEmailVerification(auth.currentUser);
      alert("Verification link sent to your email!\nPlease verify and then login.");
    })
    .catch(error => alert(error.message));
};

// LOGIN
window.login = function() {
  let email = document.getElementById("login_email").value;
  let password = document.getElementById("login_password").value;

  signInWithEmailAndPassword(auth, email, password)
    .then(userCredential => {

      if (!auth.currentUser.emailVerified) {
        alert("Please verify your email first!");
        return;
      }

      window.location.href = "index.html";
    })
    .catch(error => alert(error.message));
};

// LOGOUT
window.logoutUser = function() {
  signOut(auth).then(() => {
    alert("Logged out!");
    window.location.href = "login.html";
  });
};
