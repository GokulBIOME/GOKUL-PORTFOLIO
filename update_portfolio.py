from pathlib import Path

html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Gokularamanan K | Java Developer Portfolio</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <div class="brand">
        <div class="avatar"></div>
        <div>
          <p class="brand-title">Gokularamanan K</p>
          <p class="brand-subtitle">Java Developer | Biomedical Engineer</p>
        </div>
      </div>
      <nav>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#education">Education</a>
        <a href="#certifications">Certifications</a>
        <a href="#contact">Contact</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="hero" id="home">
      <div class="container hero-grid">
        <div class="hero-copy">
          <p class="hero-eyebrow">Hello, I'm</p>
          <h1>Gokularamanan K</h1>
          <p class="hero-subtitle">Java Developer • Biomedical Engineering Graduate</p>
          <p class="hero-text">Passionate about building scalable applications, solving real-world problems, and continuously improving software development skills in Java, SQL, Android, and biomedical systems.</p>
          <div class="hero-actions">
            <a class="button button-primary" href="resume.pdf" download>Download Resume</a>
            <a class="button button-secondary" href="#projects">View Projects</a>
          </div>
          <div class="hero-links">
            <a href="https://github.com/GokulBIOME" target="_blank">GitHub</a>
            <a href="https://www.linkedin.com/in/gokularamanan-k-48223266" target="_blank">LinkedIn</a>
            <a href="mailto:gokul301016@gmail.com">Email</a>
          </div>
        </div>
        <div class="hero-card">
          <div class="hero-card-header">
            <p class="eyebrow">Java Developer</p>
            <h2>Biomedical Engineering Graduate</h2>
          </div>
          <div class="hero-stats">
            <div class="stat">
              <strong>8.48</strong>
              <span>CGPA</span>
            </div>
            <div class="stat">
              <strong>3+</strong>
              <span>Projects</span>
            </div>
            <div class="stat">
              <strong>5+</strong>
              <span>Certifications</span>
            </div>
            <div class="stat">
              <strong>6</strong>
              <span>Presentations</span>
            </div>
          </div>
          <div class="hero-contact-card">
            <p><strong>Email</strong></p>
            <a href="mailto:gokul301016@gmail.com">gokul301016@gmail.com</a>
            <p><strong>Phone</strong></p>
            <a href="tel:+917448345598">+91 74483 45598</a>
          </div>
        </div>
      </div>
    </section>

    <section id="about" class="section">
      <div class="container">
        <div class="section-header">
          <p class="eyebrow">About Me</p>
          <h2>Java Developer • Biomedical Engineering Graduate</h2>
          <p>I am a Biomedical Engineering graduate with strong practical experience in Java, SQL, Android, MATLAB, and embedded healthcare systems. I enjoy building real-world applications, solving complex problems, and learning modern software practices.</p>
        </div>
        <div class="about-grid">
          <div class="about-card">
            <h3>Professional Summary</h3>
            <p>Experienced with Java programming, database systems, Android development, and medical device integration. I have developed projects in hospital management, machine learning models, and prosthetic control systems.</p>
          </div>
          <div class="about-card">
            <h3>Profile</h3>
            <ul>
              <li>Java Developer</li>
              <li>Biomedical Engineering Graduate</li>
              <li>Android Studio</li>
              <li>SQL, JDBC, MySQL</li>
              <li>MATLAB & Data Analysis</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section id="skills" class="section">
      <div class="container">
        <div class="section-header">
          <p class="eyebrow">Technical Skills</p>
          <h2>What I build</h2>
        </div>
        <div class="skill-grid">
          <div class="skill-card"><h3>Java</h3><p>Java development for applications, data processing, and system logic.</p></div>
          <div class="skill-card"><h3>SQL</h3><p>Database management, JDBC integration, and query optimization.</p></div>
          <div class="skill-card"><h3>Android</h3><p>Mobile app development, sensors, and user interface design.</p></div>
          <div class="skill-card"><h3>MATLAB</h3><p>Data analysis, signal processing, and research modeling.</p></div>
          <div class="skill-card"><h3>IoT</h3><p>Embedded prototypes, Arduino, and ThingSpeak data flows.</p></div>
          <div class="skill-card"><h3>Diagnostics</h3><p>Medical system research, classification models, and predictive tools.</p></div>
        </div>
      </div>
    </section>

    <section id="projects" class="section">
      <div class="container">
        <div class="section-header">
          <p class="eyebrow">Featured Projects</p>
          <h2>Projects I have delivered</h2>
        </div>
        <div class="project-grid">
          <div class="project-card">
            <h3>Alzheimer's Detection Using GNN</h3>
            <p>Developed a Graph Neural Network model with fMRI datasets to predict Alzheimer's disease.</p>
            <p class="project-tags">GNN • Machine Learning</p>
          </div>
          <div class="project-card">
            <h3>Hospital Management System</h3>
            <p>Built a Java application with JDBC and MySQL for managing patients, doctors, and appointments.</p>
            <p class="project-tags">Java • JDBC • MySQL</p>
          </div>
          <div class="project-card">
            <h3>Low Cost Myoelectric Bionic Arm</h3>
            <p>Prototyped a low-cost myoelectric prosthetic using EMG sensors and control logic.</p>
            <p class="project-tags">Arduino • EMG</p>
          </div>
          <div class="project-card">
            <h3>Smartwatch Alcohol Detection</h3>
            <p>Designed an IoT wearable concept for alcohol detection using sweat analysis.</p>
            <p class="project-tags">IoT • Wearables</p>
          </div>
        </div>
      </div>
    </section>

    <section id="education" class="section">
      <div class="container">
        <div class="section-header">
          <p class="eyebrow">Education</p>
          <h2>Academic foundation</h2>
        </div>
        <div class="education-grid">
          <div class="education-card"><h3>B.Tech - Biomedical Engineering</h3><p>Sri Manakula Vinayagar Engineering College</p><span>2022 - 2026 • CGPA 8.48</span></div>
          <div class="education-card"><h3>Higher Secondary (HSC)</h3><p>Amalorpavam Higher Secondary School</p><span>2021 • 87%</span></div>
          <div class="education-card"><h3>Secondary School (SSLC)</h3><p>Amalorpavam Higher Secondary School</p><span>2019 • 83%</span></div>
        </div>
      </div>
    </section>

    <section id="certifications" class="section">
      <div class="container">
        <div class="section-header">
          <p class="eyebrow">Certifications</p>
          <h2>Credentials and badges</h2>
        </div>
        <div class="cert-grid">
          <div class="cert-card"><h3>Java (Basic)</h3><p>HackerRank Java fundamentals certification.</p></div>
          <div class="cert-card"><h3>Java Gold Badge</h3><p>Advanced Java programming and problem solving.</p></div>
          <div class="cert-card"><h3>SQL Bronze Badge</h3><p>Database and query skill validation.</p></div>
          <div class="cert-card"><h3>AWS Academy</h3><p>Machine Learning Foundations coursework.</p></div>
          <div class="cert-card"><h3>NPTEL IoT</h3><p>Internet of Things systems and applications.</p></div>
        </div>
      </div>
    </section>

    <section id="coding" class="section">
      <div class="container">
        <div class="section-header">
          <p class="eyebrow">Coding Profiles</p>
          <h2>Online credentials</h2>
        </div>
        <div class="coding-grid">
          <div class="coding-card"><h3>GitHub</h3><p><a href="https://github.com/GokulBIOME" target="_blank">github.com/GokulBIOME</a></p></div>
          <div class="coding-card"><h3>HackerRank</h3><p>Java Gold Badge • SQL Bronze Badge • Java (Basic)</p></div>
          <div class="coding-card"><h3>Certifications</h3><p>MATLAB Onramp • Embedded Systems • NPTEL</p></div>
        </div>
      </div>
    </section>

    <section id="contact" class="section">
      <div class="container">
        <div class="section-header">
          <p class="eyebrow">Contact</p>
          <h2>Let's connect</h2>
        </div>
        <div class="contact-grid">
          <div class="contact-card"><h3>Phone</h3><p><a href="tel:+917448345598">+91 74483 45598</a></p></div>
          <div class="contact-card"><h3>Email</h3><p><a href="mailto:gokul301016@gmail.com">gokul301016@gmail.com</a></p></div>
          <div class="contact-card"><h3>LinkedIn</h3><p><a href="https://www.linkedin.com/in/gokularamanan-k-48223266" target="_blank">linkedin.com/in/gokularamanan-k-48223266</a></p></div>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container footer-inner">
      <p>Designed & Developed by Gokularamanan K</p>
      <p>© 2026 Gokularamanan K</p>
    </div>
  </footer>
