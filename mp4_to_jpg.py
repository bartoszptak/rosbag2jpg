import os
from pathlib import Path
import click
import cv2
import numpy as np


@click.command()
@click.option('--video', default=None, type=str, help='Path to video', required=True)

def main(video: str):
    cap = cv2.VideoCapture(video)
    
    dest = Path(os.path.join('outputs', video.split('/')[-1].split('.')[0]))
    dest.mkdir(exist_ok=True, parents=True)
    
    i = 0
    while(cap.isOpened()):
        ret, frame = cap.read()

        if i%30 == 0:
            cv2.imwrite(str(dest) + f'/{i:05d}.jpg', frame)  
    
        i+=1
        
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
    
