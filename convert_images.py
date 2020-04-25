from PIL import Image
import os, sys



def convert_images(fromdir, todir, fromext, toext, prefix):
  print("Converting " +fromext+ " in " +fromdir+ " to " +toext+ " in " + todir)
  i = 101
  for root, dirs, files in os.walk(fromdir):
     for filename in sorted(files):
        if filename.endswith("." + fromext):
          #jpg = prefix+filename.replace(fromdir,"").replace(fromext,"") + toext
          jpg = "{:05}.jpg".format(i)
          i += 1
          print("converting " + filename + " to " + jpg)
          png = Image.open(fromdir + filename)
          png.save(todir + jpg)
  print("Done")


vid = sys.argv[1] if len(sys.argv) > 1 else 1

vid = "/home/ec2-user/efs/julia/JAAD/images/video_{:04}/".format(int(vid))

convert_images(vid, "/home/ec2-user/.julia/packages/YOLO/5usZN/data/datasets/voc2007/VOCdevkit/VOC2007/JPEGImages/", "png", "jpg", "")

