document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function () {
        const submitButton = form.querySelector('button');
        submitButton.innerHTML = 'Submitting...';
        submitButton.disabled = true;
    });
});
