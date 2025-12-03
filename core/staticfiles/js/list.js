document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.history-controls .form-btn');
    const searchInput = document.getElementById('search-input');
    const searchForm = document.getElementById('search');

    buttons[0].addEventListener('click', function () {
        window.location.href = '?is_ready=false&q=' + encodeURIComponent(searchInput.value);
    });

    buttons[1].addEventListener('click', function () {
        window.location.href = '?q=' + encodeURIComponent(searchInput.value);
    });

    buttons[2].addEventListener('click', function () {
        window.location.href = '?is_ready=true&q=' + encodeURIComponent(searchInput.value);
    });
});