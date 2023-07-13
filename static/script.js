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

function handleSearch(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        const inputValue = document.getElementById("searchInput").value;
        const searchUrl = document.getElementById("searchInput").dataset.searchUrl;
        window.location.href = searchUrl + encodeURIComponent(inputValue);
    }
}
function toggleSearchResults(btn) {
    const codeList = document.getElementById("codeList");
    const questionList = document.getElementById("questionList");
    codeList.classList.toggle("hidden");
    questionList.classList.toggle("hidden");
    btn.innerHTML = btn.innerHTML === "Show Codes" ? "Show Questions" : "Show Codes";
}