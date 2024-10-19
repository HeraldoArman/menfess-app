var system_mode_btn = document.getElementsByClassName("icon-mode");
var body = document.getElementsByTagName("body")[0];
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
    });
});

for (let i = 0; i < system_mode_btn.length; i++) {
    system_mode_btn[i].addEventListener('click', function () {
        var paragraph = system_mode_btn[i].getElementsByTagName('p')[0];
        var icon_image = system_mode_btn[i].getElementsByTagName('img')[0];

        // Toggle tema
        if (body.getAttribute('data-bs-theme') === 'dark') {
            icon_image.setAttribute('src', icon_image.getAttribute('data-default-src').replace('moon.png', 'sun.png'));
            paragraph.textContent = "Light mode";
            body.setAttribute('data-bs-theme', 'light');
            localStorage.setItem('data-bs-theme', 'light');
        } else {
            icon_image.setAttribute('src', icon_image.getAttribute('data-default-src').replace('sun.png', 'moon.png'));
            paragraph.textContent = "Dark mode";
            body.setAttribute('data-bs-theme', 'dark');
            localStorage.setItem('data-bs-theme', 'dark');
        }
    });
}

function applySavedTheme() {
    const savedTheme = localStorage.getItem('data-bs-theme');
    const icon_image = system_mode_btn[0].getElementsByTagName('img')[0];
    const paragraph = system_mode_btn[0].getElementsByTagName('p')[0];

    if (savedTheme === 'dark') {
        body.setAttribute('data-bs-theme', 'dark');
        icon_image.setAttribute('src', icon_image.getAttribute('data-default-src').replace('sun.png', 'moon.png'));
        paragraph.textContent = "Dark mode";
    } else {
        body.setAttribute('data-bs-theme', 'light');
        icon_image.setAttribute('src', icon_image.getAttribute('data-default-src').replace('moon.png', 'sun.png'));
        paragraph.textContent = "Light mode";
    }
}




const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));

applySavedTheme();
