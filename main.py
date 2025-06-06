def text_to_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    try:
        return ''.join(chr(int(b, 2)) for b in binary.split())
    except ValueError:
        return "Invalid binary input"

print("Choose conversion:")
print("1. Text to Binary (computer format)")
print("2. Binary to Text (human-readable)")

choice = input("Enter 1 or 2: ")
if choice == '1':
    text = input("Enter text: ")
    print("Binary:", text_to_binary(text))
elif choice == '2':
    binary = input("Enter binary (space-separated): ")
    print("Text:", binary_to_text(binary))
else:
    print("Invalid option.")

