# main.py
import os
import json
import time
from dotenv import load_dotenv
from rich import print
from rich.prompt import Prompt

load_dotenv()

PERSONALITY_FILE = "ersonality.json"
OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
GPT4ALL_MODEL = os.getenv("GPT4ALL_PATH", "")  # optional local model path

# Load personality
with open(PERSONALITY_FILE, "r", encoding="utf-8") as f:
    persona = json.load(f)

current_mode = "friendly"

def build_system_prompt(mode_key):
    core = persona["identity"]
    mode = persona["modes"].get(mode_key, {})
    mode_instr = mode.get("instructions", "")
    honesty = persona.get("honesty_rule", "")
    prompt = f"{core}\nMode: {mode_key} - {mode.get('label','')}\nMode instructions: {mode_instr}\nGlobal rule: {honesty}\nLanguage preference: {','.join(persona.get('default_language', ['en']))}\nRespond as a human friend; use casual slang, code-switch to Hindi when needed."
    return prompt

# Minimal engine: choose remote or local model
def query_llm(user_text, system_prompt):
    """
    Query either OpenAI GPT or GPT4All (if available).
    Falls back to a friendly message if neither is configured.
    """
    # First, try OpenAI if key exists
    if OPENAI_KEY:
        try:
            import openai
            openai.api_key = OPENAI_KEY
            resp = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_text}
                ],
                max_tokens=300
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            print(f"[red]OpenAI error:[/red] {e}")

    # Then, try GPT4All if path exists
    if GPT4ALL_MODEL and GPT4ALL_MODEL.strip():
        try:
            from gpt4all import GPT4All
            gptj = GPT4All(GPT4ALL_MODEL)
            prompt = f"{system_prompt}\nUser: {user_text}\nTiulen:"
            out = gptj.generate(prompt=prompt, max_tokens=300)
            return out
        except Exception as e:
            print(f"[red]gpt4all error:[/red] {e}")

    # Fallback if nothing is configured
    return "Yo bro — Tiulen doesn't have an LLM key or local model ready. Put OPENAI_API_KEY in .env or set GPT4ALL_PATH."

def handle_command(text):
    global current_mode
    t = text.lower().strip()
    if t.startswith("tiulen, switch to "):
        target = t.replace("tiulen, switch to ", "").strip()
        if target in persona["modes"]:
            current_mode = target
            return f"[green]Mode switched to:[/green] {target}"
        else:
            return f"[yellow]Unknown mode:[/yellow] {target}. Available: {', '.join(persona['modes'].keys())}"
    if "tiulen, activate master control" in t:
        return "[magenta]Master control activated. Awaiting commands.[/magenta]"
    if "tiulen, self destruct" in t:
        # Placeholder: we will later implement crypto-key delete
        return "[red]SELF-DESTRUCT initiated (simulation). All ephemeral session data cleared.[/red]"
    if t in ("exit", "quit", "shutdown"):
        print("[bold red]Shutting down Tiulen. Catch you later, bro.[/bold red]")
        raise SystemExit
    return None

def main_loop():
    print("[bold cyan]Tiulen — MVP text mode[/bold cyan]")
    print(f"[dim]Loaded modes: {', '.join(persona['modes'].keys())}[/dim]")
    print("[yellow]Type messages. Use 'Tiulen, switch to <mode>' to change mode. Type 'exit' to quit.[/yellow]\n")
    while True:
        try:
            user = Prompt.ask("[white]You[/white]")
            cmd_resp = handle_command(user)
            if cmd_resp:
                print(cmd_resp)
                continue
            sys_prompt = build_system_prompt(current_mode)
            print("[dim]Tiulen is thinking...[/dim]")
            resp = query_llm(user, sys_prompt)
            # basic postprocess to ensure honesty rule (placeholder)
            print(f"[bold green]Tiulen ({current_mode})[/bold green]: {resp}\n")
        except KeyboardInterrupt:
            print("\n[red]Manual interrupt. Shutting down.[/red]")
            break

if __name__ == "__main__":
    main_loop()
