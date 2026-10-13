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
        "role": "Founder · Attorney · Admitted in Georgia and Alabama",
        "title": "Attorney",
        "email": "drew@maplebridgelaw.com",
        "phone": "678-572-1954",
        "photo": "portrait/drew.jpg",
        "bio": "Drew Jenkins is the founder of Maple Bridge Law LLC in Atlanta, Georgia and AMA Capital, LLC in Birmingham, Alabama. He is an attorney licensed in both Alabama and Georgia who specializes in real estate transactions, financing, title, business structure, and international related projects. Drew handles both residential and commercial properties with deep experience in SBA, EB-5 financing, and 1031 transactions. He earned his B.A. degree, magna cum laude, from the University of Alabama at Birmingham and his J.D. degree from the University of Alabama School of Law.",
    },
    {
        "slug": "elliott-smith",
        "first": "Elliott",
        "last": "Smith",
        "role": "Attorney · Admitted in Georgia",
        "title": "Attorney",
        "email": "elliott@maplebridgelaw.com",
        "phone": "678-541-8878",
        "photo": "portrait/elliott.jpg",
        "bio": "Elliott Smith is an experienced attorney for title insurance underwriting, real estate closings, development and permitting. Formerly a member of Lipscomb &amp; Johnson law firm in Cumming, Elliott has been in private law practice for over 20 years. He is a graduate of Woodward Academy, the University of Georgia (B.A. Political Science, 1995), and Georgia State University College of Law (J.D., 2000). Elliott is an active member of the State Bar of Georgia and the Real Property Law Section.",
    },
    {
        "slug": "said-jabbour",
        "first": "Said",
        "last": "Jabbour",
        "role": "Attorney · Admitted in Alabama only",
        "title": "Attorney",
        "email": None,
        "phone": None,
        "photo": "portrait/said.jpg",
        "bio": "Said&rsquo;s background includes Vulcan Materials and Balch &amp; Bingham, where he worked on mergers and acquisitions, corporate finance, and securities. He holds a JD and an LLM in taxation from the University of Alabama.",
    },
    {
        "slug": "clay-johnson",
        "first": "Clay",
        "last": "Johnson",
        "role": "Attorney · Admitted in Alabama only",
        "title": "Attorney",
        "email": None,
        "phone": None,
        "photo": "portrait/clay.jpg",
        "bio": "Clay works on corporate, commercial, and real estate transactions. Before Maple Bridge Law, he worked at Vulcan Materials, Shipt, and Baker Donelson. He holds a JD and an MBA from Samford University.",
    },
    {
        "slug": "sam-pierce",
        "first": "Sam",
        "last": "Pierce",
        "role": "Attorney · Admitted in Alabama",
        "title": "Attorney",
        "email": "sam@maplebridgelaw.com",
        "phone": None,
        "photo": "portrait/sam.jpg",
        "bio": "Samuel C. Pierce represents commercial lenders, developers, and real estate professionals throughout Alabama. His practice draws on more than a decade of experience spanning complex commercial litigation, financial services, corporate transactions, contract negotiation, compliance, and real estate matters. He has also held several in-house counsel and general counsel roles for companies ranging from emerging startups to national organizations, advising executives on commercial contracts, employment matters, regulatory compliance, risk management, and dispute resolution. His unique background provides clients with both the practical business perspective of in-house counsel and the advocacy skills of an experienced litigator. Earlier in his career, Sam practiced with Baker Donelson, one of the Southeast&rsquo;s largest law firms, as a member of the Financial Services Practice Group and Corporate Restructuring &amp; Bankruptcy Practice Group. Sam earned his J.D., cum laude, from Cumberland School of Law at Samford University, where he graduated in the top 8% of his class and served as a Research Editor on the Cumberland Law Review.",
    },
    {
        "slug": "zovig-kelesarian",
        "first": "Zovig",
        "last": "Kelesarian",
        "role": "Legal Consultant · Admitted to the practice of law in Venezuela",
        "title": "Legal Consultant",
        "email": "zovig@maplebridgelaw.com",
        "phone": None,
        "photo": "portrait/zovig.jpg",
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
        "photo": "portrait/mary.jpg",
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
        "photo": "portrait/eliberth.jpg",
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
    ]
    if emp.get("email"):
        lines.append(f"EMAIL;TYPE=WORK:{emp['email']}")
    if emp.get("phone"):
        lines.append(f"TEL;TYPE=WORK,VOICE:{emp['phone']}")
    lines.append(f"TEL;TYPE=WORK,VOICE:{OFFICE_PHONE}")
    lines.append(f"ADR;TYPE=WORK:;;{ADDRESS}")
    lines.append(f"URL:{WEBSITE}/team/{emp['slug']}")
    lines.append(f"PHOTO;VALUE=URI:{BASE_URL}/assets/images/team/{emp['photo']}")
    lines.append("END:VCARD")
    return "\r\n".join(lines)



FONTS = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Source+Sans+3:wght@400;500;600&display=swap"

PRACTICES = ["Corporate &amp; M&amp;A", "Funds &amp; Securities", "Lending", "Real Estate", "Tax", "International"]


def site_head(title, description, p=""):
    """<head> shared by every page. p = path prefix back to the site root ("" or "../../")."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" type="image/svg+xml" href="{p}assets/images/logo.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">
  <link rel="stylesheet" href="{p}assets/css/site.css">
</head>
<body>
"""


