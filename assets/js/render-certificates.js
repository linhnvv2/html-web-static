// Vẽ thẻ chứng chỉ theo style .lp-card (dùng chung site.css)
document.addEventListener('DOMContentLoaded', () => {
  const box = document.getElementById('certificate-container');
  if (!box || typeof certificates === 'undefined') return;
  const base = 'assets/img/certifications/';
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  certificates.forEach((c, i) => {
    const el = document.createElement('div');
    el.className = 'lp-card cert-card';
    el.setAttribute('data-aos', 'fade-up');
    el.setAttribute('data-aos-delay', String(Math.min(i, 5) * 60));
    const href = base + encodeURIComponent(c.file);
    const head = c.type === 'image'
      ? `<img class="thumb" src="${href}" alt="" loading="lazy">`
      : `<div class="ico"><i class="bi ${c.icon || 'bi-file-earmark-pdf'}"></i></div>`;
    el.innerHTML = `${head}
      <div class="kind">${c.type === 'pdf' ? 'PDF' : '<span lang="en">Image</span><span lang="vi">Ảnh</span>'}</div>
      <h3><a class="stretched-link" href="${href}" target="_blank" rel="noopener">${esc(c.title)}</a></h3>`;
    box.appendChild(el);
  });
});
