


// Collapse section

// selecting the container for each faq
  let faqs = document.querySelectorAll(".faq");

//toggling the css class 'active' in order to use accordian
  faqs.forEach(faq => {
    faq.addEventListener("click", () => {
      faq.classList.toggle("active")
    })

  })
    
  



  // Dark mode

  const colorIcon = document.getElementById("color-icon")


  
  // A more elegant decision than last time. Instead of removing and adding classes, merely toggle the 'dark-mode class'
  colorIcon.addEventListener("click", function(){
    document.body.classList.toggle("dark-mode");
    // code to switch the icon taht changes theme depending if 'dark mode' is on or not
    if(document.body.classList.contains("dark-mode")) {
      colorIcon.src = "static/sun.png"
    } else{
      colorIcon.src = "static/moon.png"
    }
  });
      

  // Scroll

let scrollDown = document.getElementById("scroll-down")

let aboutMini = document.getElementById("about-mini")

scrollDown.addEventListener("click", function() {
    aboutMini.scrollIntoView()
    
});


