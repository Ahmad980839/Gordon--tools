import random
import requests
import time
import os
import re
import sys

# نظام ألوان متطور مخيف
class BloodRedColors:
    DARK_RED = '\033[38;2;139;0;0m'      # دم غامق
    BLOOD_RED = '\033[38;2;220;20;60m'   # أحمر الدم
    FIRE_RED = '\033[38;2;255;69;0m'     # أحمر النار
    DEMON_RED = '\033[38;2;178;34;34m'   # أحمر شيطاني
    HELL_ORANGE = '\033[38;2;255;140;0m' # برتقالي جهنم
    SKULL_WHITE = '\033[38;2;245;245;245m' # أبيض عظام
    GHOST_GRAY = '\033[38;2;169;169;169m'  # رمزي شبح
    DARK_PURPLE = '\033[38;2;75;0;130m'  # بنفسجي داكن
    POISON_GREEN = '\033[38;2;0;255;127m' # أخضر سام
    BONE_YELLOW = '\033[38;2;218;165;32m' # أصفر عظام
    
    # تأثيرات خاصة
    BLOOD_DRIP = '\033[38;2;220;20;60m\033[48;2;30;0;0m'
    HELL_FLAME = '\033[38;2;255;69;0m\033[48;2;50;0;0m'
    SKULL_EFFECT = '\033[38;2;245;245;245m\033[48;2;20;20;20m'
    
    # كود التحكم
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# إيموجيات مرعبة
DEMON_EMOJIS = {
    "skull": "💀", "devil": "👹", "ghost": "👻", "fire": "🔥", 
    "knife": "🔪", "gun": "🔫", "bomb": "💣", "alien": "👽",
    "snake": "🐍", "spider": "🕷️", "bat": "🦇", "wolf": "🐺",
    "claw": "🦴", "voodoo": "🧿", "coffin": "⚰️", "tomb": "🪦",
    "syringe": "💉", "chains": "⛓️", "dagger": "🗡️", "mask": "🎭"
}

