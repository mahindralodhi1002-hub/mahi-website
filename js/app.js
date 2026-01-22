function goHome(){
  window.location.href = "/mahi-website/index.html";
}
function goBack(){
  history.back();
}
function toggleDark(){
  document.body.classList.toggle("dark");
  localStorage.setItem("dark",
    document.body.classList.contains("dark"));
}
if(localStorage.getItem("dark")==="true"){
  document.body.classList.add("dark");
}
