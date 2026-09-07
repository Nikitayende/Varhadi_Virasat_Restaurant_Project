// ================= MENU SEARCH =================

const searchInput = document.getElementById("searchInput");

if (searchInput) {

    searchInput.addEventListener("keyup", function () {

        const value = this.value.toLowerCase();

        const cards = document.querySelectorAll(".menu-card");

        cards.forEach(function (card) {

            const dish = card.querySelector("h3").innerText.toLowerCase();

            if (dish.includes(value)) {

                card.style.display = "block";

            } else {

                card.style.display = "none";

            }

        });

    });

}

// ================= CATEGORY FILTER =================

const categoryButtons = document.querySelectorAll(".category-btn");

categoryButtons.forEach(function(button){

    button.addEventListener("click", function(){

        categoryButtons.forEach(function(btn){

            btn.classList.remove("active");

        });

        this.classList.add("active");

        const category = this.dataset.category;

        const cards = document.querySelectorAll(".menu-card");

        cards.forEach(function(card){

            if(category === "All"){

                card.style.display = "block";

            }

            else if(card.dataset.category === category){

                card.style.display = "block";

            }

            else{

                card.style.display = "none";

            }

        });

    });

});

// ================= AJAX ADD TO CART =================

function addToCart(dish_name, price, image, button){

    fetch("/add_to_cart", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            dish_name: dish_name,
            price: price,
            image: image
        })

    })
    .then(response => response.json())
    .then(data => {

        // Update cart count
        const cartCount = document.getElementById("cart-count");

        if(cartCount){
            cartCount.innerText = data.cart_count;
        }

        // ===== Show Floating Cart =====

        const floatingBtn = document.getElementById("floating-cart-btn");

        const floatingCount = document.getElementById("floating-cart-count");

        if(floatingBtn){

            floatingBtn.style.display = "flex";

        }

        if(floatingCount){

            floatingCount.innerText = data.cart_count;

        }

        // ===== Change button =====

        if(button){

            button.innerHTML = "✓ Added";

            button.classList.add("added");

            button.disabled = true;

        }

        // ===== Toast =====

        const toast = document.getElementById("toast");

        if(toast){

            toast.innerHTML = "✅ " + dish_name + " added to cart";

            toast.classList.add("show");

            setTimeout(function(){

                toast.classList.remove("show");

            },2000);

        }

    })
    .catch(error => {

        console.error("Error:", error);

    });

}


/* ================= TESTIMONIAL SLIDER ================= */

const testimonials = document.querySelectorAll(".testimonial");
const dots = document.querySelectorAll(".dot");

if (testimonials.length && dots.length) {

    let currentTestimonial = 0;

    function showTestimonial(index){

        testimonials.forEach(t => t.classList.remove("active"));
        dots.forEach(d => d.classList.remove("active"));

        testimonials[index].classList.add("active");
        dots[index].classList.add("active");

    }

    dots.forEach((dot,index)=>{

        dot.addEventListener("click",()=>{

            currentTestimonial=index;

            showTestimonial(currentTestimonial);

        });

    });

    setInterval(()=>{

        currentTestimonial++;

        if(currentTestimonial >= testimonials.length){

            currentTestimonial = 0;

        }

        showTestimonial(currentTestimonial);

    },5000);

}



/* ================= SCROLL TO TOP ================= */

const scrollBtn = document.getElementById("scrollTopBtn");

if (scrollBtn) {

    window.addEventListener("scroll", () => {

        if (window.scrollY > 400) {

            scrollBtn.style.display = "flex";

        } else {

            scrollBtn.style.display = "none";

        }

    });

    scrollBtn.addEventListener("click", () => {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });

}


/* ================= MOBILE MENU ================= */

const menuToggle = document.getElementById("menuToggle");
const navLinks = document.querySelector(".nav-links");

if (menuToggle && navLinks) {

    menuToggle.addEventListener("click", () => {

        navLinks.classList.toggle("active");

        const icon = menuToggle.querySelector("i");

        if (navLinks.classList.contains("active")) {

            icon.classList.remove("bi-list");
            icon.classList.add("bi-x-lg");

        } else {

            icon.classList.remove("bi-x-lg");
            icon.classList.add("bi-list");

        }

    });

}


const navItems = document.querySelectorAll(".nav-links a");

navItems.forEach(item => {

    item.addEventListener("click", () => {

        if (navLinks) {

            navLinks.classList.remove("active");

            const icon = menuToggle?.querySelector("i");

            if (icon) {

                icon.classList.remove("bi-x-lg");
                icon.classList.add("bi-list");

            }

        }

    });

});



/* ================= SCROLL REVEAL ================= */

const revealElements = document.querySelectorAll(".reveal");

function revealOnScroll(){

    const windowHeight = window.innerHeight;

    revealElements.forEach(element=>{

        const top = element.getBoundingClientRect().top;

        if(top < windowHeight - 100){

            element.classList.add("active");

        }

    });

}

window.addEventListener("scroll", revealOnScroll);

revealOnScroll();




/* ================= LIGHTBOX ================= */

const galleryImages = document.querySelectorAll(".gallery-item img");

const lightbox = document.getElementById("lightbox");

