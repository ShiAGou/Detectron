import cv2
import glob
import os

def imgs2video(img_path, destination, fps=24):
    imgs = list(glob.iglob(img_path+'/*.png'))
    imgs.sort()
    if not len(imgs):
        return
    h, w, c = cv2.imread(imgs[0]).shape
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video = cv2.VideoWriter(destination, fourcc, 24, (w, h))
    print('video '+ destination + ' starts...')
    for img in imgs:
        print ('writing '+ img)
        video.write(cv2.imread(img))
    video.release()


if __name__ == '__main__':
    sp = '/home/shiwenlei/experiment/Data/MOT17/infer/detectron'
    flist = os.listdir(sp)
    for f in flist:
        vname = os.path.join(sp, f+'.avi')
        img_path = os.path.join(sp, f+'/img1')
        print (img_path)
        imgs2video(img_path, vname)