# شعار GORDON المخيف والدامي
def show_nightmare_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"""{BloodRedColors.BLOOD_DRIP}
    
    {BloodRedColors.HELL_FLAME}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{BloodRedColors.RESET}
    {BloodRedColors.BLOOD_DRIP}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{BloodRedColors.RESET}
    
    {BloodRedColors.FIRE_RED}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{BloodRedColors.RESET}
    {BloodRedColors.DEMON_RED}███████╗  ██████╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗     ███████╗██╗  ██╗███████╗██████╗ ███████╗██████╗ {BloodRedColors.RESET}
    {BloodRedColors.BLOOD_RED}██╔════╝ ██╔════╝██╔═══██╗██╔══██╗██╔═══██╗████╗  ██║     ██╔════╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗{BloodRedColors.RESET}
    {BloodRedColors.FIRE_RED}██║  ███╗██║     ██║   ██║██║  ██║██║   ██║██╔██╗ ██║     ███████╗███████║█████╗  ██████╔╝█████╗  ██║  ██║{BloodRedColors.RESET}
    {BloodRedColors.DEMON_RED}██║   ██║██║     ██║   ██║██║  ██║██║   ██║██║╚██╗██║     ╚════██║██╔══██║██╔══╝  ██╔══██╗██╔══╝  ██║  ██║{BloodRedColors.RESET}
    {BloodRedColors.BLOOD_RED}╚██████╔╝╚██████╗╚██████╔╝██████╔╝╚██████╔╝██║ ╚████║     ███████║██║  ██║███████╗██║  ██║███████╗██████╔╝{BloodRedColors.RESET}
    {BloodRedColors.FIRE_RED} ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ {BloodRedColors.RESET}
    {BloodRedColors.DEMON_RED}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{BloodRedColors.RESET}
    
    {BloodRedColors.SKULL_EFFECT}                  ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗                  {BloodRedColors.RESET}
    {BloodRedColors.SKULL_EFFECT}                  ║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╔══╝║╔══╝                  {BloodRedColors.RESET}
    {BloodRedColors.SKULL_EFFECT}                  ║╚══╗║║─║║║╚═╝║║║─║║║╚══╗║╚══╗                  {BloodRedColors.RESET}
    {BloodRedColors.SKULL_EFFECT}                  ╚══╗║║║─║║║╔╗╔╝║║─║║║╔══╝║╔══╝                  {BloodRedColors.RESET}
    {BloodRedColors.SKULL_EFFECT}                  ║╚═╝║║╚═╝║║║║╚╗║╚═╝║║╚══╗║╚══╗                  {BloodRedColors.RESET}
    {BloodRedColors.SKULL_EFFECT}                  ╚═══╝╚═══╝╚╝╚═╝╚═══╝╚═══╝╚═══╝                  {BloodRedColors.RESET}
    {BloodRedColors.SKULL_EFFECT}                  G   O   R   D   O   N                         {BloodRedColors.RESET}
    
    {BloodRedColors.POISON_GREEN}╔══════════════════════════════════════════════════════════════════════════════════════════════════╗{BloodRedColors.RESET}
    {BloodRedColors.POISON_GREEN}║ {BloodRedColors.BLINK}{BloodRedColors.BLOOD_RED}👹 DEMON MODE ACTIVATED {DEMON_EMOJIS['skull']} | {DEMON_EMOJIS['devil']} BLOODTHIRSTY BRUTEFORCE {DEMON_EMOJIS['fire']} | {DEMON_EMOJIS['ghost']} SOUL HARVESTER {BloodRedColors.RESET}{BloodRedColors.POISON_GREEN} ║{BloodRedColors.RESET}
    {BloodRedColors.POISON_GREEN}╚══════════════════════════════════════════════════════════════════════════════════════════════════╝{BloodRedColors.RESET}
    
    {BloodRedColors.DARK_PURPLE}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{BloodRedColors.RESET}
    {BloodRedColors.DARK_PURPLE}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{BloodRedColors.RESET}
    
    {BloodRedColors.RESET}""")
    
    # تأثير كتابة مخيف مع إيموجيات
    nightmare_messages = [
        f"{BloodRedColors.BLOOD_RED}[{DEMON_EMOJIS['devil']}] SYSTEM CORRUPTION INITIATED...",
        f"{BloodRedColors.FIRE_RED}[{DEMON_EMOJIS['fire']}] BURNING THROUGH FIREWALLS...",
        f"{BloodRedColors.DEMON_RED}[{DEMON_EMOJIS['skull']}] SOUL COLLECTOR ONLINE...",
        f"{BloodRedColors.POISON_GREEN}[{DEMON_EMOJIS['snake']}] VENOM INJECTION READY...",
        f"{BloodRedColors.HELL_ORANGE}[{DEMON_EMOJIS['alien']}] ALIEN TECHNOLOGY ENGAGED..."
    ]
    
    for msg in nightmare_messages:
        for char in msg:
            print(char, end='', flush=True)
            time.sleep(0.01)
        print()
        time.sleep(0.3)
    
    print(f"\n{BloodRedColors.BONE_YELLOW}{'═' * 100}{BloodRedColors.RESET}\n")

# تأثير كتابة مخيف مع دم
def bloody_print(text, delay=0.02, color=BloodRedColors.BLOOD_RED):
    print(color, end="")
    bloody_chars = ["💉", "🩸", "🔪", "💀"]
    for i, char in enumerate(text):
        print(char, end='', flush=True)
        time.sleep(delay)
        if random.random() < 0.1:  # 10% فرصة لإظهار قطرة دم
            print(f"{BloodRedColors.BLOOD_RED}{random.choice(bloody_chars)}{color}", end='', flush=True)
    print(BloodRedColors.RESET, end="")

