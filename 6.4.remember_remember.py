from PIL import Image

def decode_message(file_path):
    image = Image.open(file_path)
    image.show()
    width, height = image.size
    message = ''
    for x in range(30,width):
        y = 0
        while y < height and image.getpixel((x,y)) != 0:
            y += 1
        if y < height:
            message += chr(y)
            print('ok')
    return message



def main():
    print(decode_message('code.png'))

if __name__ == "__main__":
    main()