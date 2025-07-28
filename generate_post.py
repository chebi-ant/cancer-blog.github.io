#!/usr/bin/env python3
"""
Cancer Blog Post Generator
Creates weekly blog posts with rotating topics
"""

import os
import datetime
from pathlib import Path

# Weekly prompts that rotate based on week number
PROMPTS = [
    "What is Cancer, Really?",
    "How Chronic Inflammation Contributes to Cancer",
    "Nutrition and Cancer: What Science Says",
    "The Role of Genetics in Cancer Risk",
    "Can Exercise Prevent Cancer?",
    "Radiation vs. Chemotherapy: What's the Difference?",
    "The History of Cancer Research",
    "How Does the Immune System Fight Cancer?",
    "Cancer Screening: Early Detection Saves Lives",
    "Understanding Cancer Staging and Prognosis",
    "The Psychology of Cancer Diagnosis",
    "Breakthrough Cancer Treatments in 2025"
]

def create_slug(title):
    """Convert title to URL-friendly slug"""
    return title.lower().replace(" ", "-").replace(":", "").replace("?", "").replace(",", "")

def get_weekly_prompt():
    """Get prompt based on current week number to ensure rotation"""
    # Get current week number (1-52)
    today = datetime.date.today()
    week_number = today.isocalendar()[1]
    
    # Cycle through prompts
    prompt_index = (week_number - 1) % len(PROMPTS)
    return PROMPTS[prompt_index]

def generate_post():
    """Generate a new blog post"""
    # Get current date
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d")
    
    # Get this week's topic
    title = get_weekly_prompt()
    slug = create_slug(title)
    
    # Create filename
    filename = f"{date_str}-{slug}.md"
    
    # Ensure _posts directory exists
    posts_dir = Path("_posts")
    posts_dir.mkdir(exist_ok=True)
    
    # Full file path
    file_path = posts_dir / filename
    
    # Check if post already exists
    if file_path.exists():
        print(f"Post already exists: {filename}")
        return False
    
    # Create post content
    content = f"""---
layout: post
title: "{title}"
date: {today.strftime("%Y-%m-%d")}
categories: cancer health
tags: cancer research health awareness
---

## {title}

**[PLACEHOLDER - Replace with AI-generated content]**

This week's topic explores: {title.lower()}

### Key Points to Cover:
- Introduction to the topic
- Current research and findings  
- Practical implications
- Conclusion and takeaways

---

*This post is part of our weekly cancer awareness series. Content will be updated with detailed, AI-generated insights about {title.lower()}.*

### About This Series
Each week, we explore different aspects of cancer to help increase understanding and awareness. Topics are carefully selected to provide valuable, accessible information about cancer prevention, treatment, and research.

**Disclaimer:** This content is for educational purposes only and should not replace professional medical advice. Always consult with healthcare providers for medical decisions.
"""

    # Write the file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created new post: {filename}")
        return True
    except Exception as e:
        print(f"Error creating post: {e}")
        return False

if __name__ == "__main__":
    success = generate_post()
    if not success:
        exit(1)
