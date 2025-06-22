import cv2

# Step 1: Get image path from user
image_path = input("Enter image path (e.g., photo.jpg): ")
img = cv2.imread(image_path)

if img is None:
    print("❌ Could not load image. Check the path.")
    exit()

# Step 2: Get new size
width = int(input("Enter new width: "))
height = int(input("Enter new height: "))

# Step 3: Resize the image
resized = cv2.resize(img, (width, height))

# Step 4: Get save path and save
save_path = input("Enter path to save resized image (e.g., resized.jpg): ")
cv2.imwrite(save_path, resized)

print("✅ Image resized and saved successfully!")
