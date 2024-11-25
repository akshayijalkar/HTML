// Wait for DOM to load
document.addEventListener('DOMContentLoaded', () => {
    // Animation: Smooth Fade-In on Main Section
    const main = document.querySelector('main');
    main.style.opacity = 0;
    main.style.transition = "opacity 2s ease-in-out";
    setTimeout(() => {
        main.style.opacity = 1;
    }, 500);

    // Animation: Header Logo Hover Effect
    const logo = document.querySelector('.logo img');
    logo.addEventListener('mouseover', () => {
        logo.style.transform = "scale(1.1)";
        logo.style.transition = "transform 0.3s ease";
    });

    logo.addEventListener('mouseout', () => {
        logo.style.transform = "scale(1)";
    });

    // Search Input Animation
    const searchInput = document.querySelector('main input');
    searchInput.addEventListener('focus', () => {
        searchInput.style.boxShadow = "0 0 10px #ffd54f";
    });

    searchInput.addEventListener('blur', () => {
        searchInput.style.boxShadow = "none";
    });

    // Navigation Link Hover Animation
    const navLinks = document.querySelectorAll('header nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('mouseover', () => {
            link.style.textShadow = "0 0 5px #ffd54f";
        });
        link.addEventListener('mouseout', () => {
            link.style.textShadow = "none";
        });
    });
});
