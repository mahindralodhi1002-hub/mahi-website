// Firebase imports
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";

// Firebase config
const firebaseConfig = {
  apiKey: "ATzASyDghZLJnfS9PC_nNF1-EMv5hRr-TI0z-Nw",
  authDomain: "mahi-website-4df3d.firebaseapp.com",
  projectId: "mahi-website-4df3d",
  storageBucket: "mahi-website-4df3d.appspot.com",
  messagingSenderId: "558542822230",
  appId: "1:558542822230:web:968a6ebd3b19e6070854f7"
};

// Init
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Navbar buttons
const loginBtn = document.getElementById("loginBtn");
const signupBtn = document.getElementById("signupBtn");
const logoutBtn = document.getElementById("logoutBtn");

// Login state check
onAuthStateChanged(auth, (user) => {
  if (user) {
    loginBtn.style.display = "none";
    signupBtn.style.display = "none";
    logoutBtn.style.display = "inline";
  } else {
    loginBtn.style.display = "inline";
    signupBtn.style.display = "inline";
    logoutBtn.style.display = "none";
  }
});

// Logout
logoutBtn.addEventListener("click", () => {
  signOut(auth).then(() => {
    alert("Logged out successfully");
    window.location.href = "index.html";
  });
});