const lightboxImg = document.getElementById("lightboxImage");

const closeLightbox = document.getElementById("closeLightbox");

if(galleryImages.length){

    galleryImages.forEach(img=>{

        img.addEventListener("click",()=>{

            lightbox.style.display="flex";

            lightboxImg.src=img.src;

        });

    });

}

if(closeLightbox){

    closeLightbox.onclick=function(){

        lightbox.style.display="none";

    }

}

if(lightbox){

    lightbox.onclick=function(e){

        if(e.target===lightbox){

            lightbox.style.display="none";

        }

    }

}



/* ================= PRELOADER ================= */

window.addEventListener("load", () => {

    const preloader = document.getElementById("preloader");

    if(preloader){

        preloader.classList.add("hide");

    }

});
/* ================= HERO BACKGROUND SLIDER ================= */

const hero = document.querySelector(".hero");
const heroDots = document.querySelectorAll(".hero-scroll span");

const heroTitle = document.querySelector(".hero-title");
const heroSubtitle = document.querySelector(".hero-subtitle");
const heroDescription = document.querySelector(".hero-description");
const heroLeft = document.querySelector(".hero-left");

if (hero) {

    const slides = [

        {
            image: "/static/images/hero/hero_outside.jpg",
            title: "विरासत",
            subtitle: "Tradition Served Fresh",
            description: "Experience the authentic taste of Varhadi, Maharashtrian, Chinese and Fast Food delicacies made with fresh ingredients and traditional recipes."
        },

        {
            image: "/static/images/hero/hero_park2.jpg",
            title: "विरासत",
            subtitle: "Celebrate Every Occasion",
            description: "Enjoy memorable dining with family and friends in a peaceful atmosphere."
        },

        {
            image: "/static/images/hero/hero_terrace2.jpg",
            title: "विरासत",
            subtitle: "Every Meal Tells a Story",
            description: "Delicious food, warm hospitality and unforgettable moments await you."
        }

    ];

    let current = 0;

const bg1 = document.querySelector(".hero-bg-1");
const bg2 = document.querySelector(".hero-bg-2");

let showingFirst = true;

function showSlide(index){

    heroLeft.classList.add("slide-out");

    setTimeout(()=>{

        const nextImage = `url('${slides[index].image}')`;

        if(showingFirst){

            bg2.style.backgroundImage = nextImage;
            bg2.style.opacity = "1";
            bg1.style.opacity = "0";

        }else{

            bg1.style.backgroundImage = nextImage;
            bg1.style.opacity = "1";
            bg2.style.opacity = "0";

        }

        showingFirst = !showingFirst;

        heroTitle.textContent = slides[index].title;
        heroSubtitle.textContent = slides[index].subtitle;
        heroDescription.textContent = slides[index].description;

        heroLeft.classList.remove("slide-out");
        heroLeft.classList.add("slide-in");

        setTimeout(()=>{
            heroLeft.classList.remove("slide-in");
        },500);

    },300);

    heroDots.forEach(dot=>dot.classList.remove("active"));
    heroDots[index].classList.add("active");
}

    heroDots.forEach((dot,index)=>{

        dot.addEventListener("click",()=>{

            current=index;

            showSlide(current);

        });

    });

    showSlide(current);

    setInterval(()=>{

        current++;

        if(current>=slides.length){

            current=0;

        }

        showSlide(current);

    },5000);

}

/* ================= HERO PARALLAX ================= */

const heroSection = document.querySelector(".hero");

if(heroSection){

    window.addEventListener("scroll",()=>{

        const y = window.pageYOffset;

        heroSection.style.backgroundPosition = `center ${y*0.35}px`;

    });

}




/* ================= MENU CARD REVEAL ================= */

const menuCards = document.querySelectorAll(".menu-card");

const menuObserver = new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.classList.add("show-card");

        }

    });

},{
    threshold:.15
});

menuCards.forEach(card=>menuObserver.observe(card));



function openDishModal(name,price,image,description){

    document.getElementById("modalDishImage").src=image;
    document.getElementById("modalDishName").innerHTML=name;
    document.getElementById("modalDishPrice").innerHTML="₹"+price;
    document.getElementById("modalDishDescription").innerHTML=description;

    document.getElementById("dishModal").style.display="flex";

}

function closeDishModal(){

    document.getElementById("dishModal").style.display="none";

}


const navbar = document.querySelector(".navbar");
const navbarLogo = document.getElementById("navbarLogo");

window.addEventListener("scroll", () => {

    if(window.scrollY > 80){

        navbar.classList.add("navbar-scrolled");

        navbarLogo.src="/static/images/logo/logo_white.png";

    }else{

        navbar.classList.remove("navbar-scrolled");

        navbarLogo.src="/static/images/logo/logo_green.png";

    }

});



function toggleTable(){

    let type = document.getElementById("order_type").value;

    let tableDiv = document.getElementById("tableDiv");

    let table = document.getElementById("table_number");

    if(type === "Takeaway"){

        tableDiv.style.display = "none";

        table.required = false;

        table.value = "";

    }
    else{

        tableDiv.style.display = "block";

        table.required = true;

    }

}

window.onload = toggleTable;