# توليد كلمات مرور شيطانية
def generate_demonic_passwords(count=666):
    bloody_print(f"[{DEMON_EMOJIS['devil']}] SUMMONING {count} DEMONIC PASSWORDS FROM HELL...\n", 0.03, BloodRedColors.FIRE_RED)
    
    demonic_words = [
        "satan", "lucifer", "beelzebub", "leviathan", "belial", "asmodai",
        "abaddon", "mammon", "azazel", "moloch", "baal", "dagon", "lilith",
        "cerberus", "hydra", "chimera", "gorgon", "valac", "vassago",
        "baphomet", "incubus", "succubus", "wendigo", "zombie", "vampire",
        "werewolf", "necromancer", "warlock", "sorcerer", "hellspawn"
    ]
    
    satanic_numbers = ["666", "777", "999", "13", "7", "69", "420", "187", "6666"]
    dark_symbols = ["⚰️", "💀", "🔪", "🩸", "🔥", "👹", "👻", "🐍", "🕷️", "⛓️"]
    
    passwords = []
    
    for i in range(count):
        demon = random.choice(demonic_words)
        number = random.choice(satanic_numbers)
        symbol = random.choice(dark_symbols)
        
        patterns = [
            f"{demon.capitalize()}{number}{symbol}",
            f"{symbol}{demon}{random.choice(satanic_numbers)}",
            f"{random.choice(demonic_words)}_{random.choice(demonic_words)}_{number}",
            f"{number}{symbol}{demon.upper()}{symbol}",
            f"{random.choice(dark_symbols)}{demon}{random.choice(['666', '999'])}{random.choice(dark_symbols)}"
        ]
        
        password = random.choice(patterns)
        passwords.append(password)
        
        if i % 100 == 0:
            print(f"{BloodRedColors.DEMON_RED}[{DEMON_EMOJIS['alien']}] Summoned {i}/{count} demonic secrets...{BloodRedColors.RESET}")
    
    bloody_print(f"[{DEMON_EMOJIS['devil']}] {count} DEMONIC PASSWORDS SUMMONED FROM THE ABYSS!\n", 0.02, BloodRedColors.POISON_GREEN)
    return passwords

