// ==============================
//  Firebase Auth Navbar
// ==============================

// Firebase Config (paste your config)
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-auth.js";

const firebaseConfig = {
    apiKey: "ATzASyDghZLJnfS9PC_nNF1-EMv5hRr-TI0z-Nw",
    authDomain: "mahi-website-4df3d.firebaseapp.com",
    projectId: "mahi-website-4df3d",
    storageBucket: "mahi-website-4df3d.appspot.com",
    messagingSenderId: "558542822230",
    appId: "1:558542822230:web:968a6ebd3b19e6070854f7"
};

// Firebase Init
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Navbar Buttons
const loginBtn = document.getElementById("loginBtn");
const signupBtn = document.getElementById("signupBtn");
const logoutBtn = document.getElementById("logoutBtn");

// User Login State Check
onAuthStateChanged(auth, (user) => {
    if (user) {
        console.log("User Logged In:", user.email);
        loginBtn.style.display = "none";
        signupBtn.style.display = "none";
        logoutBtn.style.display = "inline";
    } 
    else {
        console.log("User Logged Out");
        loginBtn.style.display = "inline";
        signupBtn.style.display = "inline";
        logoutBtn.style.display = "none";
    }
});
// Logout Button Action
if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {
        signOut(auth)
        .then(() => {
            alert("Logged Out Successfully!");
            window.location.href = "index.html";
        })
        .catch((error) => {
            console.error("Logout Error:", error);
        });
    });
}
