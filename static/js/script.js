




// Collapse section
  let faqs = document.querySelectorAll(".faq");

  faqs.forEach(faq => {
    faq.addEventListener("click", () => {
      faq.classList.toggle("active")
    })

  })
    
  



  // Dark mode

  let colorIcon = document.getElementById("color-icon")
  

  colorIcon.addEventListener("click", function(){
    document.body.classList.toggle("dark-mode");
    if(document.body.classList.contains("dark-mode")) {
      colorIcon.src = "{{url_for('static', filename='sun.png')}}"
    } else{
      colorIcon.src = "{{url_for('static', filename='moon.png')}}"
    }
  });
      

  // Scroll

let scrollDown = document.getElementById("scroll-down")

let aboutMini = document.getElementById("about-mini")

scrollDown.addEventListener("click", function() {
    aboutMini.scrollIntoView()
    
});

// Collapsing nav-bar code

let navBtn = document.querySelector(".nav-btn");

let navBar = document.querySelector(".nav-bar");

navBtn.addEventListener("click", function() {
    if (navBar.classList.contains("show-bar")) {
        navBar.classList.remove("show-bar");
    }
    else{
        navBar.classList.add("show-bar");
    }


}); 
