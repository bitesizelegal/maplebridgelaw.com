#!/usr/bin/env python3
"""Generate employee pages, vCards, and QR codes for Maple Bridge Law business cards."""

import os
import qrcode
from pathlib import Path

BASE_URL = "https://maplebridgelaw.com"
SCRIPT_DIR = Path(__file__).parent
TEAM_DIR = SCRIPT_DIR / "team"
VCARD_DIR = SCRIPT_DIR / "assets" / "vcards"
QR_DIR = SCRIPT_DIR / "assets" / "images" / "qr"

COMPANY = "Maple Bridge Law LLC"
OFFICE_PHONE = "678-460-8885"
ADDRESS = "416 Pirkle Ferry Road;Suite L-100;Cumming;GA;30040;US"
WEBSITE = "https://maplebridgelaw.com"

EMPLOYEES = [
    {
        "slug": "drew-jenkins",
        "first": "Drew",
        "last": "Jenkins",
        "role": "Attorney – AL, GA",
        "title": "Attorney",
        "email": "drew@maplebridgelaw.com",
        "phone": "678-572-1954",
        "photo": "drew.jpeg",
        "bio": "Drew Jenkins is the founder of Maple Bridge Law LLC in Atlanta, Georgia and AMA Capital, LLC in Birmingham, Alabama. He is an attorney licensed in both Alabama and Georgia who specializes in real estate transactions, financing, title, business structure, and international related projects. Drew handles both residential and commercial properties with deep experience in SBA, EB-5 financing, and 1031 transactions. He earned his B.A. degree, magna cum laude, from the University of Alabama at Birmingham and his J.D. degree from the University of Alabama School of Law.",
    },
    {
        "slug": "elliott-smith",
        "first": "Elliott",
        "last": "Smith",
        "role": "Attorney – GA",
        "title": "Attorney",
        "email": "elliott@maplebridgelaw.com",
        "phone": "678-541-8878",
        "photo": "elliott.jpeg",
        "bio": "Elliott Smith is an experienced attorney for title insurance underwriting, real estate closings, development and permitting. Formerly a member of Lipscomb &amp; Johnson law firm in Cumming, Elliott has been in private law practice for over 20 years. He is a graduate of Woodward Academy, the University of Georgia (B.A. Political Science, 1995), and Georgia State University College of Law (J.D., 2000). Elliott is an active member of the State Bar of Georgia and the Real Property Law Section.",
    },
    {
        "slug": "zovig-kelesarian",
        "first": "Zovig",
        "last": "Kelesarian",
        "role": "Foreign Law Consultant – GA",
        "title": "Foreign Law Consultant",
        "email": "zovig@jenkinstitle.com",
        "phone": None,
        "photo": "zovig.jpeg",
        "bio": "Zovig Kelesarian Berejiklian is an internationally trained attorney and certified Foreign Law Consultant in the State of Georgia, with extensive experience in cross-border legal matters and U.S. transactional practice. She holds a Law degree from the Universidad Central de Venezuela and completed postgraduate legal studies in Business Law and Alternative Dispute Resolution in Argentina. Fluent in Spanish, English, and Armenian, Zovig brings a global legal perspective and strong attention to detail to her work at Maple Bridge Law.",
    },
    {
        "slug": "amber-jenkins",
        "first": "Amber",
        "last": "Jenkins",
        "role": "Foreign Law Consultant – GA",
        "title": "Foreign Law Consultant",
        "email": "amber@maplebridgelaw.com",
        "phone": None,
        "photo": "amber-placeholder.svg",
        "hidden": True,
        "bio": "Graduate of the University of Alabama School of Law with an LLM in International &amp; Comparative Law as well as an LLM from Ocean University School of Law in Economic Law, Amber's expertise is the intersection of corporate, real estate, and immigration law. In addition to an impressive legal background, she is a licensed broker in Georgia. Her combined real estate experience through owning and managing properties and an active realtor's license in Georgia prepares her well to handle all sides of real estate transactions.",
    },
    {
        "slug": "mary-diaz",
        "first": "Mary",
        "last": "Diaz",
        "role": "Paralegal",
        "title": "Paralegal",
        "email": "mary@jenkinstitle.com",
        "phone": "678-572-1956",
        "photo": "mary.jpeg",
        "bio": None,
    },
    {
        "slug": "eliberth-cordova",
        "first": "Eliberth",
        "last": "Cordova",
        "role": "Post-Closing Assistant",
        "title": "Post-Closing Assistant",
        "email": "eli@jenkinstitle.com",
        "phone": None,
        "photo": "eliberth.jpeg",
        "bio": "Eliberth Cordova is a professional with experience in real estate closings and document management. She completed legal studies at Universidad Santa Mar&iacute;a in Caracas, Venezuela, and has prior experience in real estate as a realtor with Century 21 International. She is currently in the process of obtaining her real estate licenses in the states of Georgia and Florida.",
    },
]


