$(".faq-plus").on('click', function(){
    $(this).parent().parent().find('.faq-body').slideToggle();
});

let plus = document.querySelector('.faq-plus');
let navbar = document.querySelector('.faq-body');

plus.addEventListener('click', function(){
    menu.classList.toggle('minus');
    navbar.classList.toggle('open');
});