</body>
</html>
'''

css = '''/* Global */
:root {
  color-scheme: dark;
  color: #f8fafc;
  background: #020617;
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.65;
  font-size: 16px;
  --surface: rgba(15, 23, 42, 0.95);
  --border: rgba(148, 163, 184, 0.18);
  --primary: #2563eb;
  --text-muted: #94a3b8;
  --text-bright: #e2e8f0;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  min-height: 100vh;
  background: radial-gradient(circle at top, rgba(37, 99, 235, 0.08), transparent 30%), linear-gradient(180deg, #020617 0%, #070d21 100%);
}

img {
  max-width: 100%;
}

a {
  color: inherit;
}

button,
a {
  font: inherit;
}

.container {
  width: min(1160px, calc(100% - 2rem));
  margin: 0 auto;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  background: rgba(4, 8, 20, 0.92);
  border-bottom: 1px solid rgba(148, 163, 184, 0.14);
  backdrop-filter: blur(14px);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 0;
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, #2563eb, #9333ea);
  box-shadow: 0 18px 36px rgba(37, 99, 235, 0.2);
}

.brand-title {
  margin: 0;
  font-weight: 700;
  letter-spacing: 0.03em;
}

.brand-subtitle {
  margin: 0.2rem 0 0;
  color: var(--text-muted);
  font-size: 0.94rem;
}

nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
}

