#!/usr/bin/env python3
"""Generate static site for balbusspeech.com — Clean teal/medical professional theme"""
import os, json

DOMAIN = "balbusspeech.com"
PAGES_URL = "balbusspeech.pages.dev"
SITE_NAME = "Balbus Speech"
TAGLINE = "Unlocking Fluent Communication"

img_dir = "images"
all_images = sorted([f for f in os.listdir(img_dir) if f.endswith('.webp')])

posts = [
    {"slug": "the-ultimate-guide-to-choosing-effective-speech-therapy-tools-and-techniques", "title": "The Ultimate Guide to Choosing Effective Speech Therapy Tools and Techniques", "date": "2024-11-30", "excerpt": "Speech therapy is a specialized form of intervention designed to assist individuals in improving their communication skills."},
    {"slug": "mastering-fluency-your-guide-to-effective-speech-improvement-tutorials", "title": "Mastering Fluency: Your Guide to Effective Speech Improvement Tutorials", "date": "2024-11-30", "excerpt": "Speech fluency refers to the smoothness, speed, and flow of speech during communication."},
    {"slug": "maximize-your-online-speech-therapy-sessions-essential-wifi-tips-for-smooth-communication", "title": "Maximize Your Online Speech Therapy Sessions: Essential WiFi Tips", "date": "2025-08-19", "excerpt": "A reliable WiFi connection is a fundamental requirement for effective online speech therapy sessions."},
    {"slug": "enhance-your-voice-therapy-for-improved-vocal-quality", "title": "Enhance Your Voice: Therapy for Improved Vocal Quality", "date": "2024-11-30", "excerpt": "Voice Therapy is a specialized form of treatment designed to help individuals with various voice disorders."},
    {"slug": "engaging-articulation-therapy-methods-for-clear-speech", "title": "Engaging Articulation Therapy Methods for Clear Speech", "date": "2024-11-30", "excerpt": "Articulation Therapy helps individuals improve their ability to produce speech sounds correctly."},
    {"slug": "effective-speech-therapy-exercises-to-practice-at-home", "title": "Effective Speech Therapy Exercises to Practice at Home", "date": "2024-11-30", "excerpt": "Speech Therapy Exercises are essential tools for individuals seeking to improve their communication abilities."},
    {"slug": "effective-speech-therapy-strategies-for-adults-with-challenges", "title": "Effective Speech Therapy Strategies for Adults with Challenges", "date": "2024-11-30", "excerpt": "Speech therapy for adults helps individuals recover from speech and language disorders."},
    {"slug": "understanding-and-managing-fluency-disorders-in-speech", "title": "Understanding and Managing Fluency Disorders in Speech", "date": "2024-11-30", "excerpt": "Fluency Disorders are communication disorders that impact the smoothness and rhythm of speech."},
    {"slug": "unlocking-online-speech-therapy-benefits-of-virtual-sessions", "title": "Unlocking Online Speech Therapy: Benefits of Virtual Sessions", "date": "2024-11-30", "excerpt": "Online Speech Therapy is revolutionizing the way individuals with communication challenges receive support."},
    {"slug": "unlocking-potential-effective-speech-therapy-for-children", "title": "Unlocking Potential: Effective Speech Therapy for Children", "date": "2024-11-30", "excerpt": "Speech therapy for children is a vital aspect of early childhood development."},
]

NAV = [("Home", "/"), ("About", "/about/"), ("Articles", "/posts/"), ("Contact", "/contact-us/")]

def header(title, desc="", canonical="/"):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc or title}">
<link rel="canonical" href="https://{PAGES_URL}{canonical}">
<link rel="icon" href="/images/favicon.png">
<link rel="stylesheet" href="/css/style.css">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc or title}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://{PAGES_URL}{canonical}">
</head>
<body>
<header class="header">
  <div class="header__inner">
    <a href="/" class="header__logo">{SITE_NAME}</a>
    <nav class="header__nav">
      <button class="menu-toggle" aria-label="Menu">&#9776;</button>
      <ul class="nav__list">
        {''.join(f'<li><a href="{url}">{name}</a></li>' for name, url in NAV)}
      </ul>
    </nav>
  </div>
