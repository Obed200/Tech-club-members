let slideIndex = 0;

function showSlides() {
    let slides = document.querySelectorAll('.slide');

    // Hide all slides
    slides.forEach(slide => slide.style.display = 'none');

    // Move to the next slide
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1; // Reset to first slide
    }

    // Show the current slide
    slides[slideIndex - 1].style.display = 'block';

    // Set timer for 3 seconds
    setTimeout(showSlides, 3000);
}

// Start the slideshow when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', showSlides);
