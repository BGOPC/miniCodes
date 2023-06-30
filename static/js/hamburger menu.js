function toggleHamburgerMenu() {
    const hamburgerMenu = document.getElementById('hamburger-menu');
    hamburgerMenu.classList.toggle('hidden');
}

document.addEventListener('click', (event) => {
    const hamburgerMenu = document.getElementById('hamburger-menu');
    const targetElement = event.target;
    if (!targetElement.closest('#hamburger-button') && !targetElement.closest('#hamburger-menu')) {
        hamburgerMenu.classList.add('hidden');
    }
});