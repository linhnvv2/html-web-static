document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('certificate-container');
    if (!container) return;

    const baseDir = 'assets/img/certifications/';

    certificates.forEach((cert, index) => {
        const delay = (index + 1) * 100; // Staggered animation delay
        const col = document.createElement('div');
        col.className = 'col-lg-4 col-md-6';
        col.setAttribute('data-aos', 'fade-up');
        col.setAttribute('data-aos-delay', delay);

        let iconContent = '';
        let typeLabel = '';

        if (cert.type === 'pdf') {
            iconContent = '<i class="bi bi-file-earmark-pdf"></i>';
            typeLabel = 'PDF';
        } else if (cert.type === 'image') {
            iconContent = `<img src="${baseDir}${cert.file}" alt="${cert.title}" class="img-fluid" style="max-height: 100px;">`;
            typeLabel = 'Image';
        }

        col.innerHTML = `
      <div class="service-item ${cert.color} position-relative">
        <div class="icon">
          ${iconContent}
        </div>
        <a href="${baseDir}${cert.file}" target="_blank" class="stretched-link">
          <h3>${cert.title}</h3>
        </a>
        <p>${typeLabel}</p>
      </div>
    `;

        container.appendChild(col);
    });
});