nav a {
  color: var(--text-bright);
  text-decoration: none;
  padding: 0.7rem 0.9rem;
  border-radius: 999px;
  transition: transform 0.2s ease, background 0.2s ease;
}

nav a:hover,
nav a:focus-visible {
  transform: translateY(-1px);
  background: rgba(37, 99, 235, 0.14);
}

.section {
  padding: 3rem 0;
}

.hero {
  padding: 4rem 0 3rem;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
  gap: 2rem;
  align-items: start;
}

.hero-eyebrow {
  margin: 0 0 1rem;
  color: #93c5fd;
  font-size: 0.95rem;
  text-transform: uppercase;
  letter-spacing: 0.22em;
}

.hero-copy h1 {
  margin: 0;
  font-size: clamp(3rem, 5vw, 4.5rem);
  line-height: 1.02;
}

.hero-subtitle {
  margin: 0.85rem 0 1.3rem;
  color: var(--text-muted);
  font-size: 1.05rem;
}

.hero-text {
  max-width: 700px;
  margin: 0 0 1.8rem;
  color: var(--text-muted);
  font-size: 1rem;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.85rem;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.95rem 1.6rem;
  border-radius: 999px;
  font-weight: 700;
  text-decoration: none;
  transition: transform 0.2s ease, background 0.2s ease;
}

.button-primary {
  background: var(--primary);
  color: #fff;
}

.button-secondary {
  background: rgba(255, 255, 255, 0.08);
  color: var(--text-bright);
  border: 1px solid rgba(226, 232, 240, 0.12);
}

