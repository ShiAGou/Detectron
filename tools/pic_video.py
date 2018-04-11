import cv2
import glob
import os
import sys

def imgs2video(img_path, destination, fps=24):
    imgs = list(glob.iglob(img_path+'/*.png'))
    imgs.sort()
    if not len(imgs):
        return
    h, w, c = cv2.imread(imgs[0]).shape
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video = cv2.VideoWriter(destination, fourcc, fps, (w, h))
    # print('video '+ destination + ' starts...')
    for img in imgs:
        print ('writing '+ img)
        video.write(cv2.imread(img))
    video.release()


def video2imgs(v_path, destination, low=0, high=0):
    v_name = os.path.basename(v_path)
    video = cv2.VideoCapture(v_path)
    rval = video.isOpened()
    if (rval and high <= 0)
        high = sys.maxints
    cnt = 0
    while(rval and cnt<high)
        rval, frame = video.read()
        cnt = cnt+1
        if (cnt < low):
            continue
        img_name = v_name+'_'+str(cnt).zfill(10)+'.jpg'
        print('saving '+img_name +'...')
        cv2.imwrite(os.path.join(destination, img_name), frame)
    video.release()
    return cnt


if __name__ == '__main__':
    '''
    sp = '/home/shiwenlei/experiment/Data/MOT17/infer/detectron'
    flist = os.listdir(sp)
    for f in flist:
        vname = os.path.join(sp, f+'.avi')
        img_path = os.path.join(sp, f+'/img1')
        print (img_path)
        imgs2video(img_path, vname)
    '''
    sp = '/home/shiwenlei/Downloads/nihao.mp4'
    dest = '/home/shiwenlei/experiment/Data/Detectron/nihao'
    video2imgs(sp, destination, low=3600, high=7200)



