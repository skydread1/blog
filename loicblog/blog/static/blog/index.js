/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function toggleCatDropdown() {
    document.getElementById("cat-dropdown").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var CatDropdown = document.getElementById("cat-dropdown");
      if (CatDropdown.classList.contains('show')) {
        CatDropdown.classList.remove('show');
      }
    }
  }