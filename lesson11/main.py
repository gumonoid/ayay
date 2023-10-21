from recognizeimg import RecognizeImg
path = 'img/man.jpeg'
winName = 'Man'
fileName = 'haarcascade_frontalface_default.xml'

rec = RecognizeImg(path)
rec.ShowImg(winName)

rec.GetCoordinates(fileName)
print(rec.MultiScale)

rec.HighLight()
rec.ShowImg(winName)

newPath = 'img/glasses.jpeg'
newPhotoPath = 'img/man_with_glasses.png'
rec.AddImage(newPath, newPhotoPath)
rec.ShowImg('AddImage Man')