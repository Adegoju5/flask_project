function toggleMenu() {
    const mobileNav = document.querySelector('.mobile-nav');
    const upIcon = document.querySelector('.drop_up_icon');
    const downIcon = document.querySelector('.drop_down_icon');
    if (mobileNav.style.display === 'block' || getComputedStyle(mobileNav).display === 'block') {
        mobileNav.style.display = 'none';
        downIcon.style.display = 'block'
        upIcon.style.display = 'none'

    } else {
        mobileNav.style.display = 'block';
        downIcon.style.display = 'none'
        upIcon.style.display = 'block'
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const menuIcon = document.querySelector('.menu-icon');
    menuIcon.addEventListener('click', toggleMenu);
});
