import base64
import argparse
import hashlib

def main():
    parser = argparse.ArgumentParser(description="Decode Base64 text to a ZIP file.")
    parser.add_argument("input_txt", help="Input Base64 text file")
    parser.add_argument("-o", "--output", help="Output ZIP file (default: <input_txt>.zip)")
    args = parser.parse_args()

    output_zip = args.output if args.output else f"{args.input_txt}.zip"

    try:
        print("Decoding File...")
        with open(args.input_txt, "r") as f_in:
            encoded = f_in.read().strip()  
        
        decoded = base64.b64decode(encoded)
        with open(output_zip, "wb") as f_out:
            f_out.write(decoded)
        
        with open(output_zip, "rb") as f_out:
            sha256 = hashlib.sha256(f_out.read()).hexdigest()
            print(f"Decoded to: {output_zip}")
            print(f"SHA-256 checksum: {sha256}")
        print("Decode successfully !")

    except FileNotFoundError:
        print(f"Error: File '{args.input_txt}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()