.button:hover,
.button:focus-visible {
  transform: translateY(-1px);
}

.hero-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.5rem;
}

.hero-links a {
  color: #93c5fd;
  text-decoration: none;
  font-weight: 600;
}

.hero-card {
  background: rgba(15, 23, 42, 0.95);
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 28px;
  padding: 2rem;
}

.hero-card-header .eyebrow {
  margin-bottom: 1rem;
}

.hero-card h2 {
  margin: 0;
  font-size: 1.7rem;
}

.hero-stats {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  margin-top: 1.8rem;
}

.stat {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(148, 163, 184, 0.1);
  border-radius: 20px;
  padding: 1rem;
}

.stat strong {
  display: block;
  font-size: 1.8rem;
  color: #fff;
}

.stat span {
  color: var(--text-muted);
}

.hero-contact-card {
  margin-top: 2rem;
  padding: 1.5rem;
  background: rgba(255, 255, 255, 0.04);
  border: 1px dashed rgba(148, 163, 184, 0.16);
  border-radius: 20px;
}

.hero-contact-card strong {
  display: block;
  margin-bottom: 0.5rem;
}

.hero-contact-card a {
  display: inline-block;
  color: #93c5fd;
  text-decoration: none;
  margin-bottom: 0.75rem;
}

.section-header {
  max-width: 760px;
  margin-bottom: 2rem;
}

.section-header .eyebrow {
  margin: 0 0 0.7rem;
}

.section-header h2 {
  margin: 0;
  font-size: clamp(2rem, 3vw, 2.8rem);
}

.section-header p {
  margin: 1rem 0 0;
  color: var(--text-muted);
}

.about-grid,
.skill-grid,
.project-grid,
.education-grid,
.cert-grid,
.coding-grid,
.contact-grid {
  display: grid;
  gap: 1.4rem;
}

.about-grid {
  grid-template-columns: 1.3fr 0.7fr;
}

.about-card,
.skill-card,
.project-card,
.education-card,
.cert-card,
.coding-card,
.contact-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 1.7rem;
}

.about-card h3,
.skill-card h3,
.project-card h3,
.education-card h3,
.cert-card h3,
.coding-card h3,
.contact-card h3 {
  margin-top: 0;
}

.about-card ul {
  padding: 0;
  margin: 1rem 0 0;
  list-style: none;
  color: var(--text-muted);
}

.about-card li {
  margin-bottom: 0.6rem;
}

.skill-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.skill-card p,
.about-card p,
.education-card p,
.cert-card p,
.coding-card p,
.contact-card p {
  margin: 0;
  color: var(--text-muted);
}

.project-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.project-card {
  min-height: 200px;
}

.project-tags {
  margin-top: 1rem;
  color: #93c5fd;
  font-weight: 700;
}

.education-grid,
.cert-grid,
.coding-grid,
.contact-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.education-card span {
  display: block;
  margin-top: 0.75rem;
  color: var(--text-muted);
}

.coding-card a,
.contact-card a {
  color: #93c5fd;
  text-decoration: none;
}

.footer-inner {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: center;
  padding: 1.5rem 0 0;
}

.site-footer {
  border-top: 1px solid rgba(148, 163, 184, 0.14);
}

.site-footer p {
  margin: 0;
  color: var(--text-muted);
}

@media (max-width: 980px) {
  .hero-grid,
  .about-grid,
  .skill-grid,
  .project-grid,
  .education-grid,
  .cert-grid,
  .coding-grid,
  .contact-grid,
  .footer-inner {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 700px) {
  .header-inner {
    flex-direction: column;
    align-items: flex-start;
  }

  nav {
    gap: 0.5rem;
  }

  .hero {
    padding-top: 3rem;
  }

  .hero-copy h1 {
    font-size: 2.7rem;
  }
}
'''

Path('index.html').write_text(html, encoding='utf-8')
Path('styles.css').write_text(css, encoding='utf-8')
