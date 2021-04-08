# RootMotion #
# By Daniel - CompanyBR
# Blender 2.79 / UPBGE 0.2.x


import bge

def start(self):
    pass

def update(cont): 
    owner = cont.owner     
    
    enable = True
    physic = False
    
    if enable == True:
        if physic == True:
            owner.restorePhysics()
        else:
            owner.suspendPhysics(1)
        
        
        # OBJECTS
        root = owner.childrenRecursive['Root']
        arm = owner.childrenRecursive['Armature']
        frame = arm.getActionFrame()
        
        # PLAYER          
        if frame > 2:
            owner.worldPosition = owner.worldPosition.lerp(root.worldPosition, 1)
        
        # ROOT
        root.worldPosition = root.worldPosition.lerp(owner.worldPosition, 1)
        owner.worldOrientation[2][1] = 0