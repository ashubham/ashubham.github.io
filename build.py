#!/usr/bin/env python3
"""Build a self-contained, GitHub Pages-ready HTML page. Python standard library only."""
from pathlib import Path
import json, html, base64
ROOT=Path(__file__).resolve().parent
d=json.loads((ROOT/'content.json').read_text())
e=lambda x:html.escape(str(x),quote=True)
def link(url,text,cls=''):
    return f'<a href="{e(url)}"'+(f' class="{cls}"' if cls else '')+f'>{e(text)}</a>'
def heading(num,id,title,desc):
    return f'<section class="section" id="{id}" aria-labelledby="{id}-title"><div class="section-head"><div><span class="section-number">{num}</span><h2 id="{id}-title">{title}</h2></div><p>{desc}</p></div>'
portrait='data:image/jpeg;base64,'+base64.b64encode((ROOT/'assets/ashish-shubham.jpg').read_bytes()).decode()
css=(ROOT/'styles.css').read_text()
favicon='data:image/svg+xml,'+__import__('urllib.parse',fromlist=['quote']).quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="8" fill="#102c38"/><text x="32" y="44" text-anchor="middle" fill="#ffffff" font-family="Georgia,serif" font-size="37">a<tspan fill="#efa37e">s</tspan></text></svg>')
out=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ashish Shubham — Engineering Leader, Author & Speaker</title>
<meta name="description" content="Ashish Shubham, Engineering Fellow and VP of Engineering at ThoughtSpot. Enterprise AI, embedded analytics, talks, patents, writing, and community service.">
<meta name="theme-color" content="#102c38"><meta property="og:type" content="profile"><meta property="og:title" content="Ashish Shubham — Engineering Leader, Author & Speaker"><meta property="og:description" content="Building enterprise AI and analytics. Explore Ashish’s work, talks, patents, writing, and media appearances.">
<link rel="icon" type="image/svg+xml" href="{favicon}"><style>{css}</style>
<script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@type':'Person','name':'Ashish Shubham','jobTitle':'Engineering Fellow / Vice President of Engineering','worksFor':{'@type':'Organization','name':'ThoughtSpot'},'alumniOf':{'@type':'CollegeOrUniversity','name':'Indian Institute of Technology Kharagpur'},'sameAs':['https://www.linkedin.com/in/ashubham','https://github.com/ashubham','https://ashishshubham.medium.com/','https://www.thoughtspot.com/author/ashish-shubham']})}</script>
</head><body><a class="skip" href="#main">Skip to content</a>
<header class="masthead"><div class="wrap nav"><a href="#main" class="brand" aria-label="Ashish Shubham, home">ashish<span>.</span></a><nav class="navlinks" aria-label="Main navigation"><a href="#work">Work</a><a href="#speaking">Speaking</a><a href="#writing">Writing</a><a href="#patents">Patents</a><a href="#service">Service</a><a href="#media">Media</a><a href="#contact">Contact</a></nav></div></header>
<main id="main"><div class="wrap">
<section class="hero" aria-labelledby="name"><div><div class="eyebrow">Engineering · AI · Human experience</div><h1 id="name">Ashish<br>Shubham<span style="color:var(--accent)">.</span></h1><p class="role">Engineering Fellow / VP of Engineering · ThoughtSpot</p><p class="intro">I build the platforms that bring AI and data into everyday work. My focus is enterprise AI agents, embedded analytics, and the developer experience that makes them useful.</p><div class="social"><a href="https://www.linkedin.com/in/ashubham">LinkedIn</a><a href="https://github.com/ashubham">GitHub</a><a href="https://ashishshubham.medium.com/">Blog</a><a href="mailto:ashubham@gmail.com">Email</a></div></div><figure class="portrait"><img src="{portrait}" alt="Ashish Shubham" width="640" height="640" fetchpriority="high"><figcaption><span>San Francisco Bay Area</span><span>Engineer. Author. Speaker.</span></figcaption></figure></section>
<div class="introband"><div><strong>Enterprise AI & analytics</strong><p>ThoughtSpot Embedded · Spotter · MCP</p></div><div><strong>From ideas to production</strong><p>Architecture, product, and engineering leadership</p></div><div><strong>Sharing what I learn</strong><p>Author · Conference speaker · IEEE Senior Member</p></div></div>
'''
out+=heading('01 / WORK','work','Building useful<br>intelligence.','I joined ThoughtSpot in 2015 as one of its early engineers. Since then, I’ve helped build its foundational product experiences and shape the architecture of its AI and developer platforms.')
out+='''<div class="focus-grid"><article><h3>ThoughtSpot<br>Embedded</h3><p>Created and scaled the embedded analytics product suite, bringing interactive, AI-powered analytics into other applications through developer tools and SDKs.</p><a class="small-link" href="https://www.thoughtspot.com/author/ashish-shubham">ThoughtSpot profile</a></article><article><h3>Spotter &<br>agent platforms</h3><p>Co-architected ThoughtSpot’s AI Analyst and helped define shared infrastructure for production agents: state, streaming, memory, orchestration, and secure tool use.</p><a class="small-link" href="https://aijourn.com/prompt-tools-value-everything-else-is-infra/">Read the architecture perspective</a></article><article><h3>AI meets<br>enterprise data</h3><p>Led ThoughtSpot’s Agentic MCP Server integration, connecting AI clients to enterprise analytics through a governed, natural-language tool interface.</p><a class="small-link" href="https://www.thoughtspot.com/blog/introducing-agentic-mcp-server">Explore the MCP integration</a></article></div></section>'''
out+=heading('02 / SPEAKING','speaking','On stage.<br>In conversation.','Talks, keynotes, and panels on production AI, MicroAgents, analytics, and developer platforms. Recordings are linked where available.')
for t in d['talks']:
    tagclass='tag scheduled' if 'Scheduled' in t['kind'] else 'tag'
    out+=f'<article class="trow"><div class="date">{e(t["date"])}</div><div class="tmain"><p class="event">{e(t["event"])}</p><h3>{link(t["url"],t["title"])}</h3><p class="venue">{e(t["venue"])}</p></div><div class="tmeta"><span class="{tagclass}">{e(t["kind"])}</span>'
    if t.get('recording'):out+=link(t['recording'],'Watch recording')
    elif t.get('resume'):out+=link('#source-notes','Resume listing')
    else:out+=link(t['url'],'Session details')
    out+='</div></article>'
out+='</section>'
out+=heading('03 / WRITING','writing','Ideas, in depth.','A book, technical articles, and practical guides—from conversational interfaces and web performance to shared agent infrastructure.')
out+='''<article class="book"><div><div class="eyebrow">The book</div><h3>Architecting<br>AI Data Systems</h3><p class="book-subtitle">Advanced Concepts for Senior Software Engineers</p></div><div class="book-notes"><p>Coauthored with Sayantan Ghosh. An exploration of the architecture behind modern AI and data systems.</p><p style="margin-top:14px">IndiePress</p><a class="small-link" href="https://www.goodreads.com/book/show/245530543-architecting-ai-data-systems">Explore the book</a></div></article><div class="writing-grid">'''
for a in d['writing']:
    out+=f'<article class="article"><p class="meta"><span class="type">{e(a["kind"])}</span> · {e(a["publisher"])}'+(' · '+e(a['date']) if a['date'] else '')+f'</p><h3>{link(a["url"],a["title"])}</h3><p>{e(a["description"])}</p>'
    if a.get('linkLabel'):out+=link(a['url'],a['linkLabel'],'small-link')
    out+='</article>'
out+='</div></section>'
out+=heading('04 / INVENTIONS','patents','Patents &<br>applications.','Co-inventor on U.S. patents spanning natural-language analytics, conversational interfaces, and intelligent search. Related grants are grouped by invention; application publications are labeled separately.')
out+='<div class="patent-grid">'
for i,p in enumerate(d['patents']):
    out+=f'<article class="patent"><span class="section-number">INVENTION / {i+1:02d}</span><h3>{e(p["title"])}</h3><p>{e(p["description"])}</p><ul>'
    for no,status,url in p['records']:out+=f'<li>{link(url,no)}<span>{e(status)}</span></li>'
    out+='</ul></article>'
out+='</div><p class="service-note">Named co-inventor; assignee: ThoughtSpot. Records checked September 2026. Linked records include grant and application history.</p></section>'
out+=heading('05 / SERVICE','service','Reviewing,<br>judging & advising.','Contributing to research evaluation, professional communities, and industry recognition.')
out+='''<div class="service-top"><article><div class="eyebrow">Industry judging</div><h3>BIG Awards for Business</h3><p>2025 judging service, listed in my resume. Also listed in the Business Intelligence Group’s public judge directory.</p><a class="small-link" href="https://www.bintelligence.com/judges?75dd0f39_page=37&amp;e3f2094b_page=37">Judge directory</a></article><article><div class="eyebrow">Advisory board</div><h3>DevNetwork</h3><p>Listed among DevNetwork’s industry advisory board members.</p><a class="small-link" href="https://www.devnetwork.com/advisory-boards/">Advisory board</a></article><article><div class="eyebrow">Editorial service</div><h3>Associate Editor</h3><p>Listed as an Associate Editor on SARC Publisher’s editorial team.</p><a class="small-link" href="https://sarcouncil.com/Editorial-Board-Journal-Innovative-Science/">Editorial board</a></article></div><h3 class="service-title">2026 reviewer / committee service</h3><div class="service-grid">'''
for org,full,year in d['service']:out+=f'<div class="service-item"><strong>{e(org)}</strong><span>{e(full)}</span></div>'
out+='</div><p class="service-note">Conference reviewer / committee entries follow my September 2026 resume. '+link('#source-notes','Source notes')+'</p></section>'
out+=heading('06 / MEDIA','media','In the press.<br>On the record.','Interviews, profiles, award coverage, and mentions of my work. Authored contributions appear in the writing section above.')
f=d['media'][0]
out+=f'<article class="media-feature"><div><div class="eyebrow">{e(f["publisher"])} · {e(f["kind"])}</div><span class="date">{e(f["date"])} · 91 minutes</span><p>A conversation about a decade of building enterprise analytics—and what changes when AI becomes part of the product.</p></div><div><h3>{link(f["url"],f["title"])}</h3><a class="small-link" href="{e(f["url"])}">Watch or listen</a><p class="service-note">Episode title as published by the host.</p></div></article><div class="media-list">'
for m in d['media'][1:]:
    out+=f'<article class="mrow"><div class="mby"><div class="outlet">{e(m["publisher"])}</div><div class="date">{e(m["date"])}</div><span class="tag">{e(m["kind"])}</span></div><div><h3>{link(m["url"],m["title"])}</h3><p>{e(m["description"])}</p></div></article>'
out+='</div></section>'
out+=heading('07 / OPEN SOURCE','open-source','Built in the open.','Personal projects and ThoughtSpot repositories featured on my GitHub profile. Practical tools for developers, interfaces, and conversational systems.')
out+='<div class="projects">'
for name,desc,url,kind in d['projects']:out+=f'<article class="project"><div class="eyebrow">{e(kind)}</div><h3>{link(url,name)}</h3><p>{e(desc)}</p></article>'
out+='</div></section>'
out+='''<section class="section background" id="background" aria-labelledby="background-title"><div><span class="section-number">08 / BACKGROUND</span><h2 id="background-title" style="margin-top:14px">Engineering,<br>with a product lens.</h2><p>My work brings together systems architecture, front-end engineering, and human–computer interaction. Before ThoughtSpot, I worked on web products at GoDaddy and maps and hyperlocal research at Nokia.</p><p>Outside work: snowboarding and surfing.</p></div><div><ul class="career"><li><span class="date">2015–present</span><div><strong>ThoughtSpot</strong><p>Engineering Fellow / Vice President of Engineering</p></div></li><li><span class="date">2013–2015</span><div><strong>GoDaddy</strong><p>Senior Software Engineer · Website Builder</p></div></li><li><span class="date">2011–2013</span><div><strong>Nokia Research</strong><p>Research Software Engineer · Maps and Hyperlocal</p></div></li><li><span class="date">2009</span><div><strong>Microsoft Research</strong><p>Research Intern · Human–Computer Interaction</p></div></li><li><span class="date">2006–2011</span><div><strong>IIT Kharagpur</strong><p>BS / MS in Computer Science & Engineering</p></div></li></ul><div class="recognition"><strong>Recognition</strong><p>IEEE Senior Member<br><a href="https://builtin.com/articles/tech-innovator-award-winners-2021">Built In Tech Innovator Award, 2021</a></p></div></div></section>
<section id="contact" class="contact" aria-labelledby="contact-title"><div class="eyebrow">Continue the conversation</div><h2 id="contact-title">Let’s talk AI, data,<br>and what comes next.</h2><div class="social"><a href="mailto:ashubham@gmail.com">ashubham@gmail.com</a><a href="https://www.linkedin.com/in/ashubham">LinkedIn</a><a href="https://sessionize.com/ashish-shubham1474/">Speaker profile</a></div></section>
</div></main><footer class="footer"><div class="wrap"><div class="footerbar"><a href="#main">Ashish Shubham</a><span>Personal website · Research updated September 28, 2026</span></div>
<details class="sources" id="source-notes"><summary>Sources & editorial notes</summary><p>This profile combines my September 2026 resume with linked publisher, event organizer, company, and patent records. Each linked title leads to its source. This is a researched archive, not a claim that every public appearance or publication has been indexed.</p><ul><li>IEEE World Leaders Summit 2025, IEEE Silicon Valley CyberSec 2026, the nine reviewer / committee entries, career dates, and education follow the supplied resume. Public event details were not independently located for the two IEEE speaking entries.</li><li>The AI Healthcare Conference 2026 entry follows the resume and public speaker profile. The organizer’s current site also contains 2027 dates; no exact 2026 session date is asserted here.</li><li>The API World session topic is listed on my Sessionize profile alongside the September 2026 event history. AI DevSummit’s keynote is also listed by DeveloperWeek Management.</li><li>Scheduled October and November 2026 talks are organizer listings as of the research date; schedules may change. Entries with a year only do not imply an exact date or completed appearance.</li><li>Patent continuation grants are grouped rather than counted as separate inventions. The USPTO’s June 2026 grant record supersedes the older pending label for Intelligent Search Modification Guidance.</li><li>Media labels distinguish a podcast interview, profile, event recap, award feature, press release, and company mention. Publisher headlines are reproduced as titles, not adopted as independent claims.</li><li>Portrait source: <a href="https://www.thoughtspot.com/author/ashish-shubham">ThoughtSpot author profile</a>. The book is coauthored with Sayantan Ghosh.</li></ul></details></div></footer>
<script>document.querySelectorAll('a[href="#source-notes"]').forEach(function(a){a.addEventListener('click',function(){document.getElementById('source-notes').open=true;});});</script>
</body></html>'''
(ROOT/'index.html').write_text(out)
# Maintain a human-readable source inventory outside the public page.
lines=['# Research and source inventory','',f'Researched as of {d["asOf"]}.','', 'The supplied AshishShubhamResumeSep.pdf is the source for career dates, education, the nine reviewer/committee entries, and resume-only speaking listings. The original resume is not bundled or published by this site.','']
for cat in ['talks','writing','patents','media','projects']:
    lines+=['## '+cat.title(),'']
    for item in d[cat]:
        if cat=='patents':
            lines+=['### '+item['title']]+[f'- [{r[0]}]({r[2]}) — {r[1]}' for r in item['records']]+['']
        elif cat=='projects':lines+=[f'- [{item[0]}]({item[2]}) — {item[3]}']
        else:
            title=item.get('event',item['title']);url=item['url'];lines+=[f'- [{title}]({url}) — {item.get("date", "")}']
            if item.get('resume'):lines+=['  - Resume source; public event record not located.']
            if item.get('note'):lines+=['  - '+item['note']]
    lines+=['']
lines+=['## Additional sources','','- [ThoughtSpot author profile](https://www.thoughtspot.com/author/ashish-shubham)','- [Sessionize profile and event history](https://sessionize.com/ashish-shubham1474/)','- [DevNetwork advisory boards](https://www.devnetwork.com/advisory-boards/)','- [SARC editorial board](https://sarcouncil.com/Editorial-Board-Journal-Innovative-Science/)','- [Business Intelligence Group judge directory](https://www.bintelligence.com/judges?75dd0f39_page=37&e3f2094b_page=37)','- [Medium author archive](https://ashishshubham.medium.com/)','- [Book listing](https://www.goodreads.com/book/show/245530543-architecting-ai-data-systems)','','## Editorial decisions','','- Use the resume’s Engineering Fellow / VP title; the Applied AI Summit listing uses SVP, which was not adopted.','- Avoid unverified revenue claims in the biography; the podcast title retains the host’s wording and is labeled as a title.','- Group six verified U.S. grants across three invention families, plus one additional published agentic-analysis application. Do not count the 2021 application publication as an additional grant.','- Do not attribute US12591579B2 to Ashish: it is a different invention surfaced in a broad assignee listing.','- No exhaustive-search guarantee. Private judging invitations and unindexed appearances cannot be independently recovered.','- Portrait: https://media.thoughtspot.com/35707/1624421600-ashish-headshot.jpeg','- Static page contains no tracking, analytics, remote fonts, or JavaScript dependencies.']
(ROOT/'SOURCES.md').write_text('\n'.join(lines)+'\n')
print('Built index.html:',len(out.encode()),'bytes')
print('Talks:',len(d['talks']),'Writing:',len(d['writing']),'Patent families:',len(d['patents']),'Media:',len(d['media']))
