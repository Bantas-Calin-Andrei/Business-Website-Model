document.addEventListener("DOMContentLoaded", function() {
    function showSection(sectionId, scrollToId) {
        var sections = document.querySelectorAll("section");
        sections.forEach(function(section) {
            section.style.display = "none";
        });
    
        var headers = document.querySelectorAll("header");
        headers.forEach(function(header) {
            header.style.display = "none";
        });
    
        document.getElementById(sectionId).style.display = "block";
        document.getElementById("header-" + sectionId).style.display = "block";
    
    }
    

    // Event listeners for navigation buttons
    document.querySelector(".navbar a[onclick*='acasa']").addEventListener("click", function() {
        showSection("acasa");
    });

    document.querySelector(".navbar a[onclick*='echipa']").addEventListener("click", function() {
        showSection("echipa");
    });

    document.querySelector(".navbar a[onclick*='contact']").addEventListener("click", function() {
        showSection("contact");
    });

    document.querySelector(".navbar a[onclick*='servicii']").addEventListener("click", function() {
        showSection("servicii");
    });


    
});


document.addEventListener("DOMContentLoaded", function() {
    const serviceBtns = document.querySelectorAll('.service-btn');
    const dropdownContents = document.querySelectorAll('.service-dropdown-content');
    
    serviceBtns.forEach((btn, index) => {
        btn.addEventListener('click', function() {
            // Toggle active class on the corresponding dropdown
            dropdownContents[index].classList.toggle('active');
            
            // Close other dropdowns
            dropdownContents.forEach((content, i) => {
                if (i !== index) {
                    content.classList.remove('active');
                }
            });
        });
    });
    
    // Close dropdowns when clicking outside
    document.addEventListener('click', function(event) {
        const isClickInside = serviceBtns.some(btn => btn.contains(event.target)) || 
                              dropdownContents.some(content => content.contains(event.target));
        
        if (!isClickInside) {
            dropdownContents.forEach(content => {
                content.classList.remove('active');
            });
        }
    });
});