</header>
'''

FOOTER = f'''
<footer class="footer">
  <div class="footer__inner">
    <div class="footer__col">
      <h3>{SITE_NAME}</h3>
      <p>{TAGLINE}. Your trusted partner in enhancing communication skills for individuals of all ages through evidence-based speech therapy.</p>
    </div>
    <div class="footer__col">
      <h3>Services</h3>
      <ul>
        <li>Speech Therapy</li>
        <li>Voice Therapy</li>
        <li>Fluency Disorders</li>
        <li>Articulation Therapy</li>
        <li>Online Sessions</li>
      </ul>
    </div>
    <div class="footer__col">
      <h3>Links</h3>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about/">About</a></li>
        <li><a href="/posts/">Articles</a></li>
        <li><a href="/contact-us/">Contact</a></li>
        <li><a href="/privacy/">Privacy</a></li>
        <li><a href="/terms/">Terms</a></li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <p>&copy; 2024 {SITE_NAME}. All rights reserved.</p>
  </div>
</footer>
<script>
document.querySelector('.menu-toggle').addEventListener('click', function() {{
  document.querySelector('.nav__list').classList.toggle('active');
}});
</script>
</body>
</html>'''

def post_card(post, idx):
    img = all_images[idx % len(all_images)] if all_images else ""
    return f'''<article class="card">
  <a href="/posts/{post['slug']}/">
    {f'<img src="/images/{img}" alt="{post["title"]}" class="card__img" loading="lazy">' if img else ''}
    <div class="card__body">
      <h2 class="card__title">{post['title']}</h2>
      <time class="card__date">{post['date']}</time>
      <p class="card__excerpt">{post['excerpt']}</p>
    </div>
  </a>
