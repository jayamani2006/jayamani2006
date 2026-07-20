import urllib.parse

def generate_svg(title, content, height):
    svg = f'''<svg width="800" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0d1117"/>
            <stop offset="100%" stop-color="#161b22"/>
        </linearGradient>
        <linearGradient id="border" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#58a6ff"/>
            <stop offset="100%" stop-color="#1f6feb"/>
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    <rect width="100%" height="100%" fill="url(#bg)" rx="12" stroke="url(#border)" stroke-width="1"/>
    <text x="30" y="45" fill="#c9d1d9" font-family="monospace" font-size="20" font-weight="bold">{title}</text>
    <path d="M 30,60 L 770,60" stroke="#30363d" stroke-width="2" />
    {content}
    <text x="30" y="{height - 20}" fill="#8b949e" font-family="monospace" font-size="12">> SYSTEM STATUS: ONLINE</text>
</svg>'''
    return urllib.parse.quote(svg)

# Generate detailed components
hero_content = '''
    <text x="50" y="120" fill="#58a6ff" font-family="monospace" font-size="48" font-weight="900" filter="url(#glow)">JS SoftTools</text>
    <text x="50" y="160" fill="#c9d1d9" font-family="monospace" font-size="22">Jayasubramani S // Software Architect</text>
    <rect x="50" y="190" width="300" height="6" fill="#1f6feb" rx="3"/>
    
    <g transform="translate(50, 230)">
        <rect x="0" y="0" width="120" height="30" fill="#238636" rx="4"/>
        <text x="15" y="20" fill="#ffffff" font-family="monospace" font-size="14" font-weight="bold">INIT_CORE</text>
        <rect x="130" y="0" width="120" height="30" fill="transparent" stroke="#58a6ff" rx="4"/>
        <text x="145" y="20" fill="#58a6ff" font-family="monospace" font-size="14">DEPLOY_AI</text>
    </g>
    
    <!-- Abstract data visualization -->
    <g transform="translate(500, 100)" stroke="#58a6ff" stroke-width="1" fill="none">
        <circle cx="100" cy="100" r="80" stroke-dasharray="4 8" opacity="0.5">
            <animateTransform attributeName="transform" type="rotate" from="0 100 100" to="360 100 100" dur="20s" repeatCount="indefinite"/>
        </circle>
        <circle cx="100" cy="100" r="60" stroke="#1f6feb" stroke-width="2">
            <animateTransform attributeName="transform" type="rotate" from="360 100 100" to="0 100 100" dur="15s" repeatCount="indefinite"/>
        </circle>
        <path d="M 100,20 L 100,180 M 20,100 L 180,100" stroke="#30363d" opacity="0.5"/>
        <circle cx="100" cy="100" r="4" fill="#58a6ff" filter="url(#glow)"/>
        <polyline points="40,100 70,70 100,100 130,50 160,80" stroke="#238636" stroke-width="2" filter="url(#glow)"/>
    </g>
'''

about_content = '''
    <g transform="translate(40, 100)" font-family="monospace" font-size="15" fill="#c9d1d9">
        <text x="0" y="0">> EXECUTING: whoami.exe</text>
        <text x="0" y="30" fill="#58a6ff">[JS_SYS] Loading developer profile...</text>
        <text x="0" y="70">I design and build modern software that is lightweight, beautiful,</text>
        <text x="0" y="95">fast, maintainable, and useful. I focus on premium desktop software,</text>
        <text x="0" y="120">AI-powered tools, automation utilities, and polished user interfaces.</text>
        <text x="0" y="160" fill="#8b949e">> Mission: Build software that solves real-world problems.</text>
        <text x="0" y="185" fill="#8b949e">> Vision:  Pioneer tools bridging human creativity and AI execution.</text>
    </g>
'''

skills_content = '''
    <g transform="translate(40, 100)" font-family="monospace" font-size="14">
        <text x="0" y="0" fill="#58a6ff" font-weight="bold">CORE_LANGUAGES</text>
        <g transform="translate(0, 20)">
            <text x="0" y="15" fill="#c9d1d9">C# / .NET</text>
            <rect x="120" y="5" width="250" height="10" fill="#30363d" rx="5"/>
            <rect x="120" y="5" width="230" height="10" fill="#178600" rx="5" filter="url(#glow)"/>
            <text x="385" y="15" fill="#8b949e">95%</text>
            
            <text x="0" y="45" fill="#c9d1d9">Python</text>
            <rect x="120" y="35" width="250" height="10" fill="#30363d" rx="5"/>
            <rect x="120" y="35" width="210" height="10" fill="#3572A5" rx="5" filter="url(#glow)"/>
            <text x="385" y="45" fill="#8b949e">90%</text>
            
            <text x="0" y="75" fill="#c9d1d9">TypeScript</text>
            <rect x="120" y="65" width="250" height="10" fill="#30363d" rx="5"/>
            <rect x="120" y="65" width="190" height="10" fill="#3178c6" rx="5" filter="url(#glow)"/>
            <text x="385" y="75" fill="#8b949e">85%</text>
        </g>
        
        <text x="450" y="0" fill="#58a6ff" font-weight="bold">FRAMEWORKS_&amp;_TOOLS</text>
        <g transform="translate(450, 20)">
            <rect x="0" y="0" width="100" height="28" fill="#161b22" stroke="#30363d" rx="4"/>
            <text x="25" y="19" fill="#c9d1d9">React</text>
            
            <rect x="110" y="0" width="100" height="28" fill="#161b22" stroke="#30363d" rx="4"/>
            <text x="30" y="19" fill="#c9d1d9">Node.js</text>
            
            <rect x="0" y="38" width="100" height="28" fill="#161b22" stroke="#30363d" rx="4"/>
            <text x="30" y="57" fill="#c9d1d9">Docker</text>
            
            <rect x="110" y="38" width="100" height="28" fill="#161b22" stroke="#30363d" rx="4"/>
            <text x="35" y="57" fill="#c9d1d9">Figma</text>
            
            <rect x="0" y="76" width="210" height="28" fill="#161b22" stroke="#58a6ff" rx="4"/>
            <text x="40" y="95" fill="#58a6ff">AI_Integration</text>
        </g>
    </g>
'''

hero_uri = generate_svg("JSSoftTools_OS_v10.0", hero_content, 350)
about_uri = generate_svg("Identity_Matrix", about_content, 280)
skills_uri = generate_svg("Tech_Ecosystem_Map", skills_content, 250)

readme_content = f'''<div align="center">
  <img src="data:image/svg+xml,{hero_uri}" width="100%" alt="Hero Section" />
</div>

<br>

<div align="center">
  <img src="data:image/svg+xml,{about_uri}" width="100%" alt="About Section" />
</div>

<br>

<div align="center">
  <img src="data:image/svg+xml,{skills_uri}" width="100%" alt="Skills Section" />
</div>

<br>

<div align="center">
  <h2>&#9881; ENGINEERING METRICS</h2>
  <a href="https://github.com/JayasubramaniS">
    <img src="https://github-readme-stats.vercel.app/api?username=JayasubramaniS&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=58A6FF&text_color=C9D1D9&icon_color=58A6FF&border_radius=12" height="195" />
  </a>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=JayasubramaniS&theme=tokyonight&hide_border=true&background=0D1117&ring=58A6FF&fire=58A6FF&currStreakLabel=58A6FF" height="195" />
</div>

---
<div align="center">
  <i>"Architecture is not just about the code. It's about the feeling the software provides."</i>
</div>
'''

with open("e:/JSSoftToolsProducts/Github profile/Jayasubramani_Profile/README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
