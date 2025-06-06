
---

# Payload Decoder

This tool helps you decode obfuscated Python payloads that use layered base64, zlib, and marshal compression.

---

## How to Use

1. Search your code for this pattern:

```
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'PAYLOAD'))
```

2. Copy the payload string inside the `b'...'` section (without the starting `b'` and ending `'`) into a file named `payload.txt`.

3. Run the script `main.py`. It will automatically decode the payload layer by layer until fully restored.

4. If the console closes unexpectedly, re-open it via CMD or terminal and check the error for troubleshooting.

---

## Legal Disclaimer

This tool is provided **as-is** for educational and research purposes only. By using this software, you agree that you are solely responsible for how you use it.

**I am not responsible for any damage, legal issues, or consequences that may arise from its use.** Use this tool only on code and payloads you have explicit permission to analyze.

By using or distributing this code, you agree to hold the author(s) and maintainers harmless from any claims or liabilities.

---