# نظام هجوم مخيف
class HellfireBruteforce:
    def __init__(self, target, passwords, speed=0.05):
        self.target = target
        self.passwords = passwords
        self.speed = speed
        self.souls_collected = 0
        self.demons_awakened = 0
        
    def execute_torture(self):
        bloody_print(f"\n[{DEMON_EMOJIS['skull']}] TARGET ACQUIRED: @{self.target}\n", 0.03, BloodRedColors.BLOOD_RED)
        bloody_print(f"[{DEMON_EMOJIS['fire']}] PREPARING TORTURE CHAMBER...\n", 0.02, BloodRedColors.FIRE_RED)
        bloody_print(f"[{DEMON_EMOJIS['chains']}] CHAINING {len(self.passwords)} DEMONS TO TARGET...\n\n", 0.02, BloodRedColors.DARK_PURPLE)
        
        time.sleep(1)
        
        found_password = None
        attempts = 0
        
        for idx, password in enumerate(self.passwords, 1):
            attempts = idx
            
            # تأثير تقدم مخيف مع إيموجيات
            percent = (idx / len(self.passwords)) * 100
            
            # شريط تقدم دموي
            bar_width = 50
            filled = int(bar_width * idx // len(self.passwords))
            empty = bar_width - filled
            
            progress_bar = f"{BloodRedColors.BLOOD_RED}{'█' * filled}{BloodRedColors.GHOST_GRAY}{'░' * empty}{BloodRedColors.RESET}"
            
            # إيموجيات عشوائية
            current_emoji = random.choice(list(DEMON_EMOJIS.values()))
            
            sys.stdout.write(f"\r{BloodRedColors.DEMON_RED}[{current_emoji} {idx:04d}/{len(self.passwords):04d}] "
                           f"{BloodRedColors.BLOOD_RED}{progress_bar} "
                           f"{BloodRedColors.HELL_ORANGE}{percent:6.2f}% "
                           f"{BloodRedColors.POISON_GREEN}TORTURING: "
                           f"{BloodRedColors.SKULL_WHITE}{password[:25]:<25}{BloodRedColors.RESET}")
            sys.stdout.flush()
            
            time.sleep(self.speed)
            
            # فرصة نجاح شيطانية (6.66%)
            if random.random() < 0.0666:
                found_password = password
                self.souls_collected += 1
                break
            
            # تأثيرات عشوائية مخيفة
            if random.random() < 0.01:
                print(f"\n{BloodRedColors.BLINK}{BloodRedColors.FIRE_RED}[{DEMON_EMOJIS['fire']}] SCREAM DETECTED! TARGET IS SUFFERING!{BloodRedColors.RESET}")
            
            if random.random() < 0.005:
                print(f"\n{BloodRedColors.BLINK}{BloodRedColors.DEMON_RED}[{DEMON_EMOJIS['ghost']}] SOUL FRAGMENT EXTRACTED!{BloodRedColors.RESET}")
                self.demons_awakened += 1
        
        print("\n")
        print(f"{BloodRedColors.BLOOD_RED}{'🩸' * 50}{BloodRedColors.RESET}\n")
        
        if found_password:
            self.show_victory(found_password, attempts)
        else:
            self.show_defeat(attempts)
        
        return found_password, attempts
    
    def show_victory(self, password, attempts):
        bloody_print(f"\n[{DEMON_EMOJIS['devil']}]{BloodRedColors.BLINK}{BloodRedColors.BLOOD_RED} SOUL SUCCESSFULLY HARVESTED!{BloodRedColors.RESET}\n", 0.05, BloodRedColors.FIRE_RED)
        
        victory_message = f"""
{BloodRedColors.BLOOD_DRIP}╔══════════════════════════════════════════════════════════════════════════════╗{BloodRedColors.RESET}
{BloodRedColors.BLOOD_DRIP}║                    {BloodRedColors.BLINK}{BloodRedColors.FIRE_RED}TARGET ANNIHILATED{BloodRedColors.RESET}{BloodRedColors.BLOOD_DRIP}                       ║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_DRIP}╠══════════════════════════════════════════════════════════════════════════════╣{BloodRedColors.RESET}
{BloodRedColors.BLOOD_DRIP}║ {BloodRedColors.SKULL_WHITE}VICTIM:      {BloodRedColors.POISON_GREEN}@{self.target}                                      {BloodRedColors.BLOOD_DRIP}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_DRIP}║ {BloodRedColors.SKULL_WHITE}PASSWORD:    {BloodRedColors.HELL_ORANGE}{password:<50}  {BloodRedColors.BLOOD_DRIP}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_DRIP}║ {BloodRedColors.SKULL_WHITE}ATTEMPTS:    {BloodRedColors.DEMON_RED}{attempts} DEMONIC ASSAULTS                           {BloodRedColors.BLOOD_DRIP}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_DRIP}║ {BloodRedColors.SKULL_WHITE}SOULS:       {BloodRedColors.BLOOD_RED}{self.souls_collected} SOULS COLLECTED                       {BloodRedColors.BLOOD_DRIP}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_DRIP}║ {BloodRedColors.SKULL_WHITE}DEMONS:      {BloodRedColors.DARK_PURPLE}{self.demons_awakened} DEMONS AWAKENED                      {BloodRedColors.BLOOD_DRIP}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_DRIP}║ {BloodRedColors.SKULL_WHITE}OPERATOR:    {BloodRedColors.FIRE_RED}GORDON - LORD OF TERROR                       {BloodRedColors.BLOOD_DRIP}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_DRIP}╚══════════════════════════════════════════════════════════════════════════════╝{BloodRedColors.RESET}
        """
        
        print(victory_message)
    
    def show_defeat(self, attempts):
        bloody_print(f"\n[{DEMON_EMOJIS['skull']}]{BloodRedColors.DEMON_RED} TARGET RESISTED DEMONIC ASSAULT{BloodRedColors.RESET}\n", 0.05, BloodRedColors.DEMON_RED)
        
        defeat_message = f"""
{BloodRedColors.DARK_PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗{BloodRedColors.RESET}
{BloodRedColors.DARK_PURPLE}║                  {BloodRedColors.GHOST_GRAY}TARGET SURVIVED THE TORTURE{BloodRedColors.RESET}{BloodRedColors.DARK_PURPLE}                    ║{BloodRedColors.RESET}
{BloodRedColors.DARK_PURPLE}╠══════════════════════════════════════════════════════════════════════════════╣{BloodRedColors.RESET}
{BloodRedColors.DARK_PURPLE}║ {BloodRedColors.GHOST_GRAY}VICTIM ESCAPED:   {BloodRedColors.SKULL_WHITE}@{self.target}                                     {BloodRedColors.DARK_PURPLE}║{BloodRedColors.RESET}
{BloodRedColors.DARK_PURPLE}║ {BloodRedColors.GHOST_GRAY}ATTEMPTS MADE:    {BloodRedColors.DEMON_RED}{attempts} DEMONIC ASSAULTS                          {BloodRedColors.DARK_PURPLE}║{BloodRedColors.RESET}
{BloodRedColors.DARK_PURPLE}║ {BloodRedColors.GHOST_GRAY}DEMONS AWAKENED:  {BloodRedColors.DARK_PURPLE}{self.demons_awakened} FROM THE ABYSS                     {BloodRedColors.DARK_PURPLE}║{BloodRedColors.RESET}
{BloodRedColors.DARK_PURPLE}║ {BloodRedColors.GHOST_GRAY}OPERATOR STATUS:  {BloodRedColors.FIRE_RED}GORDON WILL RETURN FOR REVENGE                 {BloodRedColors.DARK_PURPLE}║{BloodRedColors.RESET}
{BloodRedColors.DARK_PURPLE}╚══════════════════════════════════════════════════════════════════════════════╝{BloodRedColors.RESET}
        """
        
        print(defeat_message)

# إرسال إنذار شيطاني لـ Telegram
def send_demonic_alert(token, chat_id, target, password):
    demonic_message = f"""
👹 *GORDON'S DEMONIC ALERT* 👹

⚡ *TARGET ANNIHILATED*
{DEMON_EMOJIS['skull']}━━━━━━━━━━━━━━━━━━━━━━{DEMON_EMOJIS['skull']}
👤 *Victim:* `{target}`
🔑 *Soul Key:* `{password}`
🩸 *Status:* SOUL HARVESTED
🕒 *Time:* {time.strftime('%Y-%m-%d %H:%M:%S')}
{DEMON_EMOJIS['fire']}━━━━━━━━━━━━━━━━━━━━━━{DEMON_EMOJIS['fire']}
⚡ *System:* GORDON's Hellfire v9.66
👹 *Operator:* LORD GORDON
🔮 *Power Level:* DEMONIC
{DEMON_EMOJIS['chains']}━━━━━━━━━━━━━━━━━━━━━━{DEMON_EMOJIS['chains']}
"""
    
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": demonic_message,
            "parse_mode": "Markdown"
        }
        requests.post(url, data=data, timeout=10)
        bloody_print(f"[{DEMON_EMOJIS['alien']}] DEMONIC ALERT SENT TO THE VOID!\n", 0.03, BloodRedColors.POISON_GREEN)
        return True
    except:
        bloody_print(f"[{DEMON_EMOJIS['skull']}] FAILED TO CONNECT TO THE ABYSS!\n", 0.03, BloodRedColors.DEMON_RED)
        return False

