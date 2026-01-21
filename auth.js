import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { 
  getAuth, 
  createUserWithEmailAndPassword, 
  signInWithEmailAndPassword,
  sendEmailVerification
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// YOUR FIREBASE CONFIG
const firebaseConfig = {
  apiKey: "ATzAsyDghZLnJfsP9C_nNFl-EMv5hRr-Tl0z-Nw",
  authDomain: "mahi-website-4df3d.firebaseapp.com",
  projectId: "mahi-website-4df3d",
  storageBucket: "mahi-website-4df3d.appspot.com",
  messagingSenderId: "558548222320",
  appId: "1:558548222320:web:968a6edb3b19e60798547f"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// SIGNUP FUNCTION
window.signup = function () {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  createUserWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {

      sendEmailVerification(userCredential.user);

      alert("Account created! Verify your email.");
    })
    .catch((error) => {
      alert(error.message);
    });
};

// LOGIN FUNCTION
window.login = function () {
  const email = document.getElementById("login_email").value;
  const password = document.getElementById("login_password").value;

  signInWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      if (!userCredential.user.emailVerified) {
        alert("Please verify email before login.");
        return;
      }
      alert("Login Successful!");
      window.location.href = "index.html";
    })
    .catch((error) => {
      alert("Login failed: " + error.message);
    });
};
