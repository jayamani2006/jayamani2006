import os
import base64
from datetime import datetime

# =========================================================================================
# DEVELOPER KNOWLEDGE DATABASE (DKD)
# =========================================================================================
DEVELOPER_NAME = "Jayasubramani S"
BRAND = "JS SoftTools"
ROLE = "Creative Engineer & Product Thinker"

# =========================================================================================
# ASSET LOADING (BASE64)
# =========================================================================================
def load_image_b64(rel_path):
    # Try to resolve relative to this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.abspath(os.path.join(base_dir, rel_path))
    if not os.path.exists(abs_path):
        # Return a transparent 1x1 pixel if missing
        return "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
    with open(abs_path, "rb") as f:
        ext = os.path.splitext(abs_path)[1][1:].lower()
        mime = "jpeg" if ext in ["jpg", "jpeg"] else "png"
        return f"data:image/{mime};base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Images required by the spec
AVATAR_B64 = load_image_b64("assets/jayamani.jpg")
LOGO_B64 = load_image_b64("assets/JSSTP.jpg")

# =========================================================================================
# CYBERPUNK BRUTALIST TOKENS
# =========================================================================================
COLORS = {
    "bg": "#0a0a0f",
    "surface": "#12121c",
    "border": "#2a2a35",
    "magenta": "#ff0055",
    "cyan": "#00ffc4",
    "green": "#00ff00",
    "text_main": "#e2e2ee",
    "text_dim": "#6a6a7c"
}

SVG_DEFS = f"""
    <defs>
        <filter id="neonMagenta" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="neonCyan" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="hologram">
            <feColorMatrix type="matrix" values="
                0 0 0 0 0
                0 1 0 0 0
                0 0 1 0 0
                0 0 0 1 0" />
            <feComponentTransfer>
                <feFuncB type="linear" slope="1.5"/>
                <feFuncG type="linear" slope="1.2"/>
            </feComponentTransfer>
        </filter>
        <filter id="glitchDisplacement">
            <feTurbulence type="fractalNoise" baseFrequency="0.05 0.95" numOctaves="1" result="noise" />
            <feDisplacementMap in="SourceGraphic" in2="noise" scale="10" xChannelSelector="R" yChannelSelector="G">
                <animate attributeName="scale" values="0;20;0;0;50;0" dur="3s" repeatCount="indefinite" />
            </feDisplacementMap>
        </filter>
        <linearGradient id="glassBg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{COLORS['surface']}" stop-opacity="0.8" />
            <stop offset="100%" stop-color="#0a0a0f" stop-opacity="0.9" />
        </linearGradient>
        <pattern id="microGrid" width="10" height="10" patternUnits="userSpaceOnUse">
            <rect width="10" height="10" fill="none" stroke="{COLORS['border']}" stroke-width="0.5" stroke-opacity="0.3"/>
        </pattern>
        <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
            <rect width="4" height="2" fill="#000" opacity="0.3"/>
        </pattern>
    </defs>
"""

