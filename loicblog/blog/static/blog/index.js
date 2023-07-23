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

// Get the dark/light mode toggle button and the HTML tag
const toggleButton = document.getElementById('dark-light-toggle');
const htmlTag = document.getElementsByTagName('html')[0];

// Get the moon and sun icons
const moonIcon = document.getElementById('moon-icon');
const sunIcon = document.getElementById('sun-icon');

// Function to toggle the mode and icons
function setMode(mode) {
  const other_mode = (mode == 'light') ? 'dark' : 'light'
  htmlTag.classList.remove(other_mode);
  htmlTag.classList.add(mode);
  if (mode == 'light') {
    moonIcon.style.display = 'inline-block';
    sunIcon.style.display = 'none';
  }
  else {
    moonIcon.style.display = 'none';
    sunIcon.style.display = 'inline-block';
  }
  localStorage.setItem('modePreference', mode);
}

function toggleMode() {
  if (htmlTag.classList.contains('dark')) {
    setMode('light')
  } else {
    setMode('dark')
  }
}

// Event listener for the button click
toggleButton.addEventListener('click', toggleMode);

// Check the mode preference in localStorage on page load
document.addEventListener('DOMContentLoaded', () => {
  // Get the mode preference from localStorage
  const modePreference = localStorage.getItem('modePreference');

  // If mode preference is not set (first visit), set default mode to 'light'
  if (!modePreference) {
    setMode('light')
  } else {
    setMode(modePreference)
  }
});