def site_header(p=""):
    return f"""
<header id="top">
  <div class="wrap nav">
    <a class="brand" href="{p}index.html"><img src="{p}assets/images/logo.svg" alt=""><span>Maple Bridge Law</span></a>
    <button class="menu" aria-label="Menu">&#9776;</button>
    <nav>
      <a href="{p}index.html#practice">Practice</a>
      <a href="{p}index.html#approach">Approach</a>
      <a href="{p}index.html#team">People</a>
      <a href="{p}index.html#affiliates">Affiliates</a>
      <a href="{p}contact.html" class="btn btn-navy">Book a call</a>
    </nav>
  </div>
</header>
"""


def site_cta(p=""):
    return f"""
<section class="cta" id="contact">
  <div class="wrap inner">
    <div class="rv"><h2>Tell us about <em>the deal.</em></h2><p>A short call with an attorney, a clear scope, and a fee before work begins.</p></div>
    <div class="ctas rv">
      <a href="{p}contact.html" class="btn btn-light">Book a call</a>
      <a href="tel:{OFFICE_PHONE}" class="btn btn-ghost">{OFFICE_PHONE}</a>
    </div>
  </div>
</section>
"""


def site_footer(p=""):
    practices = "".join(f'<li><a href="{p}index.html#practice">{x}</a></li>' for x in PRACTICES)
    return f"""
<footer>
  <div class="wrap">
    <div class="top">
      <div>
        <a class="brand" href="{p}index.html"><img src="{p}assets/images/logo.svg" alt=""><span>Maple Bridge Law</span></a>
        <div class="social">
          <a href="https://www.linkedin.com/company/maple-bridge-law-llc" target="_blank" rel="noopener" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
          <a href="https://www.facebook.com/people/Maple-Bridge-Law/100091004212306/" target="_blank" rel="noopener" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
        </div>
      </div>
      <div><h5>Practice</h5><ul>{practices}</ul></div>
      <div><h5>Firm</h5><ul><li><a href="{p}index.html#team">People</a></li><li><a href="{p}contact.html">Contact</a></li><li><a href="https://spectrastrategies.com" target="_blank" rel="noopener">Spectra Strategies</a></li><li><a href="https://www.jenkinstitle.com" target="_blank" rel="noopener">Jenkins Title</a></li><li><a href="https://www.jointide.com" target="_blank" rel="noopener">JoinTide</a></li></ul></div>
      <div><h5>Office</h5><ul><li>416 Pirkle Ferry Road, Suite L-100</li><li>Cumming, Georgia 30040</li><li><a href="tel:{OFFICE_PHONE}">{OFFICE_PHONE}</a></li><li><a href="mailto:info@maplebridgelaw.com">info@maplebridgelaw.com</a></li></ul></div>
    </div>
    <div class="legal">
      <p>Attorney advertising. Maple Bridge Law LLC attorneys are licensed in Georgia and Alabama as noted for each attorney. Legal consultants are not admitted to practice law in any U.S. jurisdiction. Contacting the firm does not create an attorney-client relationship.</p>
      <span>&copy; 2026 Maple Bridge Law LLC &middot; <a href="{p}privacy-policy.html">Privacy Policy</a> &middot; <a href="{p}terms-of-service.html">Terms of Service</a></span>
    </div>
  </div>
</footer>
"""


SITE_JS = """
<script>
const h=document.querySelector('header');
addEventListener('scroll',()=>h.classList.toggle('scrolled',scrollY>8),{passive:true});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
const nav=document.querySelector('.nav nav');
document.querySelector('.menu').addEventListener('click',()=>nav.classList.toggle('open'));
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')));
const dlg=document.getElementById('bio');
if(dlg){
  document.querySelectorAll('button.person').forEach(c=>c.addEventListener('click',()=>{dlg.querySelector('.pop').replaceChildren(c.querySelector('template').content.cloneNode(true));dlg.showModal()}));
  dlg.querySelector('.pop-x').addEventListener('click',()=>dlg.close());
  dlg.addEventListener('click',e=>{if(e.target===dlg)dlg.close()});
}
</script>
</body>
</html>
"""


def generate_html(emp):
    """Generate an individual team page (team/<slug>/index.html)."""
    p = "../../"
    name = f"{emp['first']} {emp['last']}"
    contact = []
    if emp.get("email"):
        contact.append(f'<a href="mailto:{emp["email"]}">{emp["email"]}</a>')
    if emp.get("phone"):
        contact.append(f'<a href="tel:{emp["phone"]}">{emp["phone"]}</a>')
    contact.append(f'<span>Office <a href="tel:{OFFICE_PHONE}">{OFFICE_PHONE}</a></span>')
    bio_html = f'<div class="bio"><p>{emp["bio"]}</p></div>' if emp.get("bio") else ""
    return (site_head(f"{name} | Maple Bridge Law", f"{name} - {emp['role']} at Maple Bridge Law LLC.", p)
            + site_header(p)
            + f"""
<section class="page-body">
  <div class="wrap">
    <div class="crumbs"><a href="{p}index.html">Home</a> / <a href="{p}index.html#team">People</a> / {name}</div>
    <div class="profile">
      <div class="ph"><img src="{p}assets/images/team/{emp['photo']}" alt="{name}"></div>
      <div>
        <h1>{name}</h1>
        <div class="meta">{emp['role']}</div>
        {bio_html}
        <div class="pop-contact">{''.join(contact)}</div>
        <a href="{p}assets/vcards/{emp['slug']}.vcf" class="btn btn-navy save-contact" download>Save contact</a>
      </div>
    </div>
  </div>
</section>
"""
            + site_cta(p) + site_footer(p) + SITE_JS)


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
