import torch
import numpy as np
from helperGTRS import preprocess_joint, save_obj
from helperPoseDetector import get_2d_pose
import time

image_path = 'Tests/Parshwa.jpeg'

# Load Models
GTRS = torch.jit.load('GTRS.pt')
PoseDetector = torch.jit.load('PoseDetector.pt')
mesh_model_face = np.load('SMPL.npy')

startPose = time.time()

pose = get_2d_pose(image_path, PoseDetector)

endPose = time.time()

joint_input = pose[0]

print("Time taken for pose detection (in milliseconds): ", (endPose-startPose)*1000)

start = time.time()

joint_img = preprocess_joint(joint_input)
joint_img = torch.Tensor(joint_img)
mesh, _ = GTRS(joint_img)

end = time.time()

print("Time taken for mesh reconstruction (in milliseconds): ", (end-start)*1000)

save_obj(mesh, mesh_model_face, "mesh.obj")