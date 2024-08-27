function toggleMenu() {
    const menu = document.querySelector('.menu');
    menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
}


function openImage(src, caption) {
    document.getElementById('full-screen-view').style.display = 'flex';
    document.getElementById('full-image').src = src;
    document.getElementById('image-caption').innerText = caption;
}

function closeImage() {
    document.getElementById('full-screen-view').style.display = 'none';
    document.getElementById('full-image').src = '';
    document.getElementById('image-caption').innerText = '';
}




//aqui scripts do carrossel

let currentSlideIndex = 0;
const slides = document.querySelectorAll('.carousel-slide');
const dots = document.querySelectorAll('.carousel-dot');

function showSlide(index, direction) {
    slides.forEach((slide, i) => {
        slide.classList.remove('active', 'slide-in-left', 'slide-in-right', 'slide-out-left', 'slide-out-right');

        if (i === index) {
            slide.classList.add('active', direction === 'next' ? 'slide-in-right' : 'slide-in-left');
        } else if (i === currentSlideIndex) {
            slide.classList.add(direction === 'next' ? 'slide-out-left' : 'slide-out-right');
        }

        dots[i].classList.toggle('active', i === index);
    });

    currentSlideIndex = index;
}

function nextSlide() {
    const nextIndex = (currentSlideIndex + 1) % slides.length;
    showSlide(nextIndex, 'next');
}

function prevSlide() {
    const prevIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
    showSlide(prevIndex, 'prev');
}

function currentSlide(index) {
    if (index !== currentSlideIndex) {
        const direction = index > currentSlideIndex ? 'next' : 'prev';
        showSlide(index, direction);
    }
}

// Passar automaticamente os slides a cada 12 segundos
setInterval(nextSlide, 12000);

// Initialize the first slide as active
showSlide(currentSlideIndex, 'next');
