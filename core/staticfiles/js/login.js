
// Simple client-side validation + Persian error messages
// const form = document.getElementById('loginForm');
const username = document.getElementById('username');
const password = document.getElementById('password');
const usernameError = document.getElementById('usernameError');
const passwordError = document.getElementById('passwordError');
const toggle = document.getElementById('togglePwd');

toggle.addEventListener('click', () => {
    if (password.type === 'password') {
        password.type = 'text';
        toggle.textContent = '🙈';
    } else {
        password.type = 'password';
        toggle.textContent = '👁️';
    }
});

function showError(el, msg) {
    el.textContent = msg;
    el.style.display = 'block';
    el.previousElementSibling.classList.add('input-error');
}
function clearError(el) {
    el.textContent = '';
    el.style.display = 'none';
    if (el.previousElementSibling) el.previousElementSibling.classList.remove('input-error');
}

function validateEmailLike(v) {
    // loose check: has @ or contains non-space and length >=3
    return /@/.test(v) || (v && v.trim().length >= 3);
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    let ok = true;

    clearError(usernameError);
    clearError(passwordError);

    if (!username.value.trim()) {
        showError(usernameError, 'نام کاربری یا ایمیل نمی‌تواند خالی باشد.');
        ok = false;
    } else if (!validateEmailLike(username.value)) {
        showError(usernameError, 'لطفاً نام کاربری یا یک ایمیل معتبر وارد کنید.');
        ok = false;
    }

    if (!password.value) {
        showError(passwordError, 'پر کردن فیلد رمز عبور الزامی است.');
        ok = false;
    } else if (password.value.length < 6) {
        showError(passwordError, 'رمز عبور باید حداقل ۶ کاراکتر باشد.');
        ok = false;
    }

    if (!ok) {
        // یک Toast ساده با پیام خطا نمایش می‌دهیم
        showToast('خطا: لطفاً موارد مشخص شده را اصلاح کنید.');
        return;
    }

    // submit — اینجا باید درخواست به سرور ارسال شود
    showToast('در حال ارسال...');

    // برای دمو، شبیه‌سازی ارسال و موفقیت
    setTimeout(() => {
        showToast('ورود با موفقیت انجام شد.', false);
        // در عمل اینجا فرم را با fetch/post ارسال کنید یا window.location = ...
    }, 900);

});

// simple toast
function showToast(text, isError = true) {
    const t = document.createElement('div');
    t.textContent = text;
    t.style.position = 'fixed';
    t.style.bottom = '28px';
    t.style.left = '50%';
    t.style.transform = 'translateX(-50%)';
    t.style.padding = '10px 16px';
    t.style.borderRadius = '10px';
    t.style.boxShadow = '0 8px 30px rgba(2,6,23,0.12)';
    t.style.background = isError ? 'linear-gradient(90deg,#fff1f0,#ffeef0)' : 'linear-gradient(90deg,#ecfdf5,#e8fff0)';
    t.style.color = isError ? '#7f1d1d' : '#064e3b';
    t.style.fontWeight = '600';
    t.style.zIndex = 9999;
    document.body.appendChild(t);
    setTimeout(() => { t.style.opacity = '0'; t.style.transition = 'opacity .4s'; }, 2000);
    setTimeout(() => t.remove(), 2600);
}
