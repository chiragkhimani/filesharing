import base64
import argparse
import hashlib

def main():
    parser = argparse.ArgumentParser(description="Encode a ZIP file to Base64 text.")
    parser.add_argument("input_zip", help="Input ZIP file to encode")
    parser.add_argument("-o", "--output", help="Output text file (default: <input_zip>.txt)")
    args = parser.parse_args()

    output_txt = args.output if args.output else f"{args.input_zip}.txt"

    try:
        print("Encoding File....")
        with open(args.input_zip, "rb") as f_in:
            encoded = base64.b64encode(f_in.read()).decode("utf-8")
        
        with open(output_txt, "w") as f_out:
            f_out.write(encoded)
        
        with open(args.input_zip, "rb") as f_in:
            sha256 = hashlib.sha256(f_in.read()).hexdigest()
            print(f"Encoded to: {output_txt}")
            print(f"SHA-256 checksum: {sha256}")
        print('Encoded Successfully!')
        
    except FileNotFoundError:
        print(f"Error: File '{args.input_zip}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()