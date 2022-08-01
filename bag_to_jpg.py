import os
from pathlib import Path
import click
import cv2
import numpy as np
import rosbag as rsb


@click.command()
@click.option('--rosbag', default=None, type=str, help='Path to rosbag', required=True)
@click.option('--topic', default='/camera/color/image_raw', type=str, help='Image topic name', required=True)
def main(rosbag: str, topic: str):
    bag = rsb.Bag(rosbag, "r")
    
    dest = Path(os.path.join('outputs', rosbag.split('/')[-1].split('.')[0]))
    dest.mkdir(exist_ok=True, parents=True)
    
    i = 0
    
    for topic_name, msg, t in bag.read_messages(topics=[topic]):        
        if topic_name != topic:
            continue
        
        if i%30 == 0:
            img = np.frombuffer(
                    msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1).copy()
            
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

            cv2.imwrite(str(dest) + f'/{t}.jpg', img)  
        
        i += 1
    
        
    cv2.destroyAllWindows()
    bag.close()
    
if __name__ == '__main__':
    main()
    
