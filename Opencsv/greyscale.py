import cv2

image=cv2.imread('C:\\Users\\Aksha\\OneDrive\\Desktop\\Random stuff 2\\Legion wallpapers\\Wallpaper legion.png')

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resized_image=cv2.resize(gray_image,(400,500))
cv2.imshow('procecssed image',resized_image)
key=cv2.waitKey(0)

if key==ord('s'):
    cv2.imwrite('greyscale_image.png',resized_image)
    print('image saved as greyscale_image.png')
else:
    print('image not saved')

cv2.destroyAllWindows()

print(f"processed image dimensions: {resized_image.shape}")