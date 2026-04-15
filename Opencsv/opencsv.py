import cv2

image = cv2.imread('C:\\Users\\Aksha\\OneDrive\\Desktop\\Random stuff 2\\Legion wallpapers\\Wallpaper legion.png')

cv2.namedWindow('loaded image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('loaded image', 800, 500)

cv2.imshow('loaded image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"image dimensions: {image.shape}")