# القائمة الرئيسية السوداء
def main():
    while True:
        show_nightmare_banner()
        
        menu = f"""
{BloodRedColors.BLOOD_RED}╔══════════════════════════════════════════════════════════════════════════════╗{BloodRedColors.RESET}
{BloodRedColors.BLOOD_RED}║                  {BloodRedColors.BLINK}{BloodRedColors.FIRE_RED}GORDON'S TORTURE CHAMBER{BloodRedColors.RESET}{BloodRedColors.BLOOD_RED}                     ║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_RED}╠══════════════════════════════════════════════════════════════════════════════╣{BloodRedColors.RESET}
{BloodRedColors.BLOOD_RED}║ {BloodRedColors.POISON_GREEN}[1]{BloodRedColors.SKULL_WHITE} SINGLE SOUL HARVEST {DEMON_EMOJIS['skull']}                                 {BloodRedColors.BLOOD_RED}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_RED}║ {BloodRedColors.POISON_GREEN}[2]{BloodRedColors.SKULL_WHITE} MASS SOUL COLLECTION {DEMON_EMOJIS['ghost']}                              {BloodRedColors.BLOOD_RED}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_RED}║ {BloodRedColors.POISON_GREEN}[3]{BloodRedColors.SKULL_WHITE} SUMMON DEMONIC PASSWORDS {DEMON_EMOJIS['devil']}                         {BloodRedColors.BLOOD_RED}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_RED}║ {BloodRedColors.POISON_GREEN}[4]{BloodRedColors.SKULL_WHITE} SACRIFICE TO THE VOID {DEMON_EMOJIS['fire']}                             {BloodRedColors.BLOOD_RED}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_RED}║ {BloodRedColors.POISON_GREEN}[5]{BloodRedColors.SKULL_WHITE} ESCAPE HELL {DEMON_EMOJIS['coffin']}                                     {BloodRedColors.BLOOD_RED}║{BloodRedColors.RESET}
{BloodRedColors.BLOOD_RED}╚══════════════════════════════════════════════════════════════════════════════╝{BloodRedColors.RESET}

{BloodRedColors.HELL_ORANGE}[{DEMON_EMOJIS['knife']}] SELECT TORTURE METHOD: {BloodRedColors.RESET}"""
        
        bloody_print(menu, 0.01)
        choice = input().strip()
        
        if choice == '1':
            # تعذيب فردي
            show_nightmare_banner()
            target = input(f"{BloodRedColors.BLOOD_RED}[{DEMON_EMOJIS['dagger']}] ENTER SOUL TO HARVEST: {BloodRedColors.RESET}").strip()
            
            # اختيار قائمة التعذيب
            print(f"\n{BloodRedColors.POISON_GREEN}[1]{BloodRedColors.SKULL_WHITE} Load from torture file")
            print(f"{BloodRedColors.POISON_GREEN}[2]{BloodRedColors.SKULL_WHITE} Summon demonic passwords{BloodRedColors.RESET}")
            method = input(f"\n{BloodRedColors.HELL_ORANGE}[{DEMON_EMOJIS['alien']}] SELECT: {BloodRedColors.RESET}")
            
            if method == '1':
                file_path = input(f"{BloodRedColors.DEMON_RED}[{DEMON_EMOJIS['voodoo']}] TORTURE FILE PATH: {BloodRedColors.RESET}")
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        passwords = [line.strip() for line in f if line.strip()]
                    bloody_print(f"[{DEMON_EMOJIS['bat']}] LOADED {len(passwords)} TORTURE METHODS\n", 0.02, BloodRedColors.POISON_GREEN)
                except:
                    bloody_print(f"[{DEMON_EMOJIS['skull']}] FAILED TO READ TORTURE MANUAL!\n", 0.02, BloodRedColors.DEMON_RED)
                    passwords = generate_demonic_passwords(333)
            else:
                count = int(input(f"{BloodRedColors.FIRE_RED}[{DEMON_EMOJIS['snake']}] NUMBER OF DEMONS TO SUMMON: {BloodRedColors.RESET}") or "666")
                passwords = generate_demonic_passwords(count)
            
            speed = float(input(f"{BloodRedColors.HELL_ORANGE}[{DEMON_EMOJIS['fire']}] TORTURE SPEED (0.01-0.5): {BloodRedColors.RESET}") or "0.05")
            
            # إعداد الإنذارات
            print(f"\n{BloodRedColors.POISON_GREEN}[{DEMON_EMOJIS['alien']}] CONFIGURE VOID ALERTS? (y/n): {BloodRedColors.RESET}", end="")
            if input().lower() == 'y':
                token = input(f"{BloodRedColors.DEMON_RED}[{DEMON_EMOJIS['ghost']}] BOT SOUL TOKEN: {BloodRedColors.RESET}")
                chat_id = input(f"{BloodRedColors.DARK_PURPLE}[{DEMON_EMOJIS['coffin']}] VOID CHANNEL ID: {BloodRedColors.RESET}")
            else:
                token = chat_id = None
            
            # بدء التعذيب
            attack = HellfireBruteforce(target, passwords, speed)
            result, attempts = attack.execute_torture()
            
            if result and token and chat_id:
                send_demonic_alert(token, chat_id, target, result)
            
            input(f"\n{BloodRedColors.GHOST_GRAY}[{DEMON_EMOJIS['tomb']}] PRESS ENTER TO RETURN TO HELL{BloodRedColors.RESET}")
            
        elif choice == '5':
            # خروج مخيف
            show_nightmare_banner()
            goodbye = f"""
{BloodRedColors.BLOOD_DRIP}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║      {BloodRedColors.BLINK}{BloodRedColors.FIRE_RED}GORDON'S HELLFIRE SYSTEM SHUTTING DOWN...{BloodRedColors.RESET}{BloodRedColors.BLOOD_DRIP}               ║
║                                                                              ║
║      {BloodRedColors.SKULL_WHITE}Remember: The darkness always returns...{BloodRedColors.BLOOD_DRIP}                          ║
║      {BloodRedColors.DEMON_RED}Your soul is now marked by GORDON{BloodRedColors.BLOOD_DRIP}                                    ║
║                                                                              ║
║      {BloodRedColors.POISON_GREEN}Until we meet again in the abyss...{BloodRedColors.BLOOD_DRIP}                                ║
║      {BloodRedColors.HELL_ORANGE}Operator: LORD GORDON - MASTER OF TERROR{BloodRedColors.BLOOD_DRIP}                           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
{BloodRedColors.RESET}
"""
            print(goodbye)
            
            # تأثير اختفاء
            for i in range(5, 0, -1):
                print(f"{BloodRedColors.BLINK}{BloodRedColors.BLOOD_RED}[{DEMON_EMOJIS['skull']}] VANISHING IN {i}...{BloodRedColors.RESET}")
                time.sleep(1)
            
            break
        
        else:
            bloody_print(f"\n[{DEMON_EMOJIS['skull']}] INVALID SELECTION! THE VOID REJECTS YOU!\n", 0.03, BloodRedColors.DEMON_RED)
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        bloody_print(f"\n\n[{DEMON_EMOJIS['skull']}]{BloodRedColors.BLINK}{BloodRedColors.BLOOD_RED} HELLFIRE INTERRUPTED!{BloodRedColors.RESET}\n", 0.03, BloodRedColors.DEMON_RED)
        bloody_print(f"[{DEMON_EMOJIS['ghost']}] ERASING ALL EVIDENCE FROM THIS REALM...\n", 0.05, BloodRedColors.GHOST_GRAY)
        
        for i in range(3):
            print(f"{BloodRedColors.BLINK}{BloodRedColors.FIRE_RED}[{DEMON_EMOJIS['fire']}] BURNING TRACES...{BloodRedColors.RESET}")
            time.sleep(1)
        
        bloody_print(f"[{DEMON_EMOJIS['coffin']}] ALL TRACES VANISHED INTO THE VOID\n", 0.03, BloodRedColors.POISON_GREEN)
        time.sleep(2)