def generate_vcard(emp):
    """Generate a vCard 3.0 file."""
    lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:{emp['last']};{emp['first']};;;",
        f"FN:{emp['first']} {emp['last']}",
        f"ORG:{COMPANY}",
        f"TITLE:{emp['title']}",
        f"EMAIL;TYPE=WORK:{emp['email']}",
    ]
    if emp.get("phone"):
        lines.append(f"TEL;TYPE=WORK,VOICE:{emp['phone']}")
    lines.append(f"TEL;TYPE=WORK,VOICE:{OFFICE_PHONE}")
    lines.append(f"ADR;TYPE=WORK:;;{ADDRESS}")
    lines.append(f"URL:{WEBSITE}/team/{emp['slug']}")
    lines.append(f"PHOTO;VALUE=URI:{BASE_URL}/assets/images/team/{emp['photo']}")
    lines.append("END:VCARD")
    return "\r\n".join(lines)


def generate_html(emp):
    """Generate an individual employee page."""
    phone_html = ""
    if emp.get("phone"):
        phone_html = f"""
                <a href="tel:{emp['phone']}" class="profile-contact-item">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
                  <span>{emp['phone']}</span>
                </a>"""

    bio_html = ""
    if emp.get("bio"):
        bio_html = f"""
          <div class="profile-bio">
            <p>{emp['bio']}</p>
          </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{emp['first']} {emp['last']} - {emp['role']} at Maple Bridge Law LLC.">
  <title>{emp['first']} {emp['last']} | Maple Bridge Law</title>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Source+Sans+3:wght@300;400;600;700&display=swap" rel="stylesheet">

  <!-- Styles -->
  <link rel="stylesheet" href="../../assets/css/style.css">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="../../assets/images/logo.svg">

  <style>
    .profile-breadcrumb-bar {{
      margin-top: 80px;
      padding: 1rem 0;
      background: var(--navy);
      font-size: 0.9rem;
      text-align: center;
    }}
    .profile-breadcrumb-bar a {{
      color: rgba(255, 255, 255, 0.7);
    }}
    .profile-breadcrumb-bar a:hover {{
      color: var(--teal-light);
    }}
    .profile-breadcrumb-bar .separator {{
      margin: 0 0.5rem;
      color: rgba(255, 255, 255, 0.4);
    }}
    .profile-breadcrumb-bar span:last-child {{
      color: var(--white);
      font-weight: 600;
    }}
    .profile-section {{
      max-width: 700px;
      margin: 0 auto;
      text-align: center;
    }}
    .profile-photo {{
      width: 200px;
      height: 200px;
      border-radius: 50%;
      object-fit: cover;
      border: 4px solid var(--teal);
      margin-bottom: 1.5rem;
    }}
    .profile-name {{
      font-size: 2.25rem;
      margin-bottom: 0.25rem;
    }}
    .profile-role {{
      color: var(--teal-dark);
      font-weight: 600;
      font-size: 1rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 1.5rem;
    }}
    .profile-contacts {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 2rem;
    }}
    .profile-contact-item {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text);
      font-size: 1.05rem;
    }}
    .profile-contact-item:hover {{
      color: var(--teal-dark);
    }}
    .profile-contact-item svg {{
      color: var(--teal);
      flex-shrink: 0;
    }}
    .profile-bio {{
      text-align: left;
      margin-bottom: 2rem;
      padding: 2rem;
      background: var(--off-white);
      border-radius: 8px;
    }}
    .profile-bio p {{
      line-height: 1.8;
      color: var(--text);
    }}
    .save-contact-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      background: var(--teal);
      color: var(--white);
      padding: 1rem 2rem;
      border-radius: 4px;
      font-size: 1rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      transition: var(--transition);
      border: 2px solid var(--teal);
    }}
    .save-contact-btn:hover {{
      background: var(--teal-dark);
      border-color: var(--teal-dark);
      color: var(--white);
    }}
    .save-contact-btn svg {{
      flex-shrink: 0;
    }}
    .back-link {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 2rem;
      font-weight: 600;
      text-transform: uppercase;
      font-size: 0.85rem;
      letter-spacing: 0.05em;
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-inner">
      <a href="../../index.html" class="logo">
        <img src="../../assets/images/logo.svg" alt="Maple Bridge Law">
        <div class="logo-text">
          Maple Bridge
          <span>Law</span>
        </div>
      </a>

      <button class="menu-toggle" aria-label="Toggle menu">
        <span></span>
        <span></span>
        <span></span>
      </button>

      <nav>
        <a href="../../index.html">Home</a>
        <a href="../../practice-areas.html">Practice Areas</a>
        <a href="../../about.html">About</a>
        <a href="../../team.html" class="active">Team</a>
        <a href="../../contact.html" class="nav-cta">Contact Us</a>
      </nav>
    </div>
  </header>

  <!-- Breadcrumb Bar -->
  <div class="profile-breadcrumb-bar">
    <div class="container">
      <a href="../../index.html">Home</a>
      <span class="separator">/</span>
      <a href="../../team.html">Team</a>
      <span class="separator">/</span>
      <span>{emp['first']} {emp['last']}</span>
    </div>
  </div>

  <!-- Profile -->
  <section>
    <div class="container">
      <div class="profile-section">
        <img class="profile-photo" src="../../assets/images/team/{emp['photo']}" alt="{emp['first']} {emp['last']}">
        <h2 class="profile-name">{emp['first']} {emp['last']}</h2>
        <p class="profile-role">{emp['role']}</p>

        <div class="profile-contacts">
          <a href="mailto:{emp['email']}" class="profile-contact-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            <span>{emp['email']}</span>
          </a>{phone_html}
          <a href="tel:{OFFICE_PHONE}" class="profile-contact-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="18" rx="2" ry="2"/><line x1="2" y1="9" x2="22" y2="9"/></svg>
            <span>Office: {OFFICE_PHONE}</span>
          </a>
        </div>

        <a href="../../assets/vcards/{emp['slug']}.vcf" class="save-contact-btn" download>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z"/><polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/></svg>
          Save Contact
        </a>
{bio_html}
      </div>
    </div>
  </section>

  <!-- CTA Banner -->
  <section class="cta-banner">
    <div class="container">
      <h2>Ready to Discuss Your Legal Needs?</h2>
      <p>Contact us today for a consultation. We're here to help protect your interests and achieve your goals.</p>
      <a href="tel:{OFFICE_PHONE}" class="btn btn-primary">Call {OFFICE_PHONE}</a>
      <a href="mailto:info@maplebridgelaw.com" class="btn btn-outline">Email Us</a>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="logo-text">
            Maple Bridge
            <span>Law</span>
          </div>
          <p>Strategic legal solutions for businesses and individuals. Serving clients throughout Georgia and Alabama in real estate, corporate law, and international matters.</p>
        </div>

        <div class="footer-links">
          <h4>Practice Areas</h4>
          <ul>
            <li><a href="../../practice-areas.html#real-estate">Real Estate</a></li>
            <li><a href="../../practice-areas.html#corporate">Corporate Law</a></li>
            <li><a href="../../practice-areas.html#international">International</a></li>
          </ul>
        </div>

        <div class="footer-links">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="../../about.html">About Us</a></li>
            <li><a href="../../team.html">Our Team</a></li>
            <li><a href="../../contact.html">Contact</a></li>
            <li><a href="https://www.jenkinstitle.com" target="_blank">Jenkins Title</a></li>
          </ul>
        </div>

        <div class="footer-links">
          <h4>Contact</h4>
          <ul>
            <li>416 Pirkle Ferry Road<br>Suite L-100<br>Cumming, GA 30040</li>
            <li><a href="tel:{OFFICE_PHONE}">{OFFICE_PHONE}</a></li>
            <li><a href="mailto:info@maplebridgelaw.com">info@maplebridgelaw.com</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2025 Maple Bridge Law LLC. All Rights Reserved.</p>
        <div class="social-links">
          <a href="https://www.linkedin.com/company/maple-bridge-law-llc" target="_blank" aria-label="LinkedIn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
            </svg>
          </a>
          <a href="https://www.facebook.com/people/Maple-Bridge-Law/100091004212306/" target="_blank" aria-label="Facebook">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
            </svg>
          </a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Mobile Menu Script -->
  <script>
    document.querySelector('.menu-toggle').addEventListener('click', function() {{
      document.querySelector('nav').classList.toggle('active');
      this.classList.toggle('active');
    }});
  </script>

</body>
</html>
"""