</article>'''

def write(path, content):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# Homepage
home_schema = json.dumps({"@context":"https://schema.org","@type":"MedicalBusiness","name":SITE_NAME,"url":f"https://{PAGES_URL}/","description":"Speech therapy services for individuals of all ages","medicalSpecialty":"SpeechPathology"}, indent=2)
home = header(f"{SITE_NAME} - {TAGLINE}", "Your trusted partner in enhancing communication skills through evidence-based speech therapy.", "/")
home += f'<script type="application/ld+json">{home_schema}</script>\n'
home += '<main class="main">\n<section class="hero">\n'
home += f'<div class="hero__content"><h1>{SITE_NAME}</h1>\n<p class="hero__tagline">{TAGLINE}</p>\n'
home += '<p>Welcome to Balbus Speech Therapy, your trusted partner in enhancing communication skills for individuals of all ages. Our dedicated team of speech-language pathologists is committed to providing exceptional speech therapy services tailored to meet your unique needs.</p>\n'
home += '<p>Whether you are seeking support for stuttering, language delays, voice disorders, or any other speech-related challenges, our experienced clinicians utilize the latest evidence-based techniques to help you reach your communication goals.</p>\n'
home += '<a href="/about/" class="btn">Learn About Us</a>\n</div></section>\n'
home += '<section class="posts-grid">\n<h2>Resources & Articles</h2>\n<div class="grid">\n'
for i, p in enumerate(posts[:6]):
    home += post_card(p, i)
home += '</div>\n<div class="center"><a href="/posts/" class="btn btn--outline">View All Articles</a></div>\n</section>\n</main>\n'
home += FOOTER
write("index.html", home)

# About
about = header("About Balbus Speech | Your Partner in Effective Communication", "Learn about Balbus Speech and our mission to empower communication.", "/about/")
about += '''<main class="main"><article class="page">
<h1>About Balbus Speech</h1>
<p>At Balbus Speech, we believe that effective communication is the cornerstone of personal and professional success. Our mission is to empower individuals with the skills and confidence to express themselves clearly and persuasively.</p>
<h2>Our Mission</h2>
<p>Founded by speech experts with a passion for helping others, Balbus Speech offers a range of services designed to address a variety of speech and language needs. Our team of certified speech-language pathologists brings years of experience and a deep understanding of the science behind communication.</p>
<h2>Our Approach</h2>
<p>We believe in a personalized approach to therapy, recognizing that each individual has distinct strengths and areas for growth. Our comprehensive evaluations lay the foundation for customized treatment plans designed to foster improvement and confidence in your speaking abilities. We utilize evidence-based techniques combined with the latest research to ensure the most effective outcomes for our clients.</p>
<h2>Who We Serve</h2>
<p>Our services cater to individuals of all ages — from children experiencing language delays to adults seeking to improve their public speaking skills or recover from speech-affecting conditions. We work with stuttering, articulation disorders, voice disorders, fluency challenges, language processing difficulties, and more.</p>
<h2>Our Environment</h2>
<p>Our inviting and supportive environment encourages both children and adults to engage actively in their therapy journey. We prioritize collaboration with families and caregivers to ensure that the strategies learned in therapy can be practiced and reinforced at home. We also offer convenient online therapy sessions for those who prefer virtual appointments.</p>
<h2>Get Started</h2>
<p>Join us at Balbus Speech, where communication thrives and confidence grows. Take the first step towards better speech and language skills by contacting us today to schedule your evaluation or consultation.</p>
</article></main>
''' + FOOTER
write("about/index.html", about)

# Posts index
posts_page = header("Articles — Balbus Speech", "Speech therapy articles, guides, and resources.", "/posts/")
posts_page += '<main class="main"><h1>Articles & Resources</h1><div class="grid">\n'
for i, p in enumerate(posts):
    posts_page += post_card(p, i)
posts_page += '</div></main>\n' + FOOTER
write("posts/index.html", posts_page)

# Contact
contact = header("Contact Us - Balbus Speech", "Get in touch with Balbus Speech for speech therapy services.", "/contact-us/")
contact += '''<main class="main"><article class="page">
<h1>Contact Us</h1>
<p>We're glad you're here! At Balbus Speech, we value every opportunity to communicate with our clients. If you have any questions, need assistance, or would like to learn more about our speech therapy services, please don't hesitate to reach out!</p>
<div class="contact-info">
<h2>How to Contact Us</h2>
<ul>
<li><strong>Phone:</strong> 1-800-123-4567</li>
<li><strong>Email:</strong> info@balbusspeech.com</li>
</ul>
</div>
<h2>Schedule a Consultation</h2>
<p>Ready to take the first step towards better communication? Contact us today to schedule an initial evaluation or consultation. Our team will work with you to understand your needs and develop a personalized treatment plan.</p>
<h2>Online Therapy Available</h2>
<p>Can't make it to our office? We offer comprehensive online speech therapy sessions that provide the same quality of care from the comfort of your home. Our virtual platform is secure, easy to use, and designed to facilitate effective therapy sessions.</p>
<h2>Office Hours</h2>
<p>Monday – Friday: 8:00 AM – 6:00 PM<br>Saturday: By appointment only<br>Sunday: Closed</p>
</article></main>
''' + FOOTER
write("contact-us/index.html", contact)

# Privacy
privacy = header("Privacy Policy - Balbus Speech", "Balbus Speech privacy policy.", "/privacy/")
privacy += '''<main class="main"><article class="page">
<h1>Privacy Policy</h1>
<p>At Balbus Speech, your privacy is of utmost importance to us. This Privacy Policy outlines how we collect, use, and protect your personal information when you visit our website.</p>
<h2>Information We Collect</h2>
<p>We may collect personal information that you provide to us directly, such as your name, email address, and any other details you submit through our contact forms or when scheduling appointments.</p>
<h2>How We Use Your Information</h2>
<p>We use the information we collect to provide our speech therapy services, communicate with you about appointments and services, improve our website, and comply with legal obligations.</p>
<h2>Data Protection</h2>
<p>We implement appropriate security measures to protect your personal information. We do not sell or share your personal information with third parties for marketing purposes.</p>
<h2>HIPAA Compliance</h2>
<p>As a healthcare provider, we adhere to HIPAA regulations regarding the protection of patient health information. Your therapy records and personal health information are handled with the highest level of confidentiality.</p>
<h2>Contact</h2>
<p>If you have questions about this Privacy Policy, please contact us at info@balbusspeech.com.</p>
</article></main>
''' + FOOTER
write("privacy/index.html", privacy)

# Terms
terms = header("Terms of Service - Balbus Speech", "Balbus Speech terms of service.", "/terms/")
terms += '''<main class="main"><article class="page">
<h1>Terms of Service</h1>
<p>Welcome to Balbus Speech! By using our website and services, you agree to comply with and be bound by the following terms and conditions.</p>
<h2>1. Acceptance of Terms</h2>
<p>By accessing or using the Balbus Speech website and services, you acknowledge that you have read, understood, and agree to be bound by these Terms of Service.</p>
<h2>2. Services</h2>
<p>Balbus Speech provides speech therapy services including evaluations, treatment plans, and therapy sessions. Our services are provided by licensed speech-language pathologists.</p>
<h2>3. Medical Disclaimer</h2>
<p>The information provided on our website is for educational purposes only and should not be considered medical advice. Always consult with a qualified healthcare professional for diagnosis and treatment.</p>
<h2>4. Intellectual Property</h2>
<p>All content on this website, including text, graphics, logos, and images, is the property of Balbus Speech and is protected by copyright laws.</p>
<h2>5. Contact</h2>
<p>For questions about these terms, please contact us at info@balbusspeech.com.</p>
</article></main>
''' + FOOTER
write("terms/index.html", terms)

# Post content
generic_speech_content = """<h2>Understanding the Importance of Communication</h2>
<p>Effective communication is fundamental to every aspect of our lives — from personal relationships to professional success. When speech or language challenges arise, they can significantly impact an individual's confidence, social interactions, and overall quality of life. That's where professional speech therapy comes in.</p>
<h2>Evidence-Based Approaches</h2>
<p>Modern speech therapy relies on evidence-based practices that have been proven effective through rigorous research. These approaches are tailored to each individual's specific needs, taking into account their age, the nature of their communication challenge, and their personal goals. Whether working on articulation, fluency, voice quality, or language comprehension, therapists draw from a rich toolkit of techniques and strategies.</p>
<h2>The Role of Practice</h2>
<p>Consistent practice is key to making progress in speech therapy. While sessions with a speech-language pathologist provide expert guidance and structured activities, the work done between sessions is equally important. Home practice exercises, daily communication activities, and real-world application of learned skills all contribute to faster and more lasting improvement.</p>
<h2>Technology and Innovation</h2>
<p>The field of speech therapy continues to evolve with advances in technology. Online therapy platforms, speech analysis apps, and interactive exercises have expanded access to quality care and provided new tools for practice and assessment. These innovations make it possible for individuals to receive therapy regardless of their location or schedule constraints.</p>
<h2>A Collaborative Journey</h2>
<p>Successful speech therapy is a collaborative effort involving the therapist, the client, and often family members or caregivers. Open communication, realistic goal-setting, and ongoing assessment ensure that therapy remains effective and responsive to the individual's evolving needs. At Balbus Speech, we're committed to partnering with you on your journey to better communication.</p>"""

for i, post in enumerate(posts):
    img = all_images[i % len(all_images)] if all_images else ""
    schema = json.dumps({"@context":"https://schema.org","@type":"Article","headline":post['title'],"datePublished":post['date'],"publisher":{"@type":"Organization","name":SITE_NAME}}, indent=2)
    
    related = [p for p in posts if p['slug'] != post['slug']][:3]
    related_html = '<div class="related"><h2>Related Articles</h2><div class="related__grid">'
    for r in related:
        related_html += f'<a href="/posts/{r["slug"]}/" class="related__item"><h3>{r["title"]}</h3><time>{r["date"]}</time></a>'
    related_html += '</div></div>'
    
    page = header(post['title'], post['excerpt'], f"/posts/{post['slug']}/")
    page += f'<script type="application/ld+json">{schema}</script>\n'
    page += f'<main class="main"><article class="post">\n'
    page += f'<h1>{post["title"]}</h1>\n<time class="post__date">{post["date"]}</time>\n'
    if img:
        page += f'<img src="/images/{img}" alt="{post["title"]}" class="post__img" loading="lazy">\n'
    page += f'<div class="content">{generic_speech_content}</div>\n'
    page += related_html
    page += '</article></main>\n'
    page += FOOTER
    write(f"posts/{post['slug']}/index.html", page)

# Sitemap
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
urls = ["/", "/about/", "/posts/", "/contact-us/", "/privacy/", "/terms/"]
urls += [f"/posts/{p['slug']}/" for p in posts]
for u in urls:
    sitemap += f'  <url><loc>https://{PAGES_URL}{u}</loc></url>\n'
sitemap += '</urlset>'
write("sitemap.xml", sitemap)

write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{PAGES_URL}/sitemap.xml\n")

print(f"Generated {len(urls)} pages for {SITE_NAME}")
