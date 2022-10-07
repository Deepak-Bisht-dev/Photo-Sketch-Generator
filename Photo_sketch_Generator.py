def PhotoSketchGenerator(photo, k_size):
    
    #import opencv module for the operations in image
    import cv2
    import matplotlib.pyplot as plt

    #Read Image
    img = cv2.imread(photo)
    
    # Convert BGR image to RGB format
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert to Grey Image
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img = cv2.bitwise_not(grey_img)
    #invert_img=255-grey_img

    # Blur image
    blur_img = cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img = cv2.bitwise_not(blur_img)
    #invblur_img=255-blur_img

    # Sketch Image
    sketch_img = cv2.divide(grey_img,invblur_img, scale=256.0)


    # Save Sketch 
    cv2.imwrite('sketch.png', sketch_img)

    # Display sketch
    # cv2.imshow("Image", img)
    # cv2.imshow('RGB image', rgb_img)
    # cv2.imshow('Grey image',grey_img)
    # cv2.imshow('Invert image',invert_img)
    # cv2.imshow('Blur image',blur_img)
    # cv2.imshow('Sketch image',sketch_img)

    plt.figure(figsize=(17,10))
    plt.subplot(1,5,1)
    plt.title('Original image', size = 20)
    plt.imshow(rgb_img)
    plt.axis('off')
    plt.subplot(1,5,2)
    plt.title('Grey image', size = 20)
    plt.imshow(grey_img)
    plt.axis('off')
    plt.subplot(1,5,3)
    plt.title('Inverted image', size = 20)
    plt.imshow(invert_img)
    plt.axis('off')
    plt.subplot(1,5,4)
    plt.title('Blur image', size = 20)
    plt.imshow(blur_img)
    plt.axis('off')
    plt.subplot(1,5,5)
    plt.title('Sketch', size=20)
    rgb_sketch = cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_sketch)
    plt.axis('off')
    plt.show()

    # plt.figure(figsize=(17,10))
    # plt.subplot(1,2,1)
    # plt.title('Original image', size = 20)
    # plt.imshow(rgb_img)
    # plt.axis('on')
    # plt.subplot(1,2,2)
    # plt.title('Sketch', size=20)
    # rgb_sketch = cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
    # plt.imshow(rgb_sketch)
    # plt.axis('off')
    # plt.show()



    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#Function call
PhotoSketchGenerator(photo = 'Avengers.jpg', k_size = 7)