def generate_qr(url, output_path):
    """Generate a QR code PNG."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#00305B", back_color="white")
    img.save(output_path)


def main():
    TEAM_DIR.mkdir(exist_ok=True)
    VCARD_DIR.mkdir(parents=True, exist_ok=True)
    QR_DIR.mkdir(parents=True, exist_ok=True)

    for emp in EMPLOYEES:
        if emp.get("hidden"):
            print(f"  Skipping {emp['first']} {emp['last']} (hidden)")
            # Remove existing files if present
            for p in [
                VCARD_DIR / f"{emp['slug']}.vcf",
                TEAM_DIR / emp['slug'] / "index.html",
                QR_DIR / f"{emp['slug']}.png",
            ]:
                if p.exists():
                    p.unlink()
                    print(f"    Removed: {p.relative_to(SCRIPT_DIR)}")
            # Remove empty directory
            d = TEAM_DIR / emp['slug']
            if d.exists():
                d.rmdir()
            print()
            continue

        # vCard
        vcard_path = VCARD_DIR / f"{emp['slug']}.vcf"
        vcard_path.write_text(generate_vcard(emp))
        print(f"  vCard: {vcard_path.relative_to(SCRIPT_DIR)}")

        # HTML page (team/{slug}/index.html for clean URLs)
        page_dir = TEAM_DIR / emp['slug']
        page_dir.mkdir(exist_ok=True)
        html_path = page_dir / "index.html"
        html_path.write_text(generate_html(emp))
        print(f"  Page:  {html_path.relative_to(SCRIPT_DIR)}")

        # QR code
        page_url = f"{BASE_URL}/team/{emp['slug']}"
        qr_path = QR_DIR / f"{emp['slug']}.png"
        generate_qr(page_url, qr_path)
        print(f"  QR:    {qr_path.relative_to(SCRIPT_DIR)}")
        print()

    print("Done! All employee pages, vCards, and QR codes generated.")
    print()
    print("URLs:")
    for emp in EMPLOYEES:
        print(f"  {emp['first']:10s} {BASE_URL}/team/{emp['slug']}")


if __name__ == "__main__":
    main()
