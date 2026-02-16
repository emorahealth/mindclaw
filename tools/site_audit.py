import urllib.request
import urllib.error
import urllib.parse
import re
import time
from html.parser import HTMLParser

BASE_URL = "https://www.emorahealth.com"
MAX_PAGES = 10  # Limit to avoid timeout

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = set()
        self.tags = {} 
        self.current_tag = None
        self.text_content = []

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    self.links.add(value)
        elif tag in ['title', 'h1', 'meta']:
            self.tags[tag] = self.tags.get(tag, [])
            if tag == 'meta':
                # Store meta dict
                meta_dict = {k: v for k, v in attrs}
                self.tags['meta'].append(meta_dict)

    def handle_endtag(self, tag):
        self.current_tag = None

    def handle_data(self, data):
        if self.current_tag in ['title', 'h1']:
            self.tags[self.current_tag].append(data.strip())
        if self.current_tag not in ['script', 'style']:
            self.text_content.append(data.strip())

def fetch_page(url):
    start_time = time.time()
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'EmoraGrowthEngine/1.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
            duration = time.time() - start_time
            return content, duration, response.getcode()
    except Exception as e:
        return None, 0, str(e)

def analyze_page(url, content, duration):
    parser = LinkParser()
    parser.feed(content)
    
    # Extract Data
    title = "".join(parser.tags.get('title', []))
    h1s = parser.tags.get('h1', [])
    metas = parser.tags.get('meta', [])
    description = next((m.get('content') for m in metas if m.get('name') == 'description'), None)
    word_count = len(" ".join(parser.text_content).split())
    
    # Internal Links
    internal_links = set()
    for link in parser.links:
        full_link = urllib.parse.urljoin(BASE_URL, link)
        if full_link.startswith(BASE_URL) and full_link != BASE_URL:
            internal_links.add(full_link)

    # Scoring
    score = 100
    issues = []
    
    if not title:
        score -= 10
        issues.append("Missing Title")
    elif len(title) > 60:
        score -= 5
        issues.append("Title too long")
        
    if not description:
        score -= 10
        issues.append("Missing Meta Description")
        
    if not h1s:
        score -= 10
        issues.append("Missing H1")
    elif len(h1s) > 1:
        score -= 5
        issues.append("Multiple H1s")
        
    if word_count < 300:
        score -= 10
        issues.append(f"Thin content ({word_count} words)")
        
    if duration > 1.0:
        score -= 5
        issues.append(f"Slow load ({duration:.2f}s)")

    return {
        "url": url,
        "score": score,
        "title": title,
        "h1": h1s[0] if h1s else "N/A",
        "description": description,
        "load_time": duration,
        "issues": issues,
        "internal_links": internal_links
    }

def main():
    print(f"🦞 Crawling {BASE_URL} + 1 level depth...\n")
    
    # Homepage
    content, duration, status = fetch_page(BASE_URL)
    if not content:
        print(f"CRITICAL: Failed to fetch homepage. {status}")
        return

    home_analysis = analyze_page(BASE_URL, content, duration)
    
    results = [home_analysis]
    queue = list(home_analysis['internal_links'])
    visited = {BASE_URL}
    
    print(f"Found {len(queue)} internal links on homepage. Scanning top {MAX_PAGES}...")
    
    for link in queue[:MAX_PAGES]:
        if link in visited: continue
        visited.add(link)
        
        c, d, s = fetch_page(link)
        if c:
            analysis = analyze_page(link, c, d)
            results.append(analysis)
            print(f"Scanned: {link} (Score: {analysis['score']})")
        else:
            print(f"Failed: {link} ({s})")
            
    # Report
    print("\n" + "="*40)
    print("       EMORAHEALTH.COM AUDIT REPORT       ")
    print("="*40 + "\n")
    
    avg_score = sum(r['score'] for r in results) / len(results)
    print(f"OVERALL SITE SCORE: {avg_score:.1f}/100\n")
    
    for r in results:
        print(f"📄 {r['url']}")
        print(f"   Score: {r['score']}")
        print(f"   Title: {r['title']}")
        print(f"   H1: {r['h1']}")
        print(f"   Load: {r['load_time']:.2f}s")
        if r['issues']:
            print(f"   ⚠️ Issues: {', '.join(r['issues'])}")
        print("-" * 20)

if __name__ == "__main__":
    main()
