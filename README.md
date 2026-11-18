# Nguyen Van Vu Linh - Solutions Architect & Full Stack Developer

**Innovative and deadline-driven Fullstack Web Developer with over 9+ years of experience designing and developing websites for customers.**

Dedicated Solution Architect and Web Developer specializing in cloud architectures and driving agile transformations. Experienced in spearheading major digital overhauls within complex environments, resulting in significant enhancements to system flexibility and performance. Demonstrated proficiency in optimizing web functionality to improve data retrieval and workflow efficiencies.

## 📇 Contact Information

- **Address**: 137/5/2 Long Phuoc Street (Old District 9), Thu Duc City, HCMC
- **Telegram**: [@VuLinhBot](https://t.me/VuLinhBot)
- **Email**: quangvulinh@gmail.com
- **Website**: [www.quangvulinh.com](http://www.quangvulinh.com)
- **LinkedIn**: [quangvulinh](https://www.linkedin.com/in/quangvulinh/)

## 🛠️ Skills

- **Cloud & DevOps**: AWS (S3, RDS, SQS, CloudFront, WAF, CloudFormation/CDK), Docker, Kubernetes (ECS, EKS), Jenkins, CI/CD.
- **Backend**: Python (FastAPI, Django, Flask), .NET (Core, Framework), PHP (Laravel), Node.js.
- **Frontend**: JavaScript, React, Angular, HTML5, CSS3, Bootstrap.
- **Databases**: PostgreSQL, MSSQL, MongoDB, MySQL, Redis.
- **Big Data & ETL**: Kafka, Spark, Airflow, Yarn, Oozie.
- **Other**: LLM, Datalake, Bot development.

## 💼 Professional Experience

### Solutions Architect | Full Stack Developer
**FPT Telecom International Company** | *Aug 2022 - Present*

As a Solution Architect and Product Owner for digital conversion, I effectively communicate with both technical and non-technical audiences to design and implement solutions that meet client needs.

- **Amazing-chatbot**: Financial health insights chatbot using Python, .NET, NLU, Flask, Docker, K8s.
- **FTICareer.vn**: Recruitment portal using .NET, SQL Server, AWS SNS.
- **ASM**: IT asset management using Laravel, MySQL, Kafka.

### Web Developer | Full Stack Developer
**FPT Telecom** | *Oct 2016 - Jul 2022*

Specialized in solution design, development, and support for internal and external applications.

- **IHUB**: Internal platform using .NET Core, Kong Gateway, GRPC.
- **IDC Server**: Data center management portal using .NET Core, Kafka, Redis.
- **EDU FTC**: Training platform using .NET, ReactJS, SQL Server.
- **Member FTI**: Billing portal using Laravel, Python, ReactJS.
- **Cloud Insight**: Managed services application.
- **Member FPT**: Customer self-service portal using Flask, .NET, Laravel, Microservices.
- **Hi Gio Cloud**: Cloud service portal using Flask, PHP/Laravel.

### .NET Developer
**FPT Software** | *May 2015 - Oct 2016*

Designed, developed, and maintained platforms and applications based on WPF and Windows.

- **Windows 10 Setting**: System configuration tool.
- **Effect Management Application**: File management across devices.
- **Single Sign-On**: SSO for Windows environments.

## 🎓 Education & Certifications

### Education
- **Engineer's Degree in Information Technology**
  *Ho Chi Minh City University of Transport* | 2011 - 2015

### Certifications
- **AWS Certified Solutions Architect – Associate** (July 2023)
- **Google Associate Cloud Engineer** (Oct 2021)
- **Architecting with Google Kubernetes Engine** (Aug 2021)
- **Python and the Django Framework** (July 2021)
- **PMP Certificate**

## 🚀 Project Features (This Website)

Live at [quangvulinh.com](https://quangvulinh.com) — static site on AWS S3 + CloudFront.

- **Pages**: Home, About, Resume, Projects, Certificates, Contact, AI Bot.
- **Vietnamese / English switch**: `assets/js/lang.js` (remembers the choice, falls back to browser language).
- **Projects page**: freelance & own products — travel booking + CMS, AI meeting minutes, AI animated films for kids, Vietnamese TTS voice library (with audio samples).
- **Dynamic Certificates**: JavaScript-based certificate gallery.
- **Responsive Design**: Bootstrap 5 + custom `assets/css/site.css`.

## 🔧 Setup & Deploy

1.  Clone the repository and open `index.html` (or run `python -m http.server`).
2.  Deploy: upload changed files to the S3 bucket, e.g. `aws s3 cp projects.html s3://quangvulinh.com/projects.html --content-type "text/html; charset=utf-8"`. CloudFront caches HTML for ~5 minutes.

## 📄 License

Based on the [Kelly Bootstrap Template](https://bootstrapmade.com/kelly-free-bootstrap-cv-resume-html-template/).

## Plan (`/plan`)
`plan.html` = kế hoạch kiếm tiền (sơ đồ hướng, việc cần làm, nền tảng). Sinh từ `tools/plan_page.py` — sửa danh sách trong script, chạy `python tools/plan_page.py`, rồi upload `plan.html` lên S3 dưới 2 key `plan.html` và `plan` (content-type text/html) để mở được `quangvulinh.com/plan`.
