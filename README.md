# geometricTransformation

## Scaling

* Resizing the image
* Size of the image can be specified manually, can also be specified with scaling factor

      cv2.INTER_AREA   --> Shrinking
      cv2.INTER_CUBIC  --> Zooming
      cv2.INTER_LINEAR --> Zooming
      
## Translation

* Shifting of object's location

      cv2.warpAffine() --> array
      
## Rotation

      cv2.getRotationMatrix2D(rows,cols)
     
## Affine Transformation

* All parallel lines will be parallel in the output image

## Perspective Transformation

* 4 points --> 3 should not be collinear

* 3 x 3 Transformation Matrix
      
