// Nút EN/VI dùng chung mọi trang: lưu lựa chọn vào localStorage, đổi tiêu đề tab theo ngôn ngữ.
(function () {
  function set(l) {
    var html = document.documentElement;
    html.setAttribute('data-lang', l);
    html.lang = l;
    try { localStorage.setItem('site-lang', l); } catch (e) {}
    document.querySelectorAll('[data-set-lang]').forEach(function (b) {
      b.classList.toggle('on', b.dataset.setLang === l);
      b.setAttribute('aria-pressed', b.dataset.setLang === l ? 'true' : 'false');
    });
    var t = document.body && document.body.dataset['title' + (l === 'vi' ? 'Vi' : 'En')];
    if (t) document.title = t;
  }
  document.querySelectorAll('[data-set-lang]').forEach(function (b) {
    b.addEventListener('click', function () { set(b.dataset.setLang); });
  });
  set(document.documentElement.getAttribute('data-lang') || 'en');
})();
