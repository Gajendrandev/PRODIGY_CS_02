from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    encrypted_image = Image.new(image.mode, (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    decrypted_image = Image.new(image.mode, (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_image.putpixel((x, y), decrypted_pixel)

    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    while True:
        print("Select an option:")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            image_path = input("Enter the path to the image to encrypt: ")
            key = int(input("Enter the encryption key (integer value): "))
            encrypt_image(image_path, key)
        elif choice == '2':
            image_path = input("Enter the path to the image to decrypt: ")
            key = int(input("Enter the decryption key (integer value): "))
            decrypt_image(image_path, key)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