def encode_svg(svg_string):
    encoded = base64.b64encode(svg_string.encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{encoded}"

# =========================================================================================
# 1. HERO SVG WITH AVATAR
# =========================================================================================
def generate_hero_svg():
    svg = f"""<svg width="800" height="320" viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg">
    {SVG_DEFS}
    <rect x="10" y="10" width="780" height="300" fill="url(#glassBg)" stroke="{COLORS['border']}" stroke-width="3" />
    <rect x="10" y="10" width="780" height="300" fill="url(#microGrid)" />
    
    <path d="M 10 30 L 10 10 L 30 10 M 770 10 L 790 10 L 790 30 M 790 290 L 790 310 L 770 310 M 30 310 L 10 310 L 10 290" stroke="{COLORS['cyan']}" stroke-width="3" fill="none" filter="url(#neonCyan)" />
    
    <rect x="10" y="10" width="780" height="10" fill="{COLORS['cyan']}" opacity="0.1">
        <animate attributeName="y" values="10;300;10" dur="4s" repeatCount="indefinite" />
    </rect>
    <rect x="10" y="10" width="780" height="300" fill="url(#scanlines)" pointer-events="none" />
    
    <!-- Holographic Avatar Projection -->
    <g transform="translate(600, 50)">
        <!-- Outer glowing ring -->
        <circle cx="75" cy="75" r="85" fill="none" stroke="{COLORS['cyan']}" stroke-width="2" opacity="0.5">
            <animateTransform attributeName="transform" type="rotate" values="0 75 75; 360 75 75" dur="10s" repeatCount="indefinite" />
        </circle>
        <!-- Clip path for circular image -->
        <clipPath id="avatarClip">
            <circle cx="75" cy="75" r="75" />
        </clipPath>
        <!-- The actual image, filtered to look like a hologram -->
        <image href="{AVATAR_B64}" x="0" y="0" width="150" height="150" clip-path="url(#avatarClip)" filter="url(#hologram)" opacity="0.9" />
        
        <!-- Scanline over image -->
        <rect x="0" y="0" width="150" height="5" fill="{COLORS['cyan']}" opacity="0.5">
            <animate attributeName="y" values="0;150;0" dur="2s" repeatCount="indefinite" />
        </rect>
        <circle cx="75" cy="75" r="75" fill="none" stroke="{COLORS['magenta']}" stroke-width="3" filter="url(#neonMagenta)" />
    </g>

    <!-- Text Content -->
    <g transform="translate(50, 100)">
        <text x="0" y="0" font-family="monospace" font-size="14" fill="{COLORS['green']}">
            System.Initialize("{BRAND}");
            <animate attributeName="opacity" values="1;0.5;1;0;1" dur="2s" repeatCount="indefinite" />
        </text>
        
        <g transform="translate(0, 50)">
            <text x="-2" y="0" font-family="Arial, sans-serif" font-weight="900" font-size="50" fill="{COLORS['cyan']}" filter="url(#neonCyan)">
                {DEVELOPER_NAME}
                <animateTransform attributeName="transform" type="translate" values="0,0; -5,0; 5,0; 0,0" dur="0.1s" begin="2s" repeatCount="indefinite" />
            </text>
            <text x="2" y="0" font-family="Arial, sans-serif" font-weight="900" font-size="50" fill="{COLORS['magenta']}" filter="url(#neonMagenta)">
                {DEVELOPER_NAME}
                <animateTransform attributeName="transform" type="translate" values="0,0; 5,0; -5,0; 0,0" dur="0.1s" begin="2s" repeatCount="indefinite" />
            </text>
            <text x="0" y="0" font-family="Arial, sans-serif" font-weight="900" font-size="50" fill="#ffffff" filter="url(#glitchDisplacement)">
                {DEVELOPER_NAME}
            </text>
        </g>
        
        <text x="0" y="90" font-family="monospace" font-weight="bold" font-size="18" fill="{COLORS['text_main']}">{ROLE}</text>
        <rect x="0" y="120" width="40" height="4" fill="{COLORS['cyan']}"/>
    </g>
</svg>"""
    return encode_svg(svg)

# =========================================================================================
# 2. SECTION HEADER
# =========================================================================================
def generate_header_svg(title):
    svg = f"""<svg width="800" height="60" viewBox="0 0 800 60" xmlns="http://www.w3.org/2000/svg">
    {SVG_DEFS}
    <rect width="800" height="60" fill="url(#glassBg)" stroke="{COLORS['border']}" stroke-width="2"/>
    <path d="M 0 0 L 20 0 L 20 20 M 800 60 L 780 60 L 780 40" stroke="{COLORS['cyan']}" stroke-width="2" fill="none" />
    
    <text x="30" y="38" font-family="monospace" font-weight="bold" font-size="24" fill="{COLORS['cyan']}">
        ## █ {title}
        <animate attributeName="fill" values="{COLORS['cyan']};{COLORS['text_dim']};{COLORS['cyan']}" dur="0.5s" repeatCount="indefinite" />
    </text>
    
    <rect x="-10" y="0" width="4" height="60" fill="{COLORS['cyan']}" filter="url(#neonCyan)" opacity="0.3">
        <animate attributeName="x" values="-10;810;-10" dur="4s" repeatCount="indefinite" />
    </rect>
</svg>"""
    return encode_svg(svg)

# =========================================================================================
# 3. MASSIVE TECH ECOSYSTEM GRID
# =========================================================================================
def generate_tech_ecosystem_svg():
    categories = [
        ("LANGUAGES", ["Java", "Python", "C", "JavaScript", "TypeScript", "SQL"], 0),
        ("FRONTEND", ["HTML/CSS", "React", "Angular", "UI/UX"], 1),
        ("BACKEND", ["Node.js", "Express"], 2),
        ("DATABASE", ["MySQL", "SQLite"], 3),
        ("DESKTOP", ["PyQt6", "Tkinter"], 4),
        ("EMBEDDED", ["ESP8266", "Arduino"], 5)
    ]
    
    svg_body = ""
    y_offset = 20
    
    # Animated electrical spine
    svg_body += f'<path d="M 400 20 L 400 580" stroke="{COLORS["border"]}" stroke-width="6" fill="none" />'
    svg_body += f'<path d="M 400 20 L 400 580" stroke="{COLORS["cyan"]}" stroke-width="2" fill="none" filter="url(#neonCyan)" stroke-dasharray="20 400"><animate attributeName="stroke-dashoffset" values="420; -420" dur="3s" repeatCount="indefinite" /></path>'

    for title, techs, idx in categories:
        is_left = idx % 2 == 0
        x_base = 30 if is_left else 450
        
        # Connect to spine
        if is_left:
            svg_body += f'<path d="M 370 {y_offset+30} L 400 {y_offset+30}" stroke="{COLORS["cyan"]}" stroke-width="2" fill="none" opacity="0.5"/>'
        else:
            svg_body += f'<path d="M 400 {y_offset+30} L 430 {y_offset+30}" stroke="{COLORS["magenta"]}" stroke-width="2" fill="none" opacity="0.5"/>'
            
        color = COLORS['cyan'] if is_left else COLORS['magenta']
        
        svg_body += f'<text x="{x_base}" y="{y_offset+15}" font-family="monospace" font-weight="bold" font-size="16" fill="{color}">> {title}</text>'
        
        # Tech boxes
        for i, tech in enumerate(techs):
            col = i % 2
            row = i // 2
            bx = x_base + (col * 160)
            by = y_offset + 30 + (row * 40)
            
            svg_body += f'<rect x="{bx}" y="{by}" width="140" height="30" fill="{COLORS["surface"]}" stroke="{color}" stroke-width="1.5" />'
            svg_body += f'<text x="{bx+70}" y="{by+20}" font-family="monospace" font-size="14" fill="#fff" text-anchor="middle">{tech}</text>'
            
        y_offset += max(100, 30 + ((len(techs)-1)//2 + 1)*40 + 20)

    svg = f"""<svg width="800" height="600" viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
    {SVG_DEFS}
    <rect width="800" height="600" fill="url(#glassBg)" stroke="{COLORS['border']}" stroke-width="3" />
    <rect width="800" height="600" fill="url(#scanlines)" pointer-events="none" opacity="0.5"/>
    {svg_body}
</svg>"""
    return encode_svg(svg)

# =========================================================================================
# 4. STATUS TAGS
# =========================================================================================
def generate_status_svg(status):
    color = COLORS['green']
    if status == "RUNNING":
        anim = f"""<text x="90" y="15" font-family="monospace" font-size="12" fill="{color}"><animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />0x00FF</text>"""
    elif status == "ANALYZING":
        color = COLORS['magenta']
        anim = f"""<text x="90" y="15" font-family="monospace" font-size="12" fill="{color}"><animate attributeName="opacity" values="1;0" dur="0.1s" repeatCount="indefinite" />[/]</text>"""
    elif status == "ONLINE":
        color = COLORS['cyan']
        anim = f"""<text x="90" y="15" font-family="monospace" font-size="12" fill="{color}" filter="url(#neonCyan)"><animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite" />●</text>"""
    else: # STANDBY
        color = COLORS['text_dim']
        anim = f"""<text x="90" y="15" font-family="monospace" font-size="12" fill="{color}">IDLE</text>"""

    svg = f"""<svg width="150" height="24" viewBox="0 0 150 24" xmlns="http://www.w3.org/2000/svg">
    {SVG_DEFS}
    <rect width="150" height="24" fill="{COLORS['bg']}" stroke="{color}" stroke-width="1" />
    <text x="5" y="16" font-family="monospace" font-size="12" font-weight="bold" fill="{color}">[{status}]</text>
    {anim}
</svg>"""
    return encode_svg(svg)

# =========================================================================================
# 5. ROADMAP TERMINAL SVG
# =========================================================================================
def generate_roadmap_svg():
    svg = f"""<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
    {SVG_DEFS}
    <rect width="800" height="250" fill="#000" stroke="{COLORS['border']}" stroke-width="2"/>
    <rect width="800" height="250" fill="url(#scanlines)" pointer-events="none" />
    
    <g font-family="monospace" font-size="14" fill="{COLORS['cyan']}">
        <text x="20" y="30">root@jssofttools:~# cat roadmap.txt</text>
        
        <g fill="{COLORS['text_main']}">
            <text x="20" y="70">Foundations ──┬── Java, Python, C fundamentals</text>
            <text x="20" y="90">              │   First desktop utilities &amp; coursework projects</text>
            
            <text x="20" y="120">Expansion ────┼── Full-stack basics: React, Node.js, Express, MySQL</text>
            <text x="20" y="140">              │   Growing focus on UI/UX in every build</text>
            
            <text x="20" y="170">Now ──────────┼── Advanced TypeScript &amp; Java</text>
            <text x="20" y="190">              │   Shipping AI-assisted, production-style desktop tools</text>
            
            <text x="20" y="220">Next ─────────┴── SaaS products · Open source · Scaled tooling</text>
        </g>
        
        <rect x="580" y="208" width="10" height="15" fill="{COLORS['green']}">
            <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite" />
        </rect>
    </g>
</svg>"""
    return encode_svg(svg)

# =========================================================================================
# 6. SPOTIFY CYBERPUNK WIDGET
# =========================================================================================
def generate_spotify_svg():
    tracks = [
        "The Final Countdown - Europe (1986)",
        "Believer - Imagine Dragons",
        "In The Stars - Benson Boone",
        "I Will Survive - Gloria Gaynor",
        "Diamonds - Rihanna"
    ]
    svg_body = ""
    for i, t in enumerate(tracks):
        y = 70 + i*30
        c = COLORS["cyan"] if i == 0 else COLORS["text_main"]
        icon = "▶" if i == 0 else "·"
        svg_body += f'<text x="20" y="{y}" font-family="monospace" font-size="14" fill="{c}">{icon} {t}</text>'
        if i == 0:
            svg_body += f'<rect x="0" y="{y-15}" width="800" height="24" fill="{COLORS["cyan"]}" opacity="0.1"><animate attributeName="opacity" values="0.1;0.2;0.1" dur="2s" repeatCount="indefinite"/></rect>'

    svg = f"""<svg width="800" height="240" viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
    {SVG_DEFS}
    <rect width="800" height="240" fill="url(#glassBg)" stroke="{COLORS['border']}" stroke-width="2"/>
    <rect width="800" height="240" fill="url(#scanlines)" pointer-events="none" opacity="0.5"/>
    
    <text x="20" y="30" font-family="monospace" font-weight="bold" font-size="16" fill="{COLORS['green']}">
        > INITIALIZING AUDIO SUBSYSTEM...
        <animate attributeName="opacity" values="1;0.5;1;0;1" dur="3s" repeatCount="indefinite" />
    </text>
    <path d="M 0 40 L 800 40" stroke="{COLORS['border']}" stroke-width="2"/>
    {svg_body}
</svg>"""
    return encode_svg(svg)

# =========================================================================================
# 7. FOOTER
# =========================================================================================
def generate_footer_svg():
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    svg = f"""<svg width="800" height="150" viewBox="0 0 800 150" xmlns="http://www.w3.org/2000/svg">
    {SVG_DEFS}
    <rect width="800" height="150" fill="url(#glassBg)" stroke="{COLORS['border']}" stroke-width="2" />
    
    <path d="M 0 30 L 0 0 L 30 0" stroke="{COLORS['cyan']}" stroke-width="5" fill="none" />
    <path d="M 800 30 L 800 0 L 770 0" stroke="{COLORS['cyan']}" stroke-width="5" fill="none" />
    <path d="M 0 120 L 0 150 L 30 150" stroke="{COLORS['cyan']}" stroke-width="5" fill="none" />
    <path d="M 800 120 L 800 150 L 770 150" stroke="{COLORS['cyan']}" stroke-width="5" fill="none" />
    
    <!-- JS SoftTools Brand Logo inside Footer -->
    <clipPath id="logoClip">
        <circle cx="400" cy="50" r="30" />
    </clipPath>
    <image href="{LOGO_B64}" x="370" y="20" width="60" height="60" clip-path="url(#logoClip)" opacity="0.8" />
    <circle cx="400" cy="50" r="30" fill="none" stroke="{COLORS['magenta']}" stroke-width="2" filter="url(#neonMagenta)" />
    
    <clipPath id="logClip">
        <rect x="250" y="90" width="300" height="40" />
    </clipPath>
    <g clip-path="url(#logClip)" font-family="monospace" font-size="12" fill="{COLORS['green']}" text-anchor="middle">
        <text x="400" y="110">
            <animate attributeName="y" values="130; 110; 110; 110; 110" dur="4s" repeatCount="indefinite" />
            System generated on {date_str}
        </text>
        <text x="400" y="110">
            <animate attributeName="y" values="150; 130; 110; 90; 90" dur="4s" repeatCount="indefinite" />
            Kernel shutdown sequence initiated...
        </text>
    </g>
</svg>"""
    return encode_svg(svg)

# =========================================================================================
# BUILD README
# =========================================================================================
def build_readme():
    lines = []
    
    # 1. INTRO
    lines.append("<h1 align=\"center\">Hi 👋, I'm Jayasubramani</h1>")
    lines.append('<h3 align="center">AI Developer | Full Stack Developer | Java Programmer | Software Engineer | Founder of JS SoftTools</h3>\\n')
    
    lines.append('<p align="left"> <img src="https://komarev.com/ghpvc/?username=jayamani2006&label=Profile%20views&color=0e75b6&style=flat" alt="jayamani2006" /> </p>')
    lines.append('<p align="left"> <a href="https://github.com/ryo-ma/github-profile-trophy"><img src="https://github-profile-trophy.vercel.app/?username=jayamani2006&theme=dracula" alt="jayamani2006" /></a> </p>\\n')
    
    # 2. ABOUT ME BULLETS
    lines.append("- 🔭 I’m currently working on [JS NotePad Website](https://js-notepad-website.onrender.com)")
    lines.append("- 🌱 I’m currently learning **Advanced Java Data Structures & Algorithms, SQL, Node.js, Angular, React, System Design, REST APIs, GitHub Actions, AI Application Development**")
    lines.append("- 👯 I’m looking to collaborate on [Open Source AI, Desktop Applications & Full Stack Projects](https://github.com/jayamani2006)")
    lines.append("- 🤝 I’m looking for help with [AI Integration, Open Source Contributions & Scalable Software Architecture](https://github.com/jayamani2006)")
    lines.append("- 👨‍💻 All of my projects are available at [https://jayasubramaniportfolio.netlify.app/](https://jayasubramaniportfolio.netlify.app/)")
    lines.append("- 💬 Ask me about **Java, Python, SQL, Node.js, Angular, React, Desktop Application Development, AI Projects, UI/UX Design, GitHub Automation, Open Source**")
    lines.append("- 📫 How to reach me **Personal: jayasubramani2971@gmail.com | Business: support.jssofttoolsproducts@gmail.com**")
    lines.append("- 📄 Know about my experiences [https://jayasubramaniportfolio.netlify.app/](https://jayasubramaniportfolio.netlify.app/)\\n")
    
    # 3. SOCIAL LINKS (Colored Badges)
    lines.append('<h3 align="left">Connect with me:</h3>')
    lines.append('<div align="center">')
    lines.append('  <a href="https://linkedin.com/in/jayasubramani-s-547201290"><img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="linkedin" /></a>')
    lines.append('  <a href="mailto:jayasubramani2971@gmail.com"><img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="gmail" /></a>')
    lines.append('  <a href="https://instagram.com/jaya_mani2971"><img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="instagram" /></a>')
    lines.append('  <a href="https://open.spotify.com/user/31gqp4an3kwy3c5o7zxv7ailkubm"><img src="https://img.shields.io/static/v1?message=Spotify&logo=spotify&label=&color=000000&logoColor=1DB954&labelColor=&style=for-the-badge" height="25" alt="spotify" /></a>')
    lines.append('  <a href="https://fb.com/jaya.subramani.2025"><img src="https://img.shields.io/static/v1?message=Facebook&logo=facebook&label=&color=1877F2&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="facebook" /></a>')
    lines.append('  <a href="https://www.reddit.com/u/Educational-Pain9138"><img src="https://img.shields.io/static/v1?message=Reddit&logo=reddit&label=&color=FF4500&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="reddit" /></a>')
    lines.append('  <a href="https://leetcode.com/u/a9JgwmiBQz/"><img src="https://img.shields.io/static/v1?message=LeetCode&logo=leetcode&label=&color=FFA116&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="leetcode" /></a>')
    lines.append('  <a href="http://hackerrank.com/profile/jayasubramani291"><img src="https://img.shields.io/static/v1?message=HackerRank&logo=hackerrank&label=&color=00EA64&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="hackerrank" /></a>')
    lines.append('  <a href="https://jayasubramaniportfolio.netlify.app/"><img src="https://img.shields.io/static/v1?message=Portfolio&logo=web&label=&color=0a0a0f&logoColor=00ffc4&labelColor=&style=for-the-badge" height="25" alt="portfolio" /></a>')
    lines.append('</div>\\n')
    
    # 4. TECH STACK (Devicons)
    lines.append('<h3 align="left">Languages and Tools:</h3>')
    lines.append('<div align="center">')
    tech_icons = [
        "angularjs/angularjs-original.svg", "arduino/arduino-original.svg", "amazonwebservices/amazonwebservices-original-wordmark.svg",
        "bash/bash-original.svg", "c/c-original.svg", "csharp/csharp-original.svg", "css3/css3-original-wordmark.svg",
        "express/express-original-wordmark.svg", "figma/figma-original.svg", "git/git-original.svg",
        "html5/html5-original-wordmark.svg", "java/java-original.svg", "javascript/javascript-original.svg",
        "mongodb/mongodb-original-wordmark.svg", "mysql/mysql-original-wordmark.svg", "nodejs/nodejs-original-wordmark.svg",
        "pandas/pandas-original.svg", "python/python-original.svg", "react/react-original.svg",
        "sqlite/sqlite-original.svg", "typescript/typescript-original.svg", "vscode/vscode-original.svg"
    ]
    for tech in tech_icons:
        lines.append(f'  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/{tech}" height="40" alt="{tech.split("/")[0]}" /> <img width="12" />')
    lines.append('</div>\\n<br/>\\n')
    
    # 5. GITHUB STATS & STREAKS (Side-by-side Progress Style)
    lines.append('<div align="center">')
    lines.append('  <img src="https://github-readme-stats.vercel.app/api?username=jayamani2006&show_icons=true&theme=dracula&hide_border=false" height="150" alt="GitHub Stats" />')
    lines.append('  <img src="https://streak-stats.demolab.com?user=jayamani2006&locale=en&mode=daily&theme=dracula&hide_border=false&border_radius=5" height="150" alt="Streak Graph" />')
    lines.append('</div>\\n<br/>\\n')
    
    # 7. PACMAN CONTRIBUTION GRAPH
    lines.append('<div align="center">')
    lines.append('  <h3>Contribution Graph</h3>')
    lines.append('  <picture>')
    lines.append('    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jayamani2006/jayamani2006/pacman-output/pacman-contribution-graph-dark.svg?game=pacman">')
    lines.append('    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/jayamani2006/jayamani2006/pacman-output/pacman-contribution-graph.svg?game=pacman">')
    lines.append('    <img alt="pacman contribution graph" src="https://raw.githubusercontent.com/jayamani2006/jayamani2006/pacman-output/pacman-contribution-graph.svg?game=pacman">')
    lines.append('  </picture>')
    lines.append('</div>\\n<br/>\\n')

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\\n".join(lines))
    print("Generated Ultimate README.md successfully.")

if __name__ == "__main__":
    build_readme()

