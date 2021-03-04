import pytesseract
import cv2


#image2text
img2 = cv2.imread('/Users/apple/Downloads/alphabet.png')
text2 = pytesseract.image_to_string(img2)
print("\n" + text2)