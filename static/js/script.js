


// Collapse section
  let faqs = document.querySelectorAll(".faq");

  faqs.forEach(faq => {
    faq.addEventListener("click", () => {
      faq.classList.toggle("active")
    })

  })
    
  



  // Dark mode

  const colorIcon = document.getElementById("color-icon")


  

  colorIcon.addEventListener("click", function(){
    document.body.classList.toggle("dark-mode");
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


