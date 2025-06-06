import base64
import zlib
import marshal
import types
import time
#please skid it to the max boss 
#i was to lazy to add some GUI/CLI 
def decode_payload(payload_str):
    reversed_str = payload_str[::-1]
    decoded = base64.b64decode(reversed_str)
    decompressed = zlib.decompress(decoded)
    return decompressed

def find_payload_recursive(consts):
    for const in consts:
        if isinstance(const, (str, bytes)):
            try:
                candidate = const.decode() if isinstance(const, bytes) else const
            except:
                continue
            stripped = candidate.strip()
            if len(stripped) > 100 and all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=\n\r" for c in stripped):
                return stripped
        elif isinstance(const, types.CodeType):
            result = find_payload_recursive(const.co_consts)
            if result:
                return result
    return None

def main():
    filename = "payload.txt"
    with open(filename, "r") as f:
        current_payload = f.read().strip()

    depth = 0
    while True:
        depth += 1
        try:
            decompressed = decode_payload(current_payload)
            code_obj = marshal.loads(decompressed)
            if not isinstance(code_obj, types.CodeType):
                print("Not a code object, stopping.")
                break

            next_payload_candidate = find_payload_recursive(code_obj.co_consts)
            if next_payload_candidate:
                print(f"Step {depth}: Found nested encoded payload, decoding again...")
                current_payload = next_payload_candidate
                continue
            else:
                print(f"Step {depth}: No more nested payloads found. Final code object reached!")
                import dis
                dis.dis(code_obj)
                break

        except Exception as e:
            print(f"Error at step {depth}: {e}")
            break
time.sleep(1000)
if __name__ == "__main__":
    main()
