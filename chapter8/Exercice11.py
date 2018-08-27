import image

def double_image(img):
    double = image.EmptyImage(img.getWidth()*2, img.getHeight()*2)
    print(double)
    for row in range(img.getHeight()):
        for column in range(img.getWidth()):
            double.setPixel(125/255, 125/255,125/255)
 #           p = img.getPixel(column, row)
 #
 #           double.setPixel(2*column,2*row,p)
 #           double.setPixel(2*column+1,2*row,p)
 #           double.setPixel(2*column,2*row+1,p)
 #           double.setPixel(2*column+1,2*row+1,p)
    print(dir(double))
    return double

def smooth(img):
    print(dir(img))
    print(img.getWidth)
    print(img.getWidth())
    oldw = img.getWidth
    oldh = img.getHeight()
    newimg = image.EmptyImage(oldw,oldh)

    for col in range(oldw):
        for row in range(oldh):
            p = newimg.getPixel(col,row)
            neighbors = []

            for i in range(col-1,col+2):
                for j in range(row-1,row+2):
                    try:
                        neighbor = img.getPixel(i,j)
                        neighbors.append(neighbor)
                    except:
                        continue

            nlen = len(neighbors)
            if nlen:
                red = 0
                green = 0
                blue = 0

                for i in range(nlen):
                    red += int(neighbors[i][0])
                    green += int(neighbors[i][1])
                    blue += int(neighbors[i][2])
                p.red = red/nlen
                p.green = green/nlen
                p.blue = blue/nlen

                newimg.setPixel(col,row,p)

    return newimg

def main():
    img = image.Image("luther.jpg")
    win = image.ImageWin(img.getWidth()*2,img.getHeight()*2)
    double_img = double_image(img)
    print(dir(double_img))
    smooth_image = smooth(double_img)
    #smooth_image.draw(win)

if __name__ == '__main__':